"""Prints per-shot score deltas across rounds. Usage: python -I summarize.py [results_dir]
Log format: results/<scene>/round_<n>.jsonl, one JSON object per line:
  {"shot_id": str, "score": 1-10, "worst": [str, str, str], "verdict": "pass"|"fix"}"""
import json
import sys
from pathlib import Path

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
for scene in sorted(p for p in root.iterdir() if p.is_dir()):
    rounds = {}
    for f in scene.glob("round_*.jsonl"):
        rows = [json.loads(x) for x in f.read_text().splitlines() if x.strip()]
        rounds[int(f.stem.split("_")[1])] = {j["shot_id"]: j["score"] for j in rows}
    ns = sorted(rounds)
    print(f"== {scene.name}: rounds {ns}")
    for sid in sorted({s for r in rounds.values() for s in r}):
        sc = [rounds[n].get(sid) for n in ns]
        d = [b - a for a, b in zip(sc, sc[1:]) if a is not None and b is not None]
        last = sc[-1]
        print(f"  {sid:28} {' -> '.join('-' if x is None else str(x) for x in sc)}  delta {sum(d):+d}  {'PASS' if last and last >= 7 else 'FIX'}")
