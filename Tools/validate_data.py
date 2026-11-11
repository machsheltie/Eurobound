"""Validates the engine data under game/assets/data.

Every *.json file is parsed. Files the engine reads (DataRepo, the arcade scripts) or that
carry an author-ruled schema get required-key and cross-reference checks taken from those
loaders and rulings; nothing here invents a schema. Files that are intentionally empty until
the author rules their schema (bead Eurobound-70z) report PENDING, not FAIL. Everything else
is parse-checked only and reports PARSED.

Usage: python -I tools/validate_data.py      (exit 0 = no FAIL lines)
Tests: python -I -m unittest discover -s tools/tests
"""
import json
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "game" / "assets" / "data"

BROS = ("lord_pilsner", "chadwick", "bradley")

# Empty collections awaiting an author schema ruling (Eurobound-70z): file -> collection keys.
PENDING_SCHEMA = {
    "items/equipment.json": ["equipment"],
    "skills/status_effects.json": ["status_effects"],
    "world_data/Shops.json": ["shops"],
    "world_data/Maps.json": ["maps"],
    "world_data/quest_flags.json": ["quest_flags"],
    "npcs/dialogue_trees/shared_responses.json": ["shared_responses"],
    "npcs/sprite_mappings/bartender_variants.json": ["sprite_sheets"],
    "npcs/sprite_mappings/bouncer_variants.json": ["sprite_sheets"],
    "npcs/sprite_mappings/tourist_archetypes.json": ["sprite_sheets"],
    "enemies/publandia_enemies.json": ["enemies"],
    "enemies/sinfonia_enemies.json": ["enemies"],
    "npcs/base_profiles/publandia_core.json": ["npcs"],
    "npcs/base_profiles/sinfonia_core.json": ["npcs"],
    "npcs/dialogue_trees/publandia_dialogue.json": ["dialogue_trees", "status_reactions", "world_state_responses"],
    "npcs/dialogue_trees/sinfonia_dialogue.json": ["dialogue_trees", "status_reactions", "world_state_responses"],
}

# Fields each loader reads per entry.
PARTY_FIELDS = ["display_name", "max_hp", "max_bravado", "offense", "defense", "speed",
                "luck", "grit", "charm", "skills"]                       # BattleUnit.from_member
ENEMY_FIELDS = ["display_name", "max_hp", "offense", "defense", "speed", "luck",
                "xp_reward", "item_drop", "drop_chance"]                  # BattleUnit.from_enemy
CONSUMABLE_FIELDS = ["display_name", "heal_hp", "heal_bravado", "description"]  # battle_core use_item
ABILITY_FIELDS = ["display_name", "bravado_cost"]                         # battle_core skills
KEY_ITEM_FIELDS = ["display_name", "item_class", "source", "description"]  # ruling 2026-08-06
KEY_ITEM_CLASSES = {"permanent", "curse", "quest"}
# Inventory ids that are currencies, not items: ArcadeRules.TOKEN_ID and ArcadeRules.TICKET_ID
# (game/worlds/debaucheryville/absinthe_arcade/arcade_rules.gd). A villain dropping one just
# hands the bros that currency, so item_drop may name them without an item entry.
CURRENCY_IDS = {"item_absinthe_arcade_token", "arcade_tickets"}
PRIZE_COUNTER_SOURCES = {"absinthe_arcade_prize_redemption",
                         "absinthe_arcade_prize_redemption_junk_shelf"}   # prize_shop.gd
LOCATION_FIELDS = ["location_id", "display_name", "location_type"]
# Canonical quest schema: docs/superpowers/specs/2026-08-06-quest-creation-skill-design.md
QUEST_FIELDS = ["quest_id", "display_name", "satirical_subtitle", "city", "location", "quest_type",
                "recommended_level", "estimated_duration_minutes", "quest_giver", "prerequisites",
                "satirical_targets", "quest_stages", "npcs", "rewards", "quest_flags",
                "post_credits_scene", "npc_callbacks", "easter_eggs", "validation_checklist",
                "items_acquired", "localization", "presentation"]
QUEST_LEGACY_KEYS = ["mobile_optimization", "localization_notes", "items"]
QUEST_ITEM_PATHS = {"standard", "path_a", "path_b"}


@dataclass
class Result:
    status: str  # OK | PARSED | PENDING | FAIL
    rel: str
    msg: str = ""


def _need(errs, obj, keys, where):
    for k in keys:
        if not isinstance(obj, dict) or k not in obj:
            errs.append(f"{where}: missing '{k}'")


def _collection(errs, doc, key, nonempty=True):
    val = doc.get(key) if isinstance(doc, dict) else None
    if not isinstance(val, dict):
        errs.append(f"'{key}' must be an object")
        return {}
    if nonempty and not val:
        errs.append(f"'{key}' is empty")
    return val


def _entries(errs, coll, fields):
    for eid, entry in coll.items():
        _need(errs, entry, fields, eid)


# --- per-file checks: each takes (doc, docs) and returns a list of error strings ---------

def check_party(doc, docs):
    errs = []
    party = _collection(errs, doc, "party_members")
    _entries(errs, party, PARTY_FIELDS)
    abilities = (docs.get("skills/party_abilities.json") or {}).get("abilities", {})
    for bro, m in party.items():
        for skill in (m.get("skills") or []) if isinstance(m, dict) else []:
            if skill not in abilities:
                errs.append(f"{bro}: skill '{skill}' not in skills/party_abilities.json")
    return errs


def check_enemies(doc, docs):
    errs = []
    enemies = _collection(errs, doc, "enemies")
    _entries(errs, enemies, ENEMY_FIELDS)
    items = set((docs.get("items/consumables.json") or {}).get("consumables", {}))
    items |= set((docs.get("items/key_items.json") or {}).get("key_items", {}))
    items |= CURRENCY_IDS
    for eid, e in enemies.items():
        drop = e.get("item_drop") if isinstance(e, dict) else None
        if isinstance(drop, str) and drop and drop not in items:
            errs.append(f"{eid}: item_drop '{drop}' is not defined in consumables or key_items")
    return errs


def check_arcade_battle(doc, docs):
    errs = []
    villains = _collection(errs, doc, "villains")
    cabinets = _collection(errs, doc, "cabinets")
    engine = (docs.get("enemies/debaucheryville_enemies.json") or {}).get("enemies", {})
    for vid, v in villains.items():
        _need(errs, v, ["moves"], vid)
        if vid not in engine:
            errs.append(f"{vid}: villain has no engine stats in debaucheryville_enemies.json")
    for cid, c in cabinets.items():
        _need(errs, c, ["structure", "backdrop"], cid)
        if not isinstance(c, dict):
            continue
        if c.get("structure") == "ladder":
            groups, need = c.get("rungs"), ["enemies"]
            label = "rungs"
        else:
            groups, need = c.get("releases"), ["enemies", "weight"]
            label = "releases"
        if not isinstance(groups, list) or not groups:
            errs.append(f"{cid}: missing or empty '{label}'")
            continue
        for i, g in enumerate(groups):
            _need(errs, g, need, f"{cid}.{label}[{i}]")
            for eid in (g.get("enemies") or []) if isinstance(g, dict) else []:
                if eid not in villains:
                    errs.append(f"{cid}.{label}[{i}]: '{eid}' is not a villain")
    return errs


def check_consumables(doc, docs):
    errs = []
    _entries(errs, _collection(errs, doc, "consumables"), CONSUMABLE_FIELDS)
    return errs


def check_abilities(doc, docs):
    errs = []
    _entries(errs, _collection(errs, doc, "abilities"), ABILITY_FIELDS)
    return errs


def check_key_items(doc, docs):
    errs = []
    items = _collection(errs, doc, "key_items")
    _entries(errs, items, KEY_ITEM_FIELDS)
    for iid, it in items.items():
        if not isinstance(it, dict):
            continue
        if "item_class" in it and it["item_class"] not in KEY_ITEM_CLASSES:
            errs.append(f"{iid}: item_class '{it['item_class']}' not one of {sorted(KEY_ITEM_CLASSES)}")
        if iid.startswith("aa_prize_") and "effect" not in it:
            errs.append(f"{iid}: Absinthe Arcade prize missing 'effect' (ruling 2026-11-09)")
        if it.get("source") in PRIZE_COUNTER_SOURCES and not isinstance(it.get("ticket_price"), int):
            errs.append(f"{iid}: prize-counter item needs an integer 'ticket_price'")
    return errs


def check_dialogue(doc, docs):
    errs = []
    trees = _collection(errs, doc, "dialogue_trees")
    _need(errs, trees, ["vlad_validator"], "dialogue_trees")
    _need(errs, trees.get("vlad_validator"), ["default_greeting"], "vlad_validator")
    return errs


def check_npc_profiles(doc, docs):
    errs = []
    _collection(errs, doc, "npcs")
    return errs


def check_location_list(doc, docs):
    if not isinstance(doc, list):
        return ["top level must be a list of locations (deliberately a list, not an object)"]
    errs, seen = [], set()
    for i, loc in enumerate(doc):
        _need(errs, loc, LOCATION_FIELDS, f"[{i}]")
        lid = loc.get("location_id") if isinstance(loc, dict) else None
        if lid in seen:
            errs.append(f"[{i}]: duplicate location_id '{lid}'")
        seen.add(lid)
    return errs


def check_location_nodes(doc, docs):
    if not isinstance(doc, dict) or not isinstance(doc.get("locations"), list):
        return ["'locations' must be a list"]
    return []


def check_locations_dict(doc, docs):
    errs = []
    _collection(errs, doc, "locations")
    return errs


def check_microcopy(doc, docs):
    errs = []
    ta = doc.get("token_attendant") if isinstance(doc, dict) else None
    _need(errs, ta, ["mutters", "late_night_after_0100"], "token_attendant")
    if isinstance(ta, dict):
        if not isinstance(ta.get("mutters"), dict):
            errs.append("token_attendant.mutters must be an object of line lists")
        if not isinstance(ta.get("late_night_after_0100"), list):
            errs.append("token_attendant.late_night_after_0100 must be a list")
    ddr = doc.get("ddr_expert") if isinstance(doc, dict) else None
    for moment in ("difficulty_bounce", "failed_expert_song"):
        lines = ddr.get(moment) if isinstance(ddr, dict) else None
        if not isinstance(lines, dict):
            errs.append(f"ddr_expert.{moment} must be an object keyed by bro")
            continue
        for bro in BROS:
            if not isinstance(lines.get(bro), list) or not lines[bro]:
                errs.append(f"ddr_expert.{moment}: missing lines for '{bro}'")
    return errs


def check_quest(doc, docs):
    if not isinstance(doc, dict):
        return ["quest must be an object"]
    errs = []
    _need(errs, doc, QUEST_FIELDS, "quest")
    for k in QUEST_LEGACY_KEYS:
        if k in doc:
            errs.append(f"legacy key '{k}' present (canonical schema renames it)")
    ia = doc.get("items_acquired")
    if isinstance(ia, dict):
        bad = set(ia) - QUEST_ITEM_PATHS
        if bad or not ia:
            errs.append(f"items_acquired must be sub-keyed {sorted(QUEST_ITEM_PATHS)}, got {sorted(ia)}")
    elif "items_acquired" in doc:
        errs.append("items_acquired must be an object")
    return errs


CHECKS = {
    "party/party_members.json": check_party,
    "enemies/debaucheryville_enemies.json": check_enemies,
    "enemies/debaucheryville_arcade_battle.json": check_arcade_battle,
    "items/consumables.json": check_consumables,
    "items/key_items.json": check_key_items,
    "skills/party_abilities.json": check_abilities,
    "npcs/dialogue_trees/debaucheryville_dialogue.json": check_dialogue,
    "npcs/base_profiles/debaucheryville_core.json": check_npc_profiles,
    "locations/debaucheryville/debaucheryville_locations.json": check_location_list,
    "locations/debaucheryville/debaucheryville_locations_core.json": check_location_list,
    "locations/location_nodes_debaucheryville.json": check_location_nodes,
    "locations/debaucheryville/debaucheryville_environmental.json": check_locations_dict,
    "locations/debaucheryville/debaucheryville_interactions.json": check_locations_dict,
    "locations/debaucheryville/debaucheryville_sprite_mapping.json": check_locations_dict,
    "locations/debaucheryville/absinthe_arcade_microcopy.json": check_microcopy,
}

# Files the engine cannot run without (DataRepo.load_all / arcade scripts).
REQUIRED_FILES = [
    "party/party_members.json", "enemies/debaucheryville_enemies.json",
    "enemies/debaucheryville_arcade_battle.json", "items/consumables.json",
    "items/key_items.json", "items/equipment.json", "skills/party_abilities.json",
    "npcs/dialogue_trees/debaucheryville_dialogue.json",
    "locations/debaucheryville/absinthe_arcade_microcopy.json",
]


def _check_for(rel):
    if rel in CHECKS:
        return CHECKS[rel]
    if rel.startswith("quests/"):
        return check_quest
    return None


def validate(root=ROOT):
    root = Path(root)
    docs, results = {}, []
    files = sorted(p.relative_to(root).as_posix() for p in root.rglob("*.json"))
    for rel in REQUIRED_FILES:
        if rel not in files:
            results.append(Result("FAIL", rel, "missing (the engine loads this file)"))
    for rel in files:
        try:
            docs[rel] = json.loads((root / rel).read_text(encoding="utf-8-sig"))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            docs[rel] = None
            results.append(Result("FAIL", rel, f"invalid JSON: {e}"))
    for rel in files:
        doc = docs[rel]
        if doc is None:
            continue
        if rel in PENDING_SCHEMA:
            errs = []
            colls = [_collection(errs, doc, k, nonempty=False) for k in PENDING_SCHEMA[rel]]
            if errs:
                results.extend(Result("FAIL", rel, e) for e in errs)
            elif any(colls):
                results.append(Result("PARSED", rel, "has entries but no ruled schema (Eurobound-70z)"))
            else:
                results.append(Result("PENDING", rel, "pending schema (Eurobound-70z)"))
            continue
        check = _check_for(rel)
        if check is None:
            results.append(Result("PARSED", rel, "parse only (no loader reads it yet)"))
            continue
        errs = check(doc, docs)
        if errs:
            results.extend(Result("FAIL", rel, e) for e in errs)
        else:
            results.append(Result("OK", rel))
    return results


def main(root=ROOT):
    results = validate(root)
    for r in results:
        print(f"{r.status:<8} {r.rel}" + (f": {r.msg}" if r.msg else ""))
    counts = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    print("SUMMARY  " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    return 1 if counts.get("FAIL") else 0


if __name__ == "__main__":
    sys.exit(main())
