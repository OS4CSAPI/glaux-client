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


def main() -> None:
    doc = json.loads((BASE / (NAME + ".json")).read_text(encoding="utf-8"))
    with (BASE / (NAME + ".csv")).open(newline="", encoding="utf-8") as f:
        mirror = list(csv.reader(f))
    md = (BASE / (NAME + ".md")).read_text(encoding="utf-8")

    if "review_grid" in doc and "columns" in doc:
        if len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.15" and doc.get("SOSAEvidence", {}).get("G2_7A"):
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
