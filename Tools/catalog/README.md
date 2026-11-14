# Catalogue generator

Builds the living catalogue the author asked for (bead Eurobound-yore): one Markdown file per category, a "where we are" page for the game's systems, and one JSON file a web page can read.

## Run it

From the repository root:

```bash
python -I Tools/catalog/build_catalog.py
```

It prints one line per category and writes everything to `docs/catalog/`. It needs Python 3 and nothing else. Re-run it whenever design docs, engine data, art or beads change. Never edit the files in `docs/catalog/` by hand; the next run overwrites them.

| Output | What it lists |
|---|---|
| `locations.md` | Every doc with a Location ID under `design/worlds/<city>/`, plus the `core/` companion JSONs |
| `npcs.md` | NPC profile docs and the `npcs` / `ambient_npcs` lists in the companion JSONs |
| `items.md` | Item docs, companion item JSONs and engine item data, grouped by type |
| `enemies_and_villains.md` | Villain and enemy docs, plus engine entries that have no doc |
| `quests.md` | Everything under `design/quests/`, plus engine quest data |
| `status_effects_and_abilities.md` | The master status list, the abilities in `battle_system.md`, and engine skills data |
| `game_elements_status.md` | One table per system: Designed, Ruled, Built, Tested, Data, What's left, Bead ids |
| `catalog.json` | All of the above as data, plus `duplicates` and `problems` |

`design/legacy/`, `design/World Design/` and `design/templates/` are skipped.

## What the columns mean

- **Detail** is copied from the doc: its italic tagline, or a named field such as Satirical Subtitle. The generator never writes a description. A blank cell is flagged `no summary in doc`.
- **Design doc / Engine data / Art** are yes or no from files found in the repo. Engine data means the id or name appears in `game/assets/data/`. Art means a matching file or folder exists under `game/assets/`.
- **Open beads** are beads that are not closed and mention the row's name, id or doc path.
- **Duplicate names** lists every name used more than once across the game. "Same category" is a real clash. "Across categories" can be one thing listed in two places, so check before renaming. Ambient NPC groups are left out.
- **Flags** note gaps the generator can see: an NPC with no profile doc, an engine entry with no doc of its own, an id that differs between a doc and its JSON.

## The "where we are" page

`game_elements.json` in this folder holds the wording for each row (seeded from `docs/research/2026-11-14-mechanics-gap-audit.md`). On every build the generator adds the live facts: whether the listed design, code, test and data files still exist, and each bead's current status from `bd list --all --json`. Closing a bead changes the page on the next run.

To change a row's wording, edit `game_elements.json`. To throw the seed away and rebuild it from an audit's tables:

```bash
python -I Tools/catalog/build_catalog.py --seed-from-audit docs/research/2026-11-14-mechanics-gap-audit.md
```

That overwrites hand edits to the seed.

## Options

- `--no-beads` skips `bd`; the pages say bead data is missing.
- `--beads-json FILE` reads beads from a saved `bd list --all --json` file.
- `--root`, `--out`, `--seed` point the generator at another tree (the tests use these).

## Tests

```bash
python -I -m unittest discover Tools/tests
```

`Tools/tests/test_build_catalog.py` builds a small fixture tree and checks the output.

## The page

The catalogue is published for the author at https://claude.ai/artifact/Hw6te9KWJBsbuED1TAFU79 (one tab per category, plus "Where we are" and duplicate names). The page source is `Tools/catalog/page/eurobound_catalog.html`; it reads `catalog.json` published beside it.

To refresh it: run the generator, then publish with the Artifact tool, passing `url` (the link above), `file_path` (the page source) and `files: {"catalog.json": "docs/catalog/catalog.json"}`. The lead session does this on upkeep runs when `docs/catalog/catalog.json` has changed.
