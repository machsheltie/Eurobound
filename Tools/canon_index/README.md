# canon_index

Search over everything in `design/` plus the rulings ledger, so an agent (or the author) can find every ruling, profile and data entry about a subject without re-reading files.

What it indexes:

| Label | Files |
|---|---|
| `[RULING]` | `docs/superpowers/NEXT_WORK.md`, `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md`, `design/narrative/bros_choose_debauchery.md`, `design/mechanics/intoxication_law.md`. Split one chunk per ruling bullet. |
| `[CLAUDE.md]` | `.claude/CLAUDE.md` |
| (none) | `design/**` `.md`, `.json`, `.txt`, `.docx` |
| `[TEMPLATE]` | `design/templates/` |
| `[LEGACY]` | `design/legacy/`, hidden unless you pass `--legacy` |

Each result shows `path:line`, the heading it sits under, and whether keyword search (`K`), semantic search (`S`) or both (`KS`) found it. The two lists are merged with reciprocal-rank fusion.

## Use

```sh
PY=tools/canon_index/.venv/Scripts/python      # or plain `python` for keyword-only

$PY tools/canon_index/canon_index.py build                        # incremental: only changed files
$PY tools/canon_index/canon_index.py search "arcade token price"
$PY tools/canon_index/canon_index.py search "who runs the claw machine" --rulings
$PY tools/canon_index/canon_index.py search "weed villain" --path shamsterdam -k 5
$PY tools/canon_index/canon_index.py search "Pint Pope" --mode semantic   # near-duplicate names/jokes
$PY tools/canon_index/canon_index.py stats
```

Options: `-k N` results (default 10), `--mode hybrid|keyword|semantic`, `--rulings` (ledger, laws and CLAUDE.md only), `--legacy`, `--path TEXT`, `--full-text`, `--json`.

Speed: `--mode keyword` answers in under a second with plain `python`. Hybrid and semantic searches load the embedding model each time, about 10-20 s on the laptop, so batch questions or use keyword mode for exact names.

Run `build` after editing design docs or the ledger. It re-chunks only files whose hash changed and embeds only new chunks, so it takes seconds.

## Setup (once)

Keyword search needs nothing beyond Python 3.12's standard library. Semantic search uses
[Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) (Apache 2.0) on the GPU:

```sh
py -3.12 -m venv tools/canon_index/.venv
tools/canon_index/.venv/Scripts/python -m pip install torch --index-url https://download.pytorch.org/whl/cu128
tools/canon_index/.venv/Scripts/python -m pip install "sentence-transformers>=5" numpy
tools/canon_index/.venv/Scripts/python tools/canon_index/canon_index.py build
```

The first build downloads the model (~1.2 GB, to `~/.cache/huggingface`) and embeds every chunk. On the RTX 5060 that takes a few minutes; on CPU it would take hours, so use the CUDA build of torch (`cu128`, needed for the 50-series). Without the venv, `search` falls back to keyword-only and says so.

The index lives in `tools/canon_index/.index/canon.db` (gitignored, rebuildable). Delete it and run `build` to start fresh.
