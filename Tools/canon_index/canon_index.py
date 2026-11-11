#!/usr/bin/env python3
"""Canon index: hybrid keyword + semantic search over design/ and the rulings ledger.

    python tools/canon_index/canon_index.py build            # incremental (changed files only)
    python tools/canon_index/canon_index.py search "arcade token price"
    python tools/canon_index/canon_index.py search "who runs the claw machine" --rulings
    python tools/canon_index/canon_index.py stats

Keyword search (SQLite FTS5, BM25) needs only the standard library. Semantic search
needs the venv in tools/canon_index/.venv (see README); without it, search falls back
to keyword-only and says so.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DB_PATH = HERE / ".index" / "canon.db"
MODEL_NAME = "Qwen/Qwen3-Embedding-0.6B"
MAX_CHARS = 1500  # chunk size; ~400 tokens
TEXT_EXT = {".md", ".txt", ".json", ".docx"}
SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules", ".index"}

# The rulings ledger and the standing author laws. Results from these are labelled RULING.
RULING_FILES = {
    "docs/superpowers/NEXT_WORK.md",
    "docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md",
    "design/narrative/bros_choose_debauchery.md",
    "design/mechanics/intoxication_law.md",
}
RULES_FILES = {".claude/CLAUDE.md"}


def kind_of(rel: str) -> str:
    if rel in RULING_FILES:
        return "ruling"
    if rel in RULES_FILES:
        return "rules"
    low = rel.lower()
    if low.startswith("design/legacy/"):
        return "legacy"
    if low.startswith("design/templates/"):
        return "template"
    return "design"


def source_files() -> list[Path]:
    out = []
    for p in (ROOT / "design").rglob("*"):
        if p.is_file() and p.suffix.lower() in TEXT_EXT and not (SKIP_DIRS & set(p.parts)):
            out.append(p)
    for rel in sorted(RULING_FILES | RULES_FILES):
        p = ROOT / rel
        if p.is_file() and p not in out:
            out.append(p)
    return out


# ---------------------------------------------------------------- chunking

def _windows(blocks: list[tuple[int, str]], merge: bool) -> list[tuple[int, str]]:
    """Merge (line, text) blocks into chunks of at most MAX_CHARS; split oversize blocks."""
    out: list[tuple[int, str]] = []
    cur_line, cur = None, ""
    for line, text in blocks:
        while len(text) > MAX_CHARS:  # hard split very long blocks
            cut = text.rfind(" ", 0, MAX_CHARS)
            cut = cut if cut > MAX_CHARS // 2 else MAX_CHARS
            if cur:
                out.append((cur_line, cur)); cur_line, cur = None, ""
            out.append((line, text[:cut])); text = text[cut:].lstrip()
        if not merge:
            if len(text) < 80 and cur:  # glue tiny fragments to their neighbour
                cur += "\n" + text
                continue
            if cur:
                out.append((cur_line, cur))
            cur_line, cur = line, text
            continue
        if cur and len(cur) + len(text) + 1 > MAX_CHARS:
            out.append((cur_line, cur)); cur_line, cur = None, ""
        if not cur:
            cur_line = line
        cur = f"{cur}\n{text}" if cur else text
    if cur:
        out.append((cur_line, cur))
    return out


BULLET = re.compile(r"^(\s{0,1}[-*+]|\d+[.)])\s")


def chunk_markdown(text: str, ruling: bool) -> list[tuple[int, str, str]]:
    """Return (line, heading_path, text). Rulings split per top-level bullet."""
    chunks = []
    stack: list[str] = []
    blocks: list[tuple[int, str]] = []
    para_line, para = None, []
    in_code = False

    def end_para():
        nonlocal para_line, para
        if para:
            blocks.append((para_line, "\n".join(para).strip()))
        para_line, para = None, []

    def flush_section():
        end_para()
        heading = " > ".join(stack)
        for line, body in _windows([b for b in blocks if b[1]], merge=not ruling):
            chunks.append((line, heading, body))
        blocks.clear()

    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        if line.lstrip().startswith("```"):
            in_code = not in_code
        m = None if in_code else re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            flush_section()
            level = len(m.group(1))
            stack[:] = stack[: level - 1] + [m.group(2).strip()]
            continue
        if not line.strip():
            end_para(); continue
        if ruling and not in_code and BULLET.match(line):
            end_para()
        if para_line is None:
            para_line = i
        para.append(line)
    flush_section()
    return chunks


def chunk_json(raw: str) -> list[tuple[int, str, str]]:
    try:
        data = json.loads(raw)
    except ValueError:
        return chunk_markdown(raw, ruling=False)
    lines = raw.splitlines()

    def line_of(key: str, start: int) -> int:
        needle = json.dumps(key)
        for j in range(start, len(lines)):
            if needle in lines[j]:
                return j + 1
        return start + 1

    out = []
    pos = 0

    def emit(path: list[str], value):
        nonlocal pos
        body = json.dumps(value, ensure_ascii=False, indent=1)
        if len(body) <= MAX_CHARS or not isinstance(value, (dict, list)):
            ln = line_of(path[-1], pos) if path else 1
            pos = max(pos, ln - 1)
            for k, (_, piece) in enumerate(_windows([(ln, body)], merge=True)):
                out.append((ln, " > ".join(path), piece))
            return
        items = value.items() if isinstance(value, dict) else ((str(i), v) for i, v in enumerate(value))
        for k, v in items:
            emit(path + [str(k)], v)

    emit([], data)
    return out


def chunk_docx(path: Path) -> list[tuple[int, str, str]]:
    try:
        xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8", "ignore")
    except (zipfile.BadZipFile, KeyError, OSError):
        return []
    paras = []
    for n, p in enumerate(re.split(r"</w:p>", xml), 1):
        t = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)).strip()
        if t:
            paras.append((n, t))
    return [(ln, "", body) for ln, body in _windows(paras, merge=True)]


def chunk_file(path: Path, kind: str) -> list[tuple[int, str, str]]:
    suf = path.suffix.lower()
    if suf == ".docx":
        return chunk_docx(path)
    raw = path.read_text(encoding="utf-8", errors="replace")
    if suf == ".json":
        return chunk_json(raw)
    return chunk_markdown(raw, ruling=(kind == "ruling"))


# ---------------------------------------------------------------- storage

def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    # WAL lets searches read while a build is writing; the timeout rides out brief write locks.
    db = sqlite3.connect(DB_PATH, timeout=60)
    db.execute("PRAGMA busy_timeout=60000")
    if db.execute("PRAGMA journal_mode").fetchone()[0].lower() != "wal":
        try:
            db.execute("PRAGMA journal_mode=WAL")
        except sqlite3.OperationalError:
            pass  # a build holds the lock; the next connection switches
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS files(path TEXT PRIMARY KEY, sha TEXT, kind TEXT);
        CREATE TABLE IF NOT EXISTS chunks(id INTEGER PRIMARY KEY, path TEXT, kind TEXT,
            heading TEXT, line INTEGER, text TEXT, emb BLOB);
        CREATE INDEX IF NOT EXISTS chunks_path ON chunks(path);
        CREATE VIRTUAL TABLE IF NOT EXISTS fts USING fts5(heading, text,
            tokenize='porter unicode61');
        CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY, value TEXT);
        """
    )
    return db


def load_model():
    """Return a SentenceTransformer, or None if the venv packages are missing."""
    import os

    # Use the cached copy without asking the Hub for updates (saves seconds per search);
    # fall back to online only for the first download.
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    try:
        import torch
        from sentence_transformers import SentenceTransformer
    except ImportError:
        return None
    cuda = torch.cuda.is_available()
    kwargs = dict(
        device="cuda" if cuda else "cpu",
        model_kwargs={"torch_dtype": torch.float16 if cuda else torch.float32},
        tokenizer_kwargs={"padding_side": "left"},
    )
    try:
        model = SentenceTransformer(MODEL_NAME, **kwargs)
    except OSError:  # not cached yet
        os.environ["HF_HUB_OFFLINE"] = "0"
        import huggingface_hub.constants as hc
        hc.HF_HUB_OFFLINE = False
        model = SentenceTransformer(MODEL_NAME, **kwargs)
    model.max_seq_length = 512
    return model


QUERY_PROMPT = "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery:"


def embed_query(q: str):
    """Embed one search query with plain transformers (imports ~4x faster than
    sentence-transformers). Same prompt, last-token pooling and normalisation as
    the sentence-transformers model used at build time. Returns float32 or None."""
    import os

    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    try:
        import torch
        from transformers import AutoModel, AutoTokenizer
    except ImportError:
        return None
    cuda = torch.cuda.is_available()
    tok = AutoTokenizer.from_pretrained(MODEL_NAME, padding_side="left")
    model = AutoModel.from_pretrained(MODEL_NAME, torch_dtype=torch.float16 if cuda else torch.float32)
    model.to("cuda" if cuda else "cpu").eval()
    batch = tok([QUERY_PROMPT + q], return_tensors="pt", truncation=True, max_length=512).to(model.device)
    with torch.no_grad():
        last = model(**batch).last_hidden_state[:, -1]
    vec = torch.nn.functional.normalize(last.float(), dim=-1)[0]
    return vec.cpu().numpy()


def embed_text(path: str, heading: str, text: str) -> str:
    return f"{path} | {heading}\n{text}" if heading else f"{path}\n{text}"


def cmd_build(args) -> None:
    import time

    db = connect()
    known = {p: s for p, s in db.execute("SELECT path, sha FROM files")}
    seen = set()
    changed = 0
    t0 = time.time()
    for path in source_files():
        rel = path.relative_to(ROOT).as_posix()
        seen.add(rel)
        sha = hashlib.sha1(path.read_bytes()).hexdigest()
        if known.get(rel) == sha and not args.full:
            continue
        kind = kind_of(rel)
        ids = [r[0] for r in db.execute("SELECT id FROM chunks WHERE path=?", (rel,))]
        db.executemany("DELETE FROM fts WHERE rowid=?", [(i,) for i in ids])
        db.execute("DELETE FROM chunks WHERE path=?", (rel,))
        for line, heading, text in chunk_file(path, kind):
            cur = db.execute(
                "INSERT INTO chunks(path, kind, heading, line, text) VALUES (?,?,?,?,?)",
                (rel, kind, heading, line, text),
            )
            db.execute("INSERT INTO fts(rowid, heading, text) VALUES (?,?,?)", (cur.lastrowid, heading, text))
        db.execute("INSERT OR REPLACE INTO files VALUES (?,?,?)", (rel, sha, kind))
        changed += 1
    gone = set(known) - seen
    for rel in gone:
        ids = [r[0] for r in db.execute("SELECT id FROM chunks WHERE path=?", (rel,))]
        db.executemany("DELETE FROM fts WHERE rowid=?", [(i,) for i in ids])
        db.execute("DELETE FROM chunks WHERE path=?", (rel,))
        db.execute("DELETE FROM files WHERE path=?", (rel,))
    db.commit()
    total = db.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    print(f"keyword index: {changed} file(s) updated, {len(gone)} removed, {total} chunks ({time.time() - t0:.1f}s)")

    if args.no_embed:
        return
    stored = dict(db.execute("SELECT key, value FROM meta"))
    if stored.get("model") not in (None, MODEL_NAME):
        db.execute("UPDATE chunks SET emb=NULL")
    todo = db.execute("SELECT id, path, heading, text FROM chunks WHERE emb IS NULL").fetchall()
    if not todo:
        print("embeddings: up to date")
        if changed or gone or not MATRIX.exists():
            write_matrix(db)
        return
    model = load_model()
    if model is None:
        print("embeddings: skipped (venv not installed; keyword search still works, see README)")
        return
    import numpy as np

    todo.sort(key=lambda r: len(r[3]))  # similar lengths batch faster
    t1 = time.time()
    batch = 16
    for i in range(0, len(todo), batch):
        rows = todo[i : i + batch]
        vecs = model.encode([embed_text(r[1], r[2], r[3]) for r in rows], normalize_embeddings=True)
        db.executemany(
            "UPDATE chunks SET emb=? WHERE id=?",
            [(np.asarray(v, dtype=np.float16).tobytes(), r[0]) for v, r in zip(vecs, rows)],
        )
        if (i // batch) % 50 == 0:
            db.commit()
            print(f"  embedded {min(i + batch, len(todo))}/{len(todo)} ({time.time() - t1:.0f}s)", flush=True)
    db.execute("INSERT OR REPLACE INTO meta VALUES ('model', ?)", (MODEL_NAME,))
    db.commit()
    print(f"embeddings: {len(todo)} chunk(s) in {time.time() - t1:.0f}s on {model.device}")
    write_matrix(db)


MATRIX = DB_PATH.parent / "vectors.npy"
MATRIX_IDS = DB_PATH.parent / "vector_ids.npy"


def write_matrix(db) -> None:
    """Cache all vectors as one array; search loads it in a fraction of a second.
    Written by every build that changes anything, so it is never stale."""
    import numpy as np

    rows = db.execute("SELECT id, emb FROM chunks WHERE emb IS NOT NULL ORDER BY id").fetchall()
    if not rows:
        return
    np.save(MATRIX_IDS, np.array([r[0] for r in rows], dtype=np.int64))
    np.save(MATRIX, np.frombuffer(b"".join(r[1] for r in rows), dtype=np.float16).reshape(len(rows), -1))


def load_matrix(db):
    """(ids, float16 matrix), built from SQLite on first use."""
    import numpy as np

    if not (MATRIX.exists() and MATRIX_IDS.exists()):
        write_matrix(db)
        if not MATRIX.exists():
            return None, None
    return np.load(MATRIX_IDS), np.load(MATRIX)


# ---------------------------------------------------------------- search

def fts_query(q: str, op: str) -> str:
    toks = [t for t in re.findall(r"\w+", q.lower()) if len(t) > 1]
    return f" {op} ".join(f'"{t}"' for t in toks)


def keyword_hits(db, q: str, where: str, params: list, limit: int) -> list[int]:
    hits: list[int] = []
    for op in ("AND", "OR"):
        expr = fts_query(q, op)
        if not expr:
            break
        sql = (
            "SELECT c.id FROM fts JOIN chunks c ON c.id = fts.rowid "
            f"WHERE fts MATCH ? {where} ORDER BY bm25(fts, 3.0, 1.0) LIMIT ?"
        )
        for (cid,) in db.execute(sql, [expr, *params, limit]):
            if cid not in hits:
                hits.append(cid)
        if len(hits) >= limit:
            break
    return hits[:limit]


def semantic_hits(db, q: str, where: str, params: list, limit: int):
    try:
        import numpy as np
    except ImportError:
        return None, "venv not installed"
    ids, mat = load_matrix(db)
    if ids is None:
        return None, "no embeddings yet (run build in the venv)"
    allowed = {r[0] for r in db.execute(f"SELECT c.id FROM chunks c WHERE 1=1 {where}", params)}
    qv = embed_query(q)
    if qv is None:
        return None, "venv not installed"
    scores = mat.astype(np.float32) @ qv  # float16 matmul has no fast path in numpy
    out = []
    for i in np.argsort(-scores):
        cid = int(ids[i])
        if cid in allowed:
            out.append(cid)
            if len(out) >= limit:
                break
    return out, None


def cmd_search(args) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    db = connect()
    clauses, params = [], []
    if args.rulings:
        clauses.append("c.kind IN ('ruling','rules')")
    elif not args.legacy:
        clauses.append("c.kind != 'legacy'")
    if args.path:
        clauses.append("c.path LIKE ?"); params.append(f"%{args.path}%")
    where = "".join(f" AND {c}" for c in clauses)
    pool = max(args.k * 5, 50)

    kw = keyword_hits(db, args.query, where, params, pool) if args.mode != "semantic" else []
    sem: list[int] = []
    if args.mode != "keyword":
        sem, note = semantic_hits(db, args.query, where, params, pool)
        if sem is None:
            print(f"(semantic search unavailable: {note}; keyword results only)\n")
            sem = []

    score: dict[int, float] = {}
    via: dict[int, str] = {}
    for tag, ranked in (("K", kw), ("S", sem)):
        for r, cid in enumerate(ranked):
            score[cid] = score.get(cid, 0.0) + 1.0 / (60 + r)
            via[cid] = via.get(cid, "") + tag
    best = sorted(score, key=score.get, reverse=True)[: args.k]

    results = []
    for cid in best:
        path, kind, heading, line, text = db.execute(
            "SELECT path, kind, heading, line, text FROM chunks WHERE id=?", (cid,)
        ).fetchone()
        results.append({"path": path, "line": line, "kind": kind, "heading": heading,
                        "match": via[cid], "text": text})
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=1))
        return
    if not results:
        print("no matches")
    for n, r in enumerate(results, 1):
        label = {"ruling": "  [RULING]", "rules": "  [CLAUDE.md]", "legacy": "  [LEGACY]",
                 "template": "  [TEMPLATE]"}.get(r["kind"], "")
        loc = f"{r['path']}:{r['line']}"
        print(f"{n:>2}. {loc}{label}  ({r['match']})")
        if r["heading"]:
            print(f"    § {r['heading'][:140]}")
        body = re.sub(r"\s+", " ", r["text"]).strip()
        print(f"    {body if args.full_text else body[:260] + ('…' if len(body) > 260 else '')}")


def cmd_stats(_args) -> None:
    db = connect()
    for kind, files, chunks, emb in db.execute(
        "SELECT kind, COUNT(DISTINCT path), COUNT(*), SUM(emb IS NOT NULL) FROM chunks GROUP BY kind ORDER BY 3 DESC"
    ):
        print(f"{kind:9} {files:5} files {chunks:6} chunks {emb or 0:6} embedded")
    print("model:", dict(db.execute("SELECT key, value FROM meta")).get("model", "(none)"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="index new and changed files")
    b.add_argument("--full", action="store_true", help="re-chunk every file")
    b.add_argument("--no-embed", action="store_true", help="keyword index only")
    b.set_defaults(func=cmd_build)
    s = sub.add_parser("search", help="hybrid search")
    s.add_argument("query")
    s.add_argument("-k", type=int, default=10)
    s.add_argument("--mode", choices=["hybrid", "keyword", "semantic"], default="hybrid")
    s.add_argument("--rulings", action="store_true", help="only the ledger, author laws and CLAUDE.md")
    s.add_argument("--legacy", action="store_true", help="include design/legacy (excluded by default)")
    s.add_argument("--path", help="only paths containing this text, e.g. debaucheryville")
    s.add_argument("--full-text", action="store_true", help="print whole chunks")
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=cmd_search)
    sub.add_parser("stats").set_defaults(func=cmd_stats)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
