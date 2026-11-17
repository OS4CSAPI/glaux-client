#!/usr/bin/env python3
"""Bound console output before it enters a conversation; no token estimate.

read refuses oversized excerpts intact. keys lists immediate children only.
run merges stdout/stderr into a retained temporary log and preserves exit status.
Increase the 4,000-byte default only for a named original-source question.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

DEFAULT_LIMIT = 4000
MAX_LIMIT = 16000


class GuardError(Exception):
    pass


class Parser(argparse.ArgumentParser):
    def error(self, message):
        # argparse's normal error can echo arbitrarily large argument values.
        raise GuardError("invalid arguments; use --help")


def encoded(value, pretty=False):
    return (json.dumps(value, ensure_ascii=False, indent=2 if pretty else None,
                       separators=None if pretty else (",", ":")) + "\n").encode("utf-8")


def bounded(data, limit):
    if len(data) > limit:
        raise GuardError("output exceeds byte limit; narrow the pointer, lines or file list")
    data.decode("utf-8")  # Refuse binary/non-UTF-8 data; never replace source bytes.
    return data


def regular_file(path):
    if not Path(path).is_file():
        raise GuardError("expected a regular file")
    return path


def select_json(path, pointer):
    with open(regular_file(path), encoding="utf-8-sig") as source:
        value = json.load(source)
    if pointer == "":
        return value
    if not pointer.startswith("/"):
        raise GuardError("JSON pointer must be empty or start with /")
    for part in pointer[1:].split("/"):
        if re.search(r"~(?:[^01]|$)", part):
            raise GuardError("invalid JSON pointer escape; use ~0 for ~ and ~1 for /")
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(value, dict):
            if part not in value:
                raise GuardError("JSON pointer key not found")
            value = value[part]
        elif isinstance(value, list):
            if not re.fullmatch(r"0|[1-9][0-9]*", part) or len(part) > len(str(len(value))):
                raise GuardError("invalid JSON pointer array index")
            index = int(part)
            if index >= len(value):
                raise GuardError("JSON pointer array index out of range")
            value = value[index]
        else:
            raise GuardError("JSON pointer traverses a scalar")
    return value


def read_file(args):
    if args.pointer is not None:
        return encoded(select_json(args.file, args.pointer), pretty=True)
    with open(regular_file(args.file), "rb") as source:
        if args.lines is None:
            if os.fstat(source.fileno()).st_size > args.max_bytes:
                raise GuardError("whole file exceeds byte limit; select --pointer or --lines")
            return source.read(args.max_bytes + 1)
        match = re.fullmatch(r"([1-9][0-9]*):([1-9][0-9]*)", args.lines)
        if not match:
            raise GuardError("line range must be START:END, inclusive and 1-based")
        start, end = map(int, match.groups())
        if end < start:
            raise GuardError("line range ends before it starts")
        result = bytearray()
        for number, line in enumerate(source, 1):
            if number >= start:
                result.extend(line)
                if len(result) > args.max_bytes:
                    raise GuardError("selected lines exceed byte limit; choose a smaller range")
            if number == end:
                return bytes(result)
        raise GuardError("line range extends beyond end of file")


def key_list(args):
    value = select_json(args.file, args.pointer)
    types = {dict: "object", list: "array", str: "string", bool: "boolean",
             int: "number", float: "number", type(None): "null"}
    children = value.items() if isinstance(value, dict) else enumerate(value) if isinstance(value, list) else [(None, value)]
    return encoded([{"key": key, "type": types[type(child)],
                     "count": len(child) if isinstance(child, (dict, list, str)) else None}
                    for key, child in children])


def file_stats(args):
    result = []
    for path in args.files:
        digest, count = hashlib.sha256(), 0
        with open(regular_file(path), "rb") as source:
            for block in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(block)
                count += len(block)
        result.append({"path": path, "bytes": count, "sha256": digest.hexdigest()})
    return encoded(result)


def run_command(args):
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        raise GuardError("run requires -- COMMAND [ARGS...]")
    with tempfile.NamedTemporaryFile(prefix="dim-context-", suffix=".log", delete=False) as log:
        summary = {"status": "withheld_non_utf8", "exit_code": -9999999999,
                   "bytes": 99999999999999999999, "log": log.name}
        if len(encoded(summary)) > args.max_bytes:
            raise GuardError("temporary log path exceeds output budget; use a shorter TMPDIR")
        process = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=log,
                                 stderr=subprocess.STDOUT, check=False, shell=False)
        log.flush()
        count = os.fstat(log.fileno()).st_size
        summary = {"status": "emitted", "exit_code": process.returncode,
                   "bytes": count, "log": log.name}
        data = b""
        if count + len(encoded(summary)) <= args.max_bytes:
            log.seek(0)
            data = log.read(args.max_bytes + 1)
            try:
                data.decode("utf-8")
            except UnicodeError:
                summary["status"] = "withheld_non_utf8"
                data = b""
        else:
            summary["status"] = "withheld_oversize"
        report = encoded(summary)
        if len(data) + len(report) > args.max_bytes:
            data = b""
            summary["status"] = "withheld_oversize"
            report = encoded(summary)
        sys.stdout.buffer.write(data)
        sys.stderr.buffer.write(report)
        return process.returncode if process.returncode >= 0 else 128 - process.returncode


def parser():
    root = Parser(description=__doc__)
    sub = root.add_subparsers(dest="action", required=True)
    for name, description in (("read", "Read a complete bounded excerpt"),
                              ("keys", "List immediate JSON keys, types and counts"),
                              ("stat", "Report exact file bytes and SHA-256"),
                              ("run", "Capture a command without a shell")):
        item = sub.add_parser(name, help=description)
        item.add_argument("--max-bytes", type=int, default=DEFAULT_LIMIT,
                          help="total output cap: 512..16000 bytes (default 4000)")
        item.add_argument("--source-question", default="",
                          help="named original-source question; required above 4000 bytes")
        if name == "stat":
            item.add_argument("files", nargs="+")
        elif name == "run":
            item.add_argument("command", nargs=argparse.REMAINDER)
        else:
            item.add_argument("file")
            group = item.add_mutually_exclusive_group()
            group.add_argument("--pointer", default="" if name == "keys" else None,
                               help="RFC 6901 JSON pointer; empty selects the root")
            if name == "read":
                group.add_argument("--lines", help="inclusive START:END, 1-based")
    return root


def main():
    try:
        args = parser().parse_args()
        if not 512 <= args.max_bytes <= MAX_LIMIT:
            raise GuardError("--max-bytes must be between 512 and 16000")
        if args.max_bytes > DEFAULT_LIMIT and not args.source_question.strip():
            raise GuardError("a larger cap requires --source-question naming the original-source question")
        if args.action == "run":
            return run_command(args)
        data = {"read": read_file, "keys": key_list, "stat": file_stats}[args.action](args)
        sys.stdout.buffer.write(bounded(data, args.max_bytes))
        return 0
    except GuardError as error:
        message = str(error)
    except json.JSONDecodeError:
        message = "invalid JSON; inspect the file locally"
    except UnicodeError:
        message = "input is not valid UTF-8"
    except (OSError, ValueError, RecursionError, MemoryError) as error:
        message = "operation failed (" + type(error).__name__ + "); inspect locally"
    except KeyboardInterrupt:
        return 130
    sys.stderr.write("dim_context: " + message + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
