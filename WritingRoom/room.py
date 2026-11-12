#!/usr/bin/env python3
"""Eurobound Writing Room: four OpenRouter writers collaborating on author-assigned tasks.

Usage (run from anywhere):
  python room.py go "Write bar NPC barks for Shamsterdam"      # new task + run it
  python room.py new "Title" --brief "..." | --brief-file path  # create a task only
  python room.py run <task> [--rounds N] [--budget USD] [--writers Kimi,GLM]
  python room.py note <task> "Cut the cat joke. More menace."  # author note, then `run` again
  python room.py status [<task>]
  python room.py ping                                           # check every writer answers

Stdlib only. API key comes from WritingRoom/.env (OPENROUTER_API_KEY=...).
"""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOM = Path(__file__).resolve().parent
REPO = ROOM.parent
TASKS = ROOM / "tasks"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
PROTECTED = {"thread.md", "state.json", "brief.md", "log.jsonl", "questions_for_author.md", "questions.json",
             "author_reviews.md"}
WRITABLE_TOP = {"final.md", "critiques.md", "canon_proposals.md"}
# Guardrails (author order, 2026-11-09): writers never edit the room's records.
MODERATOR_ONLY = {"decisions.md", "drafts/story_break.md"}   # only the moderator writes these; writers propose in the thread
APPEND_ONLY = {"critiques.md", "canon_proposals.md"}         # shared logs: add a section, never rewrite
WRITER_KEYS = {"kimi", "gemini", "glm", "aion"}
READ_EXCLUDE_DIRS = {".git", ".godot", "node_modules", "__pycache__", ".import", "builds"}
TEXT_EXT = {".md", ".txt", ".json", ".csv", ".tsv", ".gd", ".tres", ".tscn", ".cfg", ".yaml",
            ".yml", ".toml", ".dialogue", ".py", ".html", ".rtf"}
MAX_READ_CHARS = 60000

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# ---------------------------------------------------------------- config / io

def load_config() -> dict:
    return json.loads((ROOM / "room_config.json").read_text(encoding="utf-8"))


def api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY")
    env = ROOM / ".env"
    if not key and env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("OPENROUTER_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        sys.exit("No OPENROUTER_API_KEY in environment or WritingRoom/.env")
    return key


def now() -> str:
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M")


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return s[:40] or "task"


def task_dir(task: str) -> Path:
    d = TASKS / task
    if not d.is_dir():
        matches = [p for p in TASKS.iterdir() if p.is_dir() and task in p.name] if TASKS.exists() else []
        if len(matches) == 1:
            return matches[0]
        sys.exit(f"Task not found (or ambiguous): {task}")
    return d


def load_state(d: Path) -> dict:
    return json.loads((d / "state.json").read_text(encoding="utf-8"))


def save_state(d: Path, state: dict) -> None:
    (d / "state.json").write_text(json.dumps(state, indent=2), encoding="utf-8")


def load_questions(d: Path) -> list:
    p = d / "questions.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


def save_questions(d: Path, qs: list) -> None:
    (d / "questions.json").write_text(json.dumps(qs, indent=2), encoding="utf-8")


def append(path: Path, text: str) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(text)


# ---------------------------------------------------------------- bible

def extract_sections(text: str, wanted: list[str]) -> str:
    out, keep = [], False
    for line in text.splitlines():
        m = re.match(r"^##\s+(.*)", line)
        if m:
            keep = any(m.group(1).strip().startswith(w) for w in wanted)
        if keep:
            out.append(line)
    return "\n".join(out)


def build_bible(cfg: dict) -> str:
    parts = []
    for f in sorted((ROOM / "bible").glob("*.md")):
        parts.append(f.read_text(encoding="utf-8"))
    for item in cfg.get("bible_live_files", []):
        p = REPO / item["path"]
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if item.get("sections"):
            text = extract_sections(text, item["sections"])
        parts.append(f"# From `{item['path']}` (live project file)\n\n{text}")
    hits = glob.glob(os.path.expanduser(cfg.get("satire_voice_glob", "")))
    if hits:
        text = Path(hits[0]).read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"^---.*?---\s*", "", text, flags=re.S)
        parts.append("# Eurobound Satire Voice (binding creative authority)\n\n" + text)
    elif (ROOM / "bible" / "satire_voice_snapshot.md").exists():
        pass  # already included via bible/*.md
    return "\n\n---\n\n".join(parts)


# ---------------------------------------------------------------- tools

TOOLS = [
    {"type": "function", "function": {
        "name": "list_files",
        "description": "List files and folders at a repo-relative path (e.g. 'design/narrative' or the task folder).",
        "parameters": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}}},
    {"type": "function", "function": {
        "name": "read_file",
        "description": "Read a text file by repo-relative path. Large files are returned in chunks; pass offset to continue.",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"}, "offset": {"type": "integer", "description": "char offset, default 0"}},
            "required": ["path"]}}},
    {"type": "function", "function": {
        "name": "search",
        "description": "Case-insensitive regex search across the project's text files. Use it to check a name is unused before you coin it, or to find canon.",
        "parameters": {"type": "object", "properties": {
            "pattern": {"type": "string"},
            "path": {"type": "string", "description": "repo-relative folder to limit the search, default whole repo"}},
            "required": ["pattern"]}}},
    {"type": "function", "function": {
        "name": "write_file",
        "description": "Create or overwrite a file. Only allowed inside this task's folder. Path is relative to the task folder (e.g. 'drafts/kimi_barks.md' or 'final.md').",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"}, "content": {"type": "string"}}, "required": ["path", "content"]}}},
    {"type": "function", "function": {
        "name": "append_file",
        "description": "Append text to the end of a file in this task's folder (creates it if missing). Use it to write long drafts in parts: write_file the first part, then append_file the rest, at most ~4000 words per call.",
        "parameters": {"type": "object", "properties": {
            "path": {"type": "string"}, "content": {"type": "string"}}, "required": ["path", "content"]}}},
    {"type": "function", "function": {
        "name": "ask_author",
        "description": ("Ask the author something only they can decide (story, canon, mechanics, numbers, ambiguity). "
                        "The moderator delivers it; the answer comes back in the thread as AUTHOR ANSWERS. Prefer a "
                        "yes/no or 2-4 concrete options over open questions. One decision per call."),
        "parameters": {"type": "object", "properties": {
            "question": {"type": "string", "description": "the decision, phrased so it can be answered without reading the thread"},
            "kind": {"type": "string", "enum": ["yes_no", "options", "open"]},
            "options": {"type": "array", "items": {"type": "string"}, "description": "2-4 choices when kind=options"},
            "context": {"type": "string", "description": "one or two lines on why it matters / what each choice changes"}},
            "required": ["question", "kind"]}}},
    {"type": "function", "function": {
        "name": "vote_done",
        "description": "Declare whether you think the deliverable is finished and good enough for the author. The task ends when every writer votes done in the same round.",
        "parameters": {"type": "object", "properties": {
            "done": {"type": "boolean"}, "note": {"type": "string"}}, "required": ["done"]}}},
]


def safe_repo_path(rel: str) -> Path:
    p = (REPO / rel.strip().lstrip("/\\")).resolve()
    if REPO not in p.parents and p != REPO:
        raise ValueError("path outside the project")
    parts = set(p.relative_to(REPO).parts)
    if parts & {".git"} or p.name == ".env":
        raise ValueError("that path is off limits")
    return p


class Toolbox:
    def __init__(self, d: Path, writer: str, state: dict, round_no: int):
        self.d, self.writer, self.state, self.round_no = d, writer, state, round_no
        self.touched: list[str] = []

    def run(self, name: str, args: dict) -> str:
        args = {k: v for k, v in args.items() if not str(k).startswith("_")}  # internal flags are not writer-settable
        try:
            return getattr(self, "t_" + name)(**args)
        except AttributeError:
            return f"ERROR: unknown tool {name}"
        except TypeError as e:
            return f"ERROR: bad arguments: {e}"
        except Exception as e:  # tool errors go back to the model, not up the stack
            return f"ERROR: {e}"

    def t_list_files(self, path: str = ".") -> str:
        p = safe_repo_path(path)
        if not p.is_dir():
            return "ERROR: not a folder"
        rows = []
        for c in sorted(p.iterdir()):
            if c.name in READ_EXCLUDE_DIRS or c.name == ".env":
                continue
            rows.append(c.name + ("/" if c.is_dir() else f"  ({c.stat().st_size} bytes)"))
        return "\n".join(rows[:300]) or "(empty)"

    def t_read_file(self, path: str, offset: int = 0) -> str:
        p = safe_repo_path(path)
        if not p.is_file():
            return "ERROR: no such file"
        if p.suffix.lower() not in TEXT_EXT:
            return "ERROR: not a text file this room can read"
        text = p.read_text(encoding="utf-8", errors="replace")
        chunk = text[offset:offset + MAX_READ_CHARS]
        more = len(text) - (offset + len(chunk))
        tail = f"\n\n[... {more} more chars; call read_file with offset={offset + len(chunk)}]" if more > 0 else ""
        return chunk + tail

    def t_search(self, pattern: str, path: str = ".") -> str:
        rx = re.compile(pattern, re.I)
        root = safe_repo_path(path)
        hits = []
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [x for x in dirnames if x not in READ_EXCLUDE_DIRS]
            for fn in filenames:
                fp = Path(dirpath) / fn
                if fp.suffix.lower() not in TEXT_EXT or fn == ".env":
                    continue
                try:
                    for i, line in enumerate(fp.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                        if rx.search(line):
                            hits.append(f"{fp.relative_to(REPO).as_posix()}:{i}: {line.strip()[:200]}")
                            if len(hits) >= 60:
                                return "\n".join(hits) + "\n[truncated at 60 hits]"
                except OSError:
                    continue
        return "\n".join(hits) or "no matches"

    def _resolve(self, path: str) -> tuple[Path, str] | str:
        rel = path.strip().replace("\\", "/").lstrip("/")
        prefix = self.d.resolve().relative_to(REPO).as_posix() + "/"
        if rel.startswith(prefix):  # writer gave a repo-relative path; make it task-relative
            rel = rel[len(prefix):]
        p = (self.d / rel).resolve()
        if self.d.resolve() not in p.parents:
            return "ERROR: you can only write inside this task's folder"
        return p, p.relative_to(self.d.resolve()).as_posix()

    def _guard(self, p: Path, relp: str, appending: bool) -> str | None:
        if p.name in PROTECTED and p.parent == self.d.resolve():
            return f"ERROR: {p.name} is managed by the room; post to the thread instead"
        if relp in MODERATOR_ONLY:
            return (f"ERROR: {relp} is the room's record and only the moderator edits it. "
                    "Put your proposed decisions, rejections and disputes in your thread post; the moderator records them.")
        if not (relp.startswith("drafts/") or relp in WRITABLE_TOP):
            return ("ERROR: writers may only write inside drafts/ or to " + ", ".join(sorted(WRITABLE_TOP)) +
                    ". Everything else in the task folder belongs to the author and is read-only.")
        if relp in APPEND_ONLY and not appending and p.exists() and p.stat().st_size > 0:
            return f"ERROR: {relp} is a shared log; use append_file to add your section. Nobody rewrites it."
        if relp == "final.md" and self.writer != load_config().get("finalizer"):
            return "ERROR: only the integrator writes final.md. Put your notes in critiques.md or your thread post."
        if relp.startswith("drafts/"):
            me = self.writer.lower()
            toks = Path(relp).stem.lower().split("_")
            owner = toks[1] if toks[0].startswith("phase") and len(toks) > 1 else toks[0]
            if owner != me:
                if owner in WRITER_KEYS:
                    return (f"ERROR: {relp} belongs to {owner.upper() if owner == 'glm' else owner.capitalize()}. "
                            "You may read it, but not edit it. Put your review in critiques.md (append_file) or the thread.")
                return f"ERROR: name your draft files with your own name first, e.g. drafts/{me}_<topic>.md"
        return None

    def t_write_file(self, path: str, content: str, _appending: bool = False) -> str:
        r = self._resolve(path)
        if isinstance(r, str):
            return r
        p, relp = r
        err = self._guard(p, relp, _appending)
        if err:
            return err
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        self.touched.append(relp)
        return f"wrote {relp} ({len(content)} chars)"

    def t_append_file(self, path: str, content: str) -> str:
        r = self._resolve(path)
        if isinstance(r, str):
            return r
        p, relp = r
        existing = p.read_text(encoding="utf-8") if p.exists() else ""
        res = self.t_write_file(relp, existing + content, _appending=True)
        return res.replace("wrote", "appended to") if not res.startswith("ERROR") else res

    def t_ask_author(self, question: str, kind: str = "open", options: list | None = None, context: str = "") -> str:
        qs = load_questions(self.d)
        qid = f"q{len(qs) + 1}"
        if kind == "options" and not options:
            kind = "open"
        qs.append({"id": qid, "from": self.writer, "round": self.round_no, "created": now(), "question": question,
                   "kind": kind, "options": options or [], "context": context, "status": "open"})
        save_questions(self.d, qs)
        opts = f" Options: {' / '.join(options)}." if options else ""
        append(self.d / "questions_for_author.md", f"\n- [{qid}] **{self.writer}** (round {self.round_no}): {question}{opts}\n")
        return f"logged as {qid}; the moderator will bring it to the author. Keep working; leave a marked gap if blocked."

    def t_vote_done(self, done: bool, note: str = "") -> str:
        if isinstance(done, str):  # some models send "True"/"false" as strings
            done = done.strip().lower() in {"true", "yes", "1", "done"}
        self.state.setdefault("votes", {})[self.writer] = {"done": bool(done), "round": self.round_no, "note": note}
        return "vote recorded"


# ---------------------------------------------------------------- OpenRouter

class BudgetExceeded(Exception):
    pass


def call_model(key: str, writer: dict, messages: list, cfg: dict, tools: bool = True) -> dict:
    body = {
        "model": writer["model"],
        "messages": messages,
        "max_tokens": writer.get("max_tokens", 8000),
        "temperature": cfg.get("temperature", 0.9),
        "usage": {"include": True},
        **writer.get("params", {}),
    }
    if tools:
        body["tools"] = TOOLS
    data = json.dumps(body).encode("utf-8")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json",
               "HTTP-Referer": "https://localhost/eurobound-writing-room", "X-Title": "Eurobound Writing Room"}
    last = None
    for attempt in range(5):
        try:
            req = urllib.request.Request(API_URL, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=600) as r:
                resp = json.loads(r.read().decode("utf-8"))
            if "error" in resp:
                raise RuntimeError(json.dumps(resp["error"])[:500])
            if not resp.get("choices"):
                raise RuntimeError("empty response")
            return resp
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")[:500]
            last = f"HTTP {e.code}: {msg}"
            if e.code in (400, 401, 402, 403):
                break
        except Exception as e:
            last = str(e)
        time.sleep(min(60, 4 * 2 ** attempt))
    raise RuntimeError(last or "unknown error")


# ---------------------------------------------------------------- turns

PHASES = {
    "source_review": ("PHASE 1 — SOURCE REVIEW AND WORK ALLOCATION (house rules §8). Read the brief and the canon it "
                      "touches yourself. Post: established canon, required elements, material worth preserving, "
                      "conflicts/gaps, and what needs author approval (ask_author). Do NOT lock the creative "
                      "direction or split the work before all four have reviewed."),
    "assessment": ("PHASE 2 — INDEPENDENT CREATIVE ASSESSMENT (§8). Post three strengths to keep, three weaknesses "
                   "to fix, one original proposal, one idea to cut, and one other writer's idea that deserves "
                   "serious consideration. Specific material only; don't restate another writer."),
    "story_break": ("PHASE 3 — STORY AND GAMEPLAY BREAK (§8). Debate and settle the structure: approach, character "
                    "treatment, escalation, beats, player choices, consequences, mechanics, combat roles, continuity. "
                    "State decisions and live disagreements in your thread post; the moderator records them in decisions.md. Author-reserved calls go to ask_author."),
    "drafting": ("PHASE 4 — COORDINATED DRAFTING (§8). Draft your allocated section to its designated file, against "
                 "the shared outline. Name the reviewer for your section. If you are a reviewer, give the primary "
                 "writer concrete, quotable notes in critiques.md and in your post."),
    "review": ("PHASE 5 — ADVERSARIAL EDITORIAL REVIEW (§8). Read the integrated draft (final.md if it exists, "
               "otherwise all drafts). Identify at least two substantive problems in work outside your own section, "
               "against the §8 Phase 5 checklist, and fix or propose fixes. Call vote_done per §14."),
    "final_check": ("PHASE 6 — FINAL QUALITY CONTROL (§8, §14). Read final.md in full. Run the Phase 6 checklist. "
                    "Fix nothing silently: name each remaining defect, or call vote_done(true) if there are none "
                    "blocking."),
}


def turn_prompt(d: Path, state: dict, writer: str, others: list[str], round_no: int, total: int,
                cfg: dict, finalizer: bool) -> str:
    rel = d.relative_to(REPO).as_posix()
    brief = (d / "brief.md").read_text(encoding="utf-8")
    thread = (d / "thread.md").read_text(encoding="utf-8")
    limit = cfg.get("thread_chars_in_prompt", 60000)
    if len(thread) > limit:
        thread = f"[earlier thread truncated — read {rel}/thread.md for all of it]\n\n" + thread[-limit:]
    files = []
    for p in sorted(d.rglob("*")):
        if p.is_file() and p.name not in {"state.json", "log.jsonl"}:
            files.append(f"- {p.relative_to(d).as_posix()} ({p.stat().st_size} bytes)")
    phase = state.get("phase")
    if finalizer:
        stage = ("PHASE 6 — INTEGRATION. You are the integrator. Read the thread, decisions.md and every draft, "
                 "then write `final.md`: one cohesive production candidate with the room's best material and every "
                 "agreed fix and author ruling applied, per house rules §8 Phase 6 and §15. Your job is "
                 "consistency, not unilateral creative authority. Keep PROPOSED labels and [AUTHOR DECISION NEEDED] "
                 "gaps visible. Then post a short summary to the thread.")
    elif phase in PHASES:
        stage = PHASES[phase]
    elif round_no == 1:
        stage = PHASES["source_review"]
    elif round_no >= total:
        stage = PHASES["review"]
    else:
        stage = PHASES["drafting"]
    return f"""You are **{writer}**. The other writers in the room: {', '.join(others)}.
Task folder (repo-relative): `{rel}/` — write_file paths are relative to it.
Round {round_no} of {total}.

## The brief from the author
{brief}

## Files in the task folder
{chr(10).join(files) or '(none yet)'}

## The thread so far
{thread or '(empty — you speak first)'}

## Your turn
{stage}

Use tools as needed, then reply with your thread post (that text is what the room sees)."""


def take_turn(key: str, cfg: dict, d: Path, state: dict, writer: dict, others: list[str],
              round_no: int, total: int, bible: str, budget: float, finalizer: bool = False) -> None:
    name = writer["name"]
    box = Toolbox(d, name, state, round_no)
    msgs = [
        {"role": "system", "content": bible},
        {"role": "user", "content": turn_prompt(d, state, name, others, round_no, total, cfg, finalizer)},
    ]
    max_steps = cfg.get("max_tool_steps_per_turn", 10)
    must_write = state.get("phase") in ("drafting", "review") or finalizer
    nudged = False
    post = ""
    for step in range(max_steps + 1):
        if state["spent_this_run"] >= budget:
            raise BudgetExceeded()
        use_tools = step < max_steps
        if use_tools and must_write and not box.touched and step == max(1, max_steps - 6):
            msgs.append({"role": "user", "content": f"Moderator: you have {max_steps - step} tool steps left and have saved nothing. "
                         "Stop reading. Write your assigned drafts to their files now (write_file, then append_file for later parts)."})
        if not use_tools:
            msgs.append({"role": "user", "content": "Tool budget for this turn is used up. Write your thread post now."})
        resp = call_model(key, writer, msgs, cfg, tools=use_tools)
        usage = resp.get("usage", {}) or {}
        cost = float(usage.get("cost") or 0)
        state["spent_this_run"] += cost
        state["spent_total"] = state.get("spent_total", 0) + cost
        append(d / "log.jsonl", json.dumps({"t": now(), "writer": name, "model": writer["model"], "round": round_no,
                                            "in": usage.get("prompt_tokens"), "out": usage.get("completion_tokens"),
                                            "cost": cost}) + "\n")
        m = resp["choices"][0]["message"]
        finish = resp["choices"][0].get("finish_reason") or resp["choices"][0].get("native_finish_reason")
        calls = m.get("tool_calls") or []
        if finish == "length" and use_tools:
            print(f"    {name}: reply cut off at the length limit; asking for smaller parts")
            msgs.append({"role": "assistant", "content": (m.get("content") or "")[-2000:]})
            msgs.append({"role": "user", "content": "Your last reply was cut off at the output length limit and nothing in it was saved. Save long drafts in parts: write_file the first section, then append_file the remaining sections, at most about 4000 words per call. Keep your reasoning brief. Continue now."})
            continue
        if not calls:
            post = (m.get("content") or "").strip()
            if must_write and not box.touched and not nudged and use_tools:
                nudged = True
                print(f"    {name}: ended without saving any file; sending it back")
                msgs.append({"role": "assistant", "content": post})
                msgs.append({"role": "user", "content": "You have not saved any file this turn. Describing a draft does not create it: nothing exists until you call write_file (and append_file for later parts). Write your assigned drafts to their files now, then give your thread post."})
                continue
            break
        msgs.append({"role": "assistant", "content": m.get("content") or "", "tool_calls": calls})
        for c in calls:
            fn = c.get("function", {})
            try:
                args = json.loads(fn.get("arguments") or "{}")
            except json.JSONDecodeError:
                args = {}
                result = "ERROR: arguments were not valid JSON"
            else:
                result = box.run(fn.get("name", ""), args)
            print(f"    {name} -> {fn.get('name')}({_short(args)})")
            msgs.append({"role": "tool", "tool_call_id": c.get("id"), "name": fn.get("name"), "content": result})
    label = "FINAL PASS" if finalizer else f"Round {round_no}"
    touched = f"\n\n_files: {', '.join(sorted(set(box.touched)))}_" if box.touched else ""
    vote = state.get("votes", {}).get(name)
    vtxt = f"\n_vote: {'DONE' if vote['done'] else 'not done'}{' — ' + vote['note'] if vote.get('note') else ''}_" \
        if vote and vote.get("round") == round_no and not finalizer else ""
    append(d / "thread.md", f"\n### {label} — {name} ({now()})\n\n{post or '(no post)'}{touched}{vtxt}\n")
    print(f"  {name}: posted ({len(post)} chars), run spend ${state['spent_this_run']:.3f}")


def _short(args: dict) -> str:
    s = ", ".join(f"{k}={str(v)[:50]!r}" for k, v in args.items() if k != "content")
    return s + (f", content=<{len(args['content'])} chars>" if "content" in args else "")


# ---------------------------------------------------------------- commands

def cmd_new(title: str, brief: str) -> Path:
    TASKS.mkdir(exist_ok=True)
    tid = dt.datetime.now().strftime("%Y%m%d_%H%M") + "_" + slugify(title)
    d = TASKS / tid
    (d / "drafts").mkdir(parents=True)
    (d / "brief.md").write_text(f"# {title}\n\n{brief.strip()}\n", encoding="utf-8")
    (d / "thread.md").write_text(f"# Thread — {title}\n", encoding="utf-8")
    (d / "questions_for_author.md").write_text("# Questions for the author\n", encoding="utf-8")
    save_state(d, {"title": title, "created": now(), "rounds_done": 0, "status": "open", "spent_total": 0, "votes": {}})
    print(f"Created task: {tid}")
    return d


def cmd_run(d: Path, rounds: int | None, budget: float | None, only: list[str] | None) -> None:
    cfg, key = load_config(), api_key()
    writers = [w for w in cfg["writers"] if not only or w["name"].lower() in [o.lower() for o in only]]
    if not writers:
        sys.exit("No matching writers")
    rounds = rounds or cfg.get("default_rounds", 3)
    budget = budget if budget is not None else cfg.get("budget_usd_per_run", 3.0)
    bible = build_bible(cfg)
    state = load_state(d)
    state["spent_this_run"] = 0.0
    state.pop("phase", None)
    state["status"] = "running"
    state["votes"] = {}
    start = state.get("rounds_done", 0)
    total = start + rounds
    names = [w["name"] for w in writers]
    print(f"Task {d.name}: rounds {start + 1}-{total}, writers {', '.join(names)}, budget ${budget:.2f}")
    finished = False
    try:
        for r in range(start + 1, total + 1):
            print(f"\n== Round {r} ==")
            k = (r - 1) % len(writers)
            order = writers[k:] + writers[:k]
            for w in order:
                try:
                    take_turn(key, cfg, d, state, w, [n for n in names if n != w["name"]], r, total, bible, budget)
                except BudgetExceeded:
                    raise
                except Exception as e:
                    print(f"  {w['name']}: FAILED ({e}) — skipping turn")
                    append(d / "thread.md", f"\n### Round {r} — {w['name']}\n\n_(missed this turn: {str(e)[:200]})_\n")
                save_state(d, state)
            state["rounds_done"] = r
            save_state(d, state)
            votes = state.get("votes", {})
            if all(votes.get(n, {}).get("done") and votes[n].get("round") == r for n in names):
                print("\nEvery writer voted done.")
                finished = True
                break
        fin_name = cfg.get("finalizer") if cfg.get("finalizer") in names else names[0]
        fin = next(w for w in writers if w["name"] == fin_name)
        print(f"\n== Final pass ({fin_name}) ==")
        take_turn(key, cfg, d, state, fin, [n for n in names if n != fin_name], state["rounds_done"],
                  state["rounds_done"], bible, budget + 1.0, finalizer=True)  # small reserve so final.md always lands
        state["status"] = "done" if finished else "awaiting author (rounds used up)"
    except BudgetExceeded:
        state["status"] = "paused: budget reached"
        append(d / "thread.md", f"\n_(room paused: run budget ${budget:.2f} reached)_\n")
        print("\nBudget reached; paused.")
    save_state(d, state)
    print(f"\nStatus: {state['status']}. This run: ${state['spent_this_run']:.3f}. Task total: ${state['spent_total']:.3f}")
    print(f"Read: {d / 'final.md'}\n      {d / 'thread.md'}\n      {d / 'questions_for_author.md'}")


def cmd_round(d: Path, phase: str, budget: float | None, only: list[str] | None, no_advance: bool = False) -> None:
    """Moderated mode: run exactly one round, no auto-finalize. Prints a JSON report for the moderator."""
    cfg, key = load_config(), api_key()
    writers = [w for w in cfg["writers"] if not only or w["name"].lower() in [o.lower() for o in only]]
    names = [w["name"] for w in writers]
    budget = budget if budget is not None else cfg.get("budget_usd_per_run", 3.0)
    bible = build_bible(cfg)
    state = load_state(d)
    state.update(spent_this_run=0.0, status="round running", votes={})
    r = state.get("rounds_done", 0) + 1
    state["phase"] = phase
    total = r + 1
    before = {q["id"] for q in load_questions(d)}
    print(f"== Round {r} ({phase}) — {', '.join(names)} — budget ${budget:.2f} ==")
    k = (r - 1) % len(writers)
    try:
        for w in writers[k:] + writers[:k]:
            try:
                take_turn(key, cfg, d, state, w, [n for n in names if n != w["name"]],
                          r, total, bible, budget)
            except BudgetExceeded:
                raise
            except Exception as e:
                if "HTTP 402" in str(e):
                    print("  OpenRouter is out of credits (HTTP 402). Stopping the round.")
                    raise BudgetExceeded()
                print(f"  {w['name']}: FAILED ({e})")
                append(d / "thread.md", f"\n### Round {r} — {w['name']}\n\n_(missed this turn: {str(e)[:200]})_\n")
            save_state(d, state)
        state["status"] = "awaiting author review"
    except BudgetExceeded:
        state["status"] = "paused: budget reached"
    if not no_advance:
        state["rounds_done"] = r
    save_state(d, state)
    votes = state.get("votes", {})
    new_q = [q for q in load_questions(d) if q["id"] not in before]
    print("REPORT " + json.dumps({"task": d.name, "round": r, "phase": phase, "status": state["status"],
                                  "spent_round": round(state["spent_this_run"], 4),
                                  "spent_total": round(state.get("spent_total", 0), 4),
                                  "votes": {n: votes.get(n, {}).get("done") for n in names},
                                  "new_questions": new_q}))


def cmd_moderate(d: Path, text: str) -> None:
    append(d / "thread.md", f"\n### MODERATOR ({now()})\n\n{text.strip()}\n")
    print("Moderator note posted.")


def cmd_answer(d: Path, path: str) -> None:
    """Deliver author answers. File: [{"id": "q1", "answer": "...", "comment": "..."}]"""
    answers = json.loads(Path(path).read_text(encoding="utf-8"))
    qs = {q["id"]: q for q in load_questions(d)}
    lines = []
    for a in answers:
        q = qs.get(a["id"])
        if not q:
            continue
        q.update(status="answered", answer=a.get("answer", ""), comment=a.get("comment", ""), answered=now())
        bits = [b for b in (a.get("answer"), a.get("comment")) if b]
        lines.append(f"- **[{q['id']}] {q['from']} asked:** {q['question']}\n  **Author:** {' — '.join(bits) or '(no answer)'}")
    save_questions(d, list(qs.values()))
    append(d / "thread.md", f"\n### AUTHOR ANSWERS ({now()})\n\nThese are rulings. Apply them.\n\n" + "\n".join(lines) + "\n")
    print(f"Delivered {len(lines)} answers.")


def cmd_finalize(d: Path) -> None:
    cfg, key = load_config(), api_key()
    names = [w["name"] for w in cfg["writers"]]
    fin_name = cfg.get("finalizer") if cfg.get("finalizer") in names else names[0]
    fin = next(w for w in cfg["writers"] if w["name"] == fin_name)
    state = load_state(d)
    state["spent_this_run"] = 0.0
    r = state.get("rounds_done", 0)
    take_turn(key, cfg, d, state, fin, [n for n in names if n != fin_name], r, r, build_bible(cfg),
              cfg.get("budget_usd_per_run", 3.0), finalizer=True)
    state["status"] = "final draft ready for author"
    save_state(d, state)
    print(f"Final written by {fin_name}: {d / 'final.md'}")


def cmd_note(d: Path, text: str) -> None:
    append(d / "thread.md", f"\n### AUTHOR NOTE ({now()})\n\n{text.strip()}\n")
    print("Note added. Run the room again to have the writers act on it.")


def cmd_status(task: str | None) -> None:
    if task:
        d = task_dir(task)
        s = load_state(d)
        print(json.dumps({k: v for k, v in s.items()}, indent=2))
        q = (d / "questions_for_author.md").read_text(encoding="utf-8").strip().splitlines()[1:]
        print(f"\nOpen questions: {sum(1 for x in q if x.startswith('- '))}")
        return
    if not TASKS.exists():
        print("No tasks yet.")
        return
    for d in sorted(TASKS.iterdir()):
        if (d / "state.json").exists():
            s = load_state(d)
            print(f"{d.name:55} {s.get('status', ''):32} rounds {s.get('rounds_done', 0):2}  ${s.get('spent_total', 0):.3f}")


def cmd_ping() -> None:
    cfg, key = load_config(), api_key()
    for w in cfg["writers"]:
        try:
            r = call_model(key, {**w, "max_tokens": 400}, [{"role": "user", "content":
                "Writers' room roll call. Reply with one line: your name is " + w["name"] + "."}], cfg, tools=False)
            txt = (r["choices"][0]["message"].get("content") or "").strip().replace("\n", " ")
            print(f"OK   {w['name']:7} {w['model']:28} {txt[:90]}")
        except Exception as e:
            print(f"FAIL {w['name']:7} {w['model']:28} {e}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Eurobound Writing Room")
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("go"); g.add_argument("brief"); g.add_argument("--title")
    g.add_argument("--rounds", type=int); g.add_argument("--budget", type=float); g.add_argument("--writers")
    n = sub.add_parser("new"); n.add_argument("title"); n.add_argument("--brief"); n.add_argument("--brief-file")
    r = sub.add_parser("run"); r.add_argument("task"); r.add_argument("--rounds", type=int)
    r.add_argument("--budget", type=float); r.add_argument("--writers")
    o = sub.add_parser("note"); o.add_argument("task"); o.add_argument("text")
    s = sub.add_parser("status"); s.add_argument("task", nargs="?")
    sub.add_parser("ping")
    rd = sub.add_parser("round"); rd.add_argument("task")
    rd.add_argument("--phase", choices=list(PHASES), required=True)
    rd.add_argument("--budget", type=float); rd.add_argument("--writers")
    rd.add_argument("--no-advance", action="store_true", help="single-writer turn; don't close the round")
    md = sub.add_parser("moderate"); md.add_argument("task"); md.add_argument("text")
    an = sub.add_parser("answer"); an.add_argument("task"); an.add_argument("file")
    fz = sub.add_parser("finalize"); fz.add_argument("task")
    qq = sub.add_parser("questions"); qq.add_argument("task")
    a = ap.parse_args()

    def split(x):
        return [y.strip() for y in x.split(",")] if x else None

    if a.cmd == "go":
        d = cmd_new(a.title or a.brief[:60], a.brief)
        cmd_run(d, a.rounds, a.budget, split(a.writers))
    elif a.cmd == "new":
        brief = Path(a.brief_file).read_text(encoding="utf-8") if a.brief_file else (a.brief or "")
        if not brief.strip():
            sys.exit("Give --brief or --brief-file")
        cmd_new(a.title, brief)
    elif a.cmd == "run":
        cmd_run(task_dir(a.task), a.rounds, a.budget, split(a.writers))
    elif a.cmd == "note":
        cmd_note(task_dir(a.task), a.text)
    elif a.cmd == "status":
        cmd_status(a.task)
    elif a.cmd == "ping":
        cmd_ping()
    elif a.cmd == "round":
        cmd_round(task_dir(a.task), a.phase, a.budget, split(a.writers), a.no_advance)
    elif a.cmd == "moderate":
        cmd_moderate(task_dir(a.task), a.text)
    elif a.cmd == "answer":
        cmd_answer(task_dir(a.task), a.file)
    elif a.cmd == "finalize":
        cmd_finalize(task_dir(a.task))
    elif a.cmd == "questions":
        print(json.dumps([q for q in load_questions(task_dir(a.task)) if q["status"] == "open"], indent=2))


if __name__ == "__main__":
    main()
