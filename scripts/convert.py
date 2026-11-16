#!/usr/bin/env python3
"""Reproduce strokes.bin and components.bin from upstream Make Me a Hanzi.

Usage:
    python3 scripts/convert.py /path/to/makemeahanzi

Expects graphics.txt and dictionary.txt as provided by
https://github.com/skishore/makemeahanzi

Run this to verify that this repository's data is an unaltered conversion.
"""
import gzip
import json
import os
import sqlite3
import sys
import tempfile

PROVENANCE = (
    "Converted from Make Me a Hanzi graphics.txt (Arphic Public License, "
    "copyright 1999 Arphic Technology Co., Ltd.) to a gzipped SQLite database by HanziLens "
    "on 2025-11-15. No glyph geometry, stroke order or median point was altered. "
    "Converted file published at https://github.com/MaximeLeBesnerais/hanzilens-hanzi-data"
)


def build_strokes(graphics_path: str, out_path: str) -> int:
    rows = []
    with open(graphics_path, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            rows.append((
                d["character"],
                json.dumps(d["strokes"], ensure_ascii=False, separators=(",", ":")),
                json.dumps(d["medians"], ensure_ascii=False, separators=(",", ":")),
            ))
    tmp = tempfile.mktemp(suffix=".db")
    c = sqlite3.connect(tmp)
    c.execute("create table strokes (character text primary key, strokes text, medians text)")
    c.executemany("insert into strokes values (?,?,?)", rows)
    c.execute("create table meta (key text primary key, value text)")
    c.executemany("insert or replace into meta values (?,?)", [
        ("provenance", PROVENANCE),
        ("source", "Make Me a Hanzi graphics.txt / AR PL KaitiM GB, AR PL UKai"),
        ("license", "Arphic Public License (see ARPHICPL.TXT)"),
        ("conversion_date", "2025-11-15"),
    ])
    c.commit()
    c.execute("vacuum")
    c.close()
    raw = open(tmp, "rb").read()
    with gzip.open(out_path, "wb", compresslevel=6) as g:
        g.write(raw)
    os.unlink(tmp)
    return len(rows)


def build_components(dict_path: str, out_path: str) -> int:
    lines = []
    with open(dict_path, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            et = d.get("etymology") or {}
            lines.append("\t".join([
                d["character"],
                d.get("radical", ""),
                d.get("decomposition", ""),
                et.get("semantic", "") or "",
                et.get("phonetic", "") or "",
                et.get("hint", "") or "",
            ]))
    with gzip.open(out_path, "wb", compresslevel=6) as g:
        g.write(("\n".join(lines) + "\n").encode("utf-8"))
    return len(lines)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    src = sys.argv[1]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    n1 = build_strokes(os.path.join(src, "graphics.txt"), os.path.join(root, "strokes.bin"))
    n2 = build_components(os.path.join(src, "dictionary.txt"), os.path.join(root, "components.bin"))
    print(f"strokes.bin: {n1} characters")
    print(f"components.bin: {n2} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
