# Provenance and modifications

Recorded as required by the Arphic Public License, section 2(a):
*"You must insert a prominent notice in each modified file stating how and when
you changed that file."*

## `strokes.bin`

- **Upstream:** `graphics.txt` from
  [skishore/makemeahanzi](https://github.com/skishore/makemeahanzi)
- **Underlying fonts:** AR PL KaitiM GB and AR PL UKai, copyright 1999 Arphic
  Technology Co., Ltd.
- **License:** Arphic Public License
- **When:** converted 2025-11-15, provenance table added 2026-11-16
- **How:** JSON-lines → gzipped SQLite. One row per character, with the
  `strokes` and `medians` JSON fields preserved verbatim as text columns. A
  `meta` table was added inside the database carrying this same notice.
- **Data altered:** none. Glyph paths, stroke order and median points are
  byte-identical to upstream after JSON parsing.

## `components.bin`

- **Upstream:** `dictionary.txt` from
  [skishore/makemeahanzi](https://github.com/skishore/makemeahanzi)
- **Underlying data:** Unihan database, CJKlib
- **License:** GNU Lesser General Public License, version 3 or later
- **When:** converted 2025-11-15
- **How:** JSON-lines → tab-separated, gzipped text. Fields kept:
  `radical`, `decomposition`, `etymology.semantic`, `etymology.phonetic`,
  `etymology.hint`.
- **Data altered:** none. A field-by-field comparison against upstream
  `dictionary.txt` confirmed 9,574/9,574 rows identical and 0 field mismatches.

## Verification

The comparison was performed by parsing both the upstream JSON and the
converted file and diffing every field for every character. The 9,574 row count
matches upstream coverage exactly.

## Why these files are here

`graphics.txt` and `dictionary.txt` are licensed works. Repackaging them into a
format HanziLens can load is a *modification* under both licenses, which
requires making the modified data freely available. This repository is that
designated place.
