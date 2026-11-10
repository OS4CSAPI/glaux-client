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



def main() -> None:
    doc = json.loads((BASE / (NAME + ".json")).read_text(encoding="utf-8"))
    with (BASE / (NAME + ".csv")).open(newline="", encoding="utf-8") as f:
        mirror = list(csv.reader(f))
    md = (BASE / (NAME + ".md")).read_text(encoding="utf-8")

    if "review_grid" in doc and "columns" in doc:
        if len(doc["columns"]) == 15 and doc.get("schemaVersion") == "0.12":
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
