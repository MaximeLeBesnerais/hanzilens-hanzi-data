# hanzilens-hanzi-data

Converted Chinese stroke-order and character-decomposition data used by
[HanziLens](https://github.com/MaximeLeBesnerais/HanziLens).

This repository exists to satisfy the publication requirements of the
licenses that cover the upstream data: the **Arphic Public License** for the
stroke graphics, and the **LGPL-3.0-or-later** for the character dictionary.

| File | Rows | Upstream | License |
|------|------|----------|---------|
| `strokes.bin` | 9,574 characters | [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) `graphics.txt` | Arphic Public License |
| `components.bin` | 9,574 characters | [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) `dictionary.txt` | LGPL-3.0-or-later |
| `cedict.db.gz` | 124,161 entries | [CC-CEDICT](https://cc-cedict.org/) text export | CC BY-SA 4.0 |

All files are **format conversions only**. No glyph geometry, stroke order,
median point, radical, decomposition or etymology field was altered. See
[PROVENANCE.md](./PROVENANCE.md) for the exact transformation.

## Files

### `strokes.bin` — gzipped SQLite

```
table strokes(character TEXT, strokes TEXT, medians TEXT)
table meta(key TEXT, value TEXT)   -- includes the conversion provenance notice
```

`strokes` holds the SVG path list for each character as a JSON array.
`medians` holds the intermediate points of each stroke as a JSON array of
`[x, y]` pairs.

### `components.bin` — gzipped TSV

Nine tab-separated columns per line:

```
character \t radical \t decomposition \t semantic \t phonetic \t etymology_hint
```

(the remaining columns are empty padding retained from the original converter).

### `cedict.db.gz` — gzipped SQLite

```
table entries(id, simplified, traditional, pinyin, freq_score, gloss)
table meta(key TEXT, value TEXT)   -- conversion provenance notice
```

CC-CEDICT is a Chinese–English dictionary. The conversion keeps every entry and
field; only the container changed.

## Licenses

- `licenses/ARPHICPL.txt` — Arphic Public License, retained unaltered as required
  by section 1 of that license.
- The `dictionary.txt`-derived data is GNU LGPL v3 or later; the Unihan and
  CJKlib copyright notices apply to it.
- `cedict.db.gz` is licensed **CC BY-SA 4.0**. The dictionary content remains
  available under that license and this conversion is released under the same
  terms. Attribution: CC-CEDICT project, https://cc-cedict.org/

## Attribution

Stroke order graphics descend from the **AR PL KaitiM GB** and **AR PL UKai**
fonts, copyright 1999 Arphic Technology Co., Ltd., released under the Arphic
Public License.

Character decomposition data descends from the **Unihan** database and
**CJKlib**.
