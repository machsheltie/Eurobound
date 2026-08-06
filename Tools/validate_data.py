"""Validates that every JSON file the vertical slice needs parses and has required keys."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "game" / "assets" / "data"

REQUIRED = {
    "party/party_members.json": ["party_members", "party_members.lord_pilsner",
        "party_members.lord_pilsner.max_hp", "party_members.lord_pilsner.offense"],
    "enemies/debaucheryville_enemies.json": ["enemies", "enemies.feral_segway_tourist",
        "enemies.feral_segway_tourist.max_hp", "enemies.feral_segway_tourist.xp_reward"],
    "items/consumables.json": ["consumables", "consumables.lukewarm_kebab"],
    "skills/party_abilities.json": ["abilities", "abilities.roast_line",
        "abilities.roast_line.bravado_cost"],
    "npcs/dialogue_trees/debaucheryville_dialogue.json": ["dialogue_trees",
        "dialogue_trees.vlad_validator", "dialogue_trees.vlad_validator.default_greeting"],
    "npcs/base_profiles/debaucheryville_core.json": ["npcs"],
    "locations/debaucheryville/debaucheryville_locations.json": [],
}

def dig(obj, dotted):
    for part in dotted.split("."):
        if not isinstance(obj, dict) or part not in obj:
            return None
        obj = obj[part]
    return obj

failures = 0
for rel, keys in REQUIRED.items():
    path = ROOT / rel
    if not path.exists():
        print(f"MISSING  {rel}"); failures += 1; continue
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as e:
        print(f"INVALID  {rel}: {e}"); failures += 1; continue
    missing = [key for key in keys if dig(data, key) is None]
    for key in missing:
        print(f"NOKEY    {rel}: missing '{key}'"); failures += 1
    if not missing:
        print(f"OK       {rel}")
sys.exit(1 if failures else 0)
