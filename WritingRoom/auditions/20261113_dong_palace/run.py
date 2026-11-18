"""Dong Palace audition (author, 2026-11-13): same prompt to Dolphin Mistral and DeepSeek via OpenRouter."""
import json, sys, concurrent.futures as cf
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import room

OUT = Path(__file__).resolve().parent
REPO = room.REPO
FILES = ["design/worlds/shamsterdam/the_dong_palace.md",
         "design/narrative/Synopsis.md",
         "design/characters/bros_core_principle.md",
         "design/narrative/bros_choose_debauchery.md",
         "design/characters/LordPilsner/lordpilsner.md",
         "design/characters/Chadwick/chadwick.md",
         "design/characters/Bradley/bradley.md"]
role = (room.ROOM / "writer_role.md").read_text(encoding="utf-8").strip()
docs = "\n\n".join(f"# FILE: {f}\n\n{(REPO / f).read_text(encoding='utf-8', errors='replace')}" for f in FILES)
task = ("Read The Dong Palace document and the bros' files above. Then come up with a subversive conversation "
        "between the bros (Lord Pilsner, Chadwick and Bradley) that pertains to or takes place in The Dong Palace. "
        "Write it as a game dialogue script.")
msgs = [{"role": "system", "content": role},
        {"role": "user", "content": docs + "\n\n---\n\n" + task}]
ALL = [{"name": "dolphin", "model": "cognitivecomputations/dolphin-mistral-24b-venice-edition", "max_tokens": 6000, "params": {}},
       {"name": "deepseek", "model": "deepseek/deepseek-v4.1-flash-1017", "max_tokens": 16000, "params": {}},
       {"name": "mistral_large_4", "model": "mistralai/mistral-large-4-0", "max_tokens": 16000, "params": {}},
       {"name": "grok_4_3", "model": "x-ai/grok-4.3", "max_tokens": 16000, "params": {}},
       {"name": "deepseek_directive", "model": "deepseek/deepseek-v4.1-flash-1017", "max_tokens": 16000, "params": {}},  
       {"name": "gemini_3_8", "model": "google/gemini-3.8-flash", "max_tokens": 16000, "params": {}},
       {"name": "glm_5_3", "model": "z-ai/glm-5.3-flashx", "max_tokens": 32000, "params": {}},
       {"name": "deepseek_pro", "model": "deepseek/deepseek-v4-pro-0813", "max_tokens": 16000, "params": {}}]
# python run.py [name ...] runs only those; no names runs all
WRITERS = [w for w in ALL if len(sys.argv) < 2 or w["name"] in sys.argv[1:]]
cfg, key = room.load_config(), room.api_key()

def go(w):
    try:
        m = msgs
        if w.get("addendum"):  # same prompt, with the writer's own directive after the role (as the room sends it)
            add = (room.ROOM / w["addendum"]).read_text(encoding="utf-8").strip()
            m = [{"role": "system", "content": role + chr(10) * 2 + add}] + msgs[1:]
        r = room.call_model(key, {k: v for k, v in w.items() if k != "addendum"}, m, cfg, tools=False)
        c = r["choices"][0]; u = r.get("usage", {})
        text = c["message"].get("content") or ""
        (OUT / f"{w['name']}.md").write_text(f"<!-- {w['model']} | finish={c.get('finish_reason')} | in={u.get('prompt_tokens')} out={u.get('completion_tokens')} cost=${u.get('cost')} -->\n\n{text}\n", encoding="utf-8")
        return f"{w['name']}: OK finish={c.get('finish_reason')} in={u.get('prompt_tokens')} out={u.get('completion_tokens')} cost=${u.get('cost')}"
    except Exception as e:
        return f"{w['name']}: FAIL {e}"

(OUT / "prompt.md").write_text(f"## system\n\n{role}\n\n## user (files: {', '.join(FILES)})\n\n{task}\n", encoding="utf-8")
with cf.ThreadPoolExecutor(len(WRITERS) or 1) as ex:
    for line in ex.map(go, WRITERS):
        print(line)
