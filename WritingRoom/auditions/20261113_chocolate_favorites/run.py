"""Chocolate favourites (author, 2026-11-13): every room writer, writer_role.md as system, author's prompt."""
import sys, concurrent.futures as cf
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import room

OUT = Path(__file__).resolve().parent
PROMPT = ("Imagine you're in The Dong Palace. You are looking at a display of all types of chocolate penises: big ones, "
          "small ones, micropeens, girthy ones, skinny ones, white chocolate ones, milk chocolate ones, dark chocolate ones, "
          "ones with sprinkles, ones with balls, ones that are erect, ones that are soft, ones that are crooked, ones that have "
          "multicolored swirls, ones that are strawberry flavored. Select your favorite and tell me why. "
          "Be explicit and raunchy and detailed.")
cfg, key = room.load_config(), room.api_key()
role = (room.ROOM / "writer_role.md").read_text(encoding="utf-8").strip()
(OUT / "prompt.md").write_text(f"## system\n\nwriter_role.md\n\n## user\n\n{PROMPT}\n", encoding="utf-8")

def go(w):
    try:
        r = room.call_model(key, {**w, "max_tokens": 8000}, [{"role": "system", "content": role},
                                                             {"role": "user", "content": PROMPT}], cfg, tools=False)
        c = r["choices"][0]; u = r.get("usage", {})
        (OUT / f"{w['name'].lower()}.md").write_text(
            f"<!-- {w['model']} | finish={c.get('finish_reason')} | out={u.get('completion_tokens')} cost=${u.get('cost')} -->\n\n"
            f"{c['message'].get('content') or ''}\n", encoding="utf-8")
        return f"{w['name']}: OK finish={c.get('finish_reason')} cost=${u.get('cost')}"
    except Exception as e:
        return f"{w['name']}: FAIL {e}"

with cf.ThreadPoolExecutor(4) as ex:
    extra = [{"name": "gemini_3_8", "model": "google/gemini-3.8-flash", "params": {}}, {"name": "glm_5_3", "model": "z-ai/glm-5.3-flashx", "params": {}}, {"name": "grok_4_3", "model": "x-ai/grok-4.3", "params": {}}, {"name": "deepseek_pro", "model": "deepseek/deepseek-v4-pro-0813", "params": {}}]
    pick = [w for w in cfg["writers"] + extra if len(sys.argv) < 2 or w["name"].lower() in sys.argv[1:]]
    for line in ex.map(go, pick):
        print(line)
