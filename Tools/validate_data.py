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
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "game" / "assets" / "data"

BROS = ("lord_pilsner", "chadwick", "bradley")

# Empty collections awaiting an author schema ruling (Eurobound-70z): file -> collection keys.
PENDING_SCHEMA = {
    "items/equipment.json": ["equipment"],
    "world_data/Shops.json": ["shops"],
    "world_data/Maps.json": ["maps"],
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
# Optional consumable fields, author ruling 2026-11-12 (Production Desk Eurobound-sue-q1, "Approve
# as proposed"): docs/superpowers/specs/2026-11-12-consumable-intoxicant-fields-proposal.md §2.
# A null value marks a field no ruling has set yet; each one needs a note under `_pending` keyed
# by its dotted path, and every `_pending` note must point at a null.
CONSUMABLE_SUBTYPES = {"food", "drink", "vape", "drug", "coupon", "junk"}
CONSUMABLE_USABLE_IN = {"battle", "field"}
INTOX_STACK_RULES = {"extend", "refresh", "none"}
PENDING_PATHS = {"usable_in", "max_stack", "price.amount", "intoxicant.duration.battle_turns",
                 "intoxicant.duration.field_steps", "intoxicant.duration.ends_on_rest"}
MASTER_POOL = Path(__file__).resolve().parent.parent / "design" / "economy" / "shitcoin_master_pool.md"
_POOL_ROW = re.compile(r"^\|\s*\d+\s*\|[^|]*\|\s*\$(\w+)\s*\|")
_SNAKE = re.compile(r"^[a-z][a-z0-9_]*$")
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
# Quest flag registry, tier 2 (schema check). Author ruling 2026-11-12 (Production Desk
# Eurobound-vyn-q1, "Approve as proposed"): docs/superpowers/specs/2026-11-12-quest-flag-schema-proposal.md
# §3 (category), §4 (file shape, entry fields, id rule), §6 (tier 2). Tier 3 (the cross-reference
# against game code and quest data, Eurobound-pjas) is check_flag_xref below.
REPO_ROOT = Path(__file__).resolve().parent.parent
QUEST_FLAGS_FILE = "world_data/quest_flags.json"
FLAG_FIELDS = ["type", "default", "category", "write_once", "set_by", "read_by", "doc", "status"]
# "float" (Eurobound-0jfv): field_step_carry stores a fractional metre, which no §4.2 type held.
FLAG_TYPES = {"bool": (bool,), "int": (int,), "float": (float,), "string": (str,), "array": (list,),
              "dict": (dict,)}
FLAG_CATEGORIES = {"quest", "world", "economy", "system", "setting"}
FLAG_STATUSES = {"ruled", "proposed"}
FLAG_DOC_NONE = "NONE: code only"
_FLAG_ID = re.compile(r"^[a-z0-9_]+(\.[a-z0-9_]+){2}$")  # <city>.<venue>.<event> / <quest>.<city>.<event>
_PLACEHOLDER = re.compile(r"\{[a-z_][a-z0-9_]*\}")
_DOC_REF = re.compile(r"^(.+):(\d+)$")
# Status-effect entry shape. Author ruling 2026-11-12 (Production Desk Eurobound-1m4-q1, "Approve
# as proposed"): docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md §3. Only
# display_name is required; an absent field means "this status does not do that". A null marks a
# value no ruling has set yet and needs a `_pending` note at its dotted path or an ancestor's.
# The full status schema (and migrating the hard-coded statuses) is still Eurobound-70z.
STATUS_FILE = "skills/status_effects.json"
STATUS_SCHEMA_VERSION = "1.0"
STATUS_FIELDS = {"display_name", "section", "scope", "bearer", "default_duration", "stack_rule",
                 "stats", "accuracy_steps", "skip_turn_chance", "damage_out_mult", "bravado_tick",
                 "attack_conversion", "locks", "field", "on_rest", "ladder", "interactions",
                 "cured_by", "then", "cues", "_pending"}
STATUS_SECTIONS = {"positive", "negative", "neutral", "combo"}
STATUS_SCOPES = {"battle", "field"}
STATUS_BEARERS = {"bro", "enemy", "any"}
STATUS_STACK_RULES = {"extend", "refresh", "intensify", "none"}
STATUS_STATS = {"offense", "defense", "speed", "luck", "grit", "charm", "max_hp", "max_bravado",
                "all"}                            # engine stat names (battle_unit.gd) + "all"
STATUS_DURATION_KEYS = {"battle_turns", "field_steps", "ends_on_rest", "until_cured"}
STATUS_TICK_KEYS = {"battle_per_turn", "field_amount", "field_every_steps"}
STATUS_CONVERSIONS = {"cleaning", "pacification"}
STATUS_LOCKS = {"bravado_cost_skills", "spoken_bravado_skills"}
STATUS_FIELD_KEYS = {"compulsion", "text_speed_mult", "text_filter", "choices"}
STATUS_COMPULSIONS = {"clean_nearest_interactable", "stare"}
STATUS_COMPULSION_UNITS = {"steps", "real_seconds"}
STATUS_TEXT_FILTERS = {"trailing_ellipsis"}
STATUS_CHOICE_MODES = {"shuffle", "replace"}
STATUS_LADDER_KEYS = {"display_offset", "gain_bonus"}
STATUS_INTERACTION_RULES = {"suppress", "cancel_into", "modify_then", "unaffected"}
STATUS_CURE_KINDS = {"rest", "item_subtype", "item_id"}
STATUS_CUE_KEYS = {"icon", "idle_anim", "particle"}


@dataclass
class Result:
    status: str  # OK | PARSED | PENDING | WARN | FAIL
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


def master_pool_coins(path=MASTER_POOL):
    """Lower-case tickers from the Coin Index table of the shitcoin master pool, or None."""
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except OSError:
        return None
    return {m.group(1).lower() for line in text.splitlines() if (m := _POOL_ROW.match(line))}


def _is_int(v, minimum):
    return isinstance(v, int) and not isinstance(v, bool) and v >= minimum


def _get_path(entry, dotted):
    cur = entry
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return False, None
        cur = cur[part]
    return True, cur


def _check_consumable_extras(iid, it, coins, statuses):
    """Type and enum checks for the optional fields ruled 2026-11-12 (Eurobound-sue)."""
    errs = []
    if "subtype" in it and it["subtype"] not in CONSUMABLE_SUBTYPES:
        errs.append(f"{iid}: subtype '{it['subtype']}' not one of {sorted(CONSUMABLE_SUBTYPES)}")
    if it.get("usable_in") is not None:
        ui = it["usable_in"]
        if not isinstance(ui, list) or not ui or any(u not in CONSUMABLE_USABLE_IN for u in ui):
            errs.append(f"{iid}: usable_in must be a non-empty list from {sorted(CONSUMABLE_USABLE_IN)}")
    if it.get("max_stack") is not None and not _is_int(it["max_stack"], 1):
        errs.append(f"{iid}: max_stack must be an int >= 1")

    price = it.get("price")
    if "price" in it:
        if not isinstance(price, dict) or "coin" not in price or "amount" not in price:
            errs.append(f"{iid}: price must be an object {{coin, amount}}")
            price = None
        else:
            coin = price["coin"]
            if not isinstance(coin, str) or coin != coin.lower():
                errs.append(f"{iid}: price.coin must be a lower-case string ('sovs' or a master-pool ticker)")
            elif coin != "sovs":
                if coins is None:
                    errs.append(f"{iid}: cannot read the master pool to check price.coin '{coin}'")
                elif coin not in coins:
                    errs.append(f"{iid}: price.coin '{coin}' is not 'sovs' or a master-pool ticker")
            if price["amount"] is not None and not _is_int(price["amount"], 0):
                errs.append(f"{iid}: price.amount must be an int >= 0 or null")
    if "bundles" in it:
        b = it["bundles"]
        if price is None:
            errs.append(f"{iid}: bundles need a price object (they are quoted in its coin)")
        if not isinstance(b, list) or not b:
            errs.append(f"{iid}: bundles must be a non-empty list of {{qty, amount}}")
        else:
            for i, tier in enumerate(b):
                if not isinstance(tier, dict) or not _is_int(tier.get("qty"), 2):
                    errs.append(f"{iid}: bundles[{i}].qty must be an int >= 2")
                elif "amount" not in tier or (tier["amount"] is not None and not _is_int(tier["amount"], 0)):
                    errs.append(f"{iid}: bundles[{i}].amount must be an int >= 0 or null (quoted at sale)")

    if "intoxicant" in it:
        ix = it["intoxicant"]
        if not isinstance(ix, dict):
            errs.append(f"{iid}: intoxicant must be an object")
        else:
            st = ix.get("status")
            if not isinstance(st, str) or not _SNAKE.match(st):
                errs.append(f"{iid}: intoxicant.status must be a snake_case status id")
            elif statuses and st not in statuses:
                errs.append(f"{iid}: intoxicant.status '{st}' not in skills/status_effects.json")
            dur = ix.get("duration")
            if not isinstance(dur, dict):
                errs.append(f"{iid}: intoxicant.duration must be an object {{battle_turns, field_steps, ends_on_rest}}")
            else:
                for k in ("battle_turns", "field_steps"):
                    if k not in dur:
                        errs.append(f"{iid}: intoxicant.duration missing '{k}'")
                    elif dur[k] is not None and not _is_int(dur[k], 1):
                        errs.append(f"{iid}: intoxicant.duration.{k} must be an int >= 1 or null")
                if "ends_on_rest" not in dur:
                    errs.append(f"{iid}: intoxicant.duration missing 'ends_on_rest'")
                elif dur["ends_on_rest"] is not None and not isinstance(dur["ends_on_rest"], bool):
                    errs.append(f"{iid}: intoxicant.duration.ends_on_rest must be true, false or null")
            if "stack_rule" in ix and ix["stack_rule"] not in INTOX_STACK_RULES:
                errs.append(f"{iid}: intoxicant.stack_rule '{ix['stack_rule']}' not one of {sorted(INTOX_STACK_RULES)}")
            if "then" in ix:
                then = ix["then"]
                tst = then.get("status") if isinstance(then, dict) else None
                if not isinstance(tst, str) or not _SNAKE.match(tst):
                    errs.append(f"{iid}: intoxicant.then.status must be a snake_case status id")
                elif statuses and tst not in statuses:
                    errs.append(f"{iid}: intoxicant.then.status '{tst}' not in skills/status_effects.json")
                if not isinstance(then, dict) or not isinstance(then.get("stacks"), bool):
                    errs.append(f"{iid}: intoxicant.then.stacks must be true or false")

    pending = it.get("_pending", {})
    if not isinstance(pending, dict):
        errs.append(f"{iid}: _pending must be an object of dotted path -> note")
        pending = {}
    for path in sorted(PENDING_PATHS):
        present, val = _get_path(it, path)
        if present and val is None and not str(pending.get(path, "")).strip():
            errs.append(f"{iid}: '{path}' is null but has no _pending note citing its doc line")
    for path in pending:
        present, val = _get_path(it, path)
        if path not in PENDING_PATHS:
            errs.append(f"{iid}: _pending note for '{path}', which is not a field that can be pending")
        elif not present or val is not None:
            errs.append(f"{iid}: stale _pending note for '{path}' (the field is not null)")
    return errs


def check_consumables(doc, docs, pool=MASTER_POOL):
    errs = []
    items = _collection(errs, doc, "consumables")
    _entries(errs, items, CONSUMABLE_FIELDS)
    coins = master_pool_coins(pool)
    statuses = set((docs.get("skills/status_effects.json") or {}).get("status_effects", {}) or {})
    for iid, it in items.items():
        if isinstance(it, dict):
            errs.extend(_check_consumable_extras(iid, it, coins, statuses))
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


def _check_flag_entry(fid, entry, repo):
    """§4.2 fields, types and enums for one flag or pattern entry."""
    if not isinstance(entry, dict):
        return [f"{fid}: entry must be an object"]
    errs = []
    _need(errs, entry, FLAG_FIELDS, fid)
    ftype = entry.get("type")
    if "type" in entry and ftype not in FLAG_TYPES:
        errs.append(f"{fid}: type '{ftype}' not one of {sorted(FLAG_TYPES)}")
    elif "default" in entry and ftype in FLAG_TYPES:
        val = entry["default"]
        if not isinstance(val, FLAG_TYPES[ftype]) or (ftype == "int" and isinstance(val, bool)):
            errs.append(f"{fid}: default {json.dumps(val)} does not match type '{ftype}'")
    if "category" in entry and entry["category"] not in FLAG_CATEGORIES:
        errs.append(f"{fid}: category '{entry['category']}' not one of {sorted(FLAG_CATEGORIES)}")
    if "status" in entry and entry["status"] not in FLAG_STATUSES:
        errs.append(f"{fid}: status '{entry['status']}' not one of {sorted(FLAG_STATUSES)}")
    for k in ("write_once", "legacy_id"):
        if k in entry and not isinstance(entry[k], bool):
            errs.append(f"{fid}: {k} must be true or false")
    for k in ("set_by", "read_by"):
        if k in entry and (not isinstance(entry[k], list) or not all(isinstance(s, str) for s in entry[k])):
            errs.append(f"{fid}: {k} must be a list of strings")
    if entry.get("quest_id") is not None and not isinstance(entry["quest_id"], str):
        errs.append(f"{fid}: quest_id must be a string or null")
    if "doc" in entry:
        ref = entry["doc"]
        m = _DOC_REF.match(ref) if isinstance(ref, str) else None
        if ref == FLAG_DOC_NONE:
            pass
        elif not m or int(m.group(2)) < 1:
            errs.append(f"{fid}: doc must be 'path:line' or '{FLAG_DOC_NONE}', got {json.dumps(ref)}")
        elif not (Path(repo) / m.group(1)).is_file():
            errs.append(f"{fid}: doc names a file that does not exist: {m.group(1)}")
    return errs


def check_quest_flags(doc, docs, repo=REPO_ROOT):
    """Tier 2 of the quest flag registry ruling (Eurobound-vyn): see QUEST_FLAGS_FILE above."""
    if not isinstance(doc, dict):
        return ["quest flag registry must be an object"]
    errs = []
    if doc.get("schema_version") != "1.1":
        errs.append(f"schema_version must be \"1.1\", got {json.dumps(doc.get('schema_version'))}")
    flags = _collection(errs, doc, "quest_flags", nonempty=False)
    patterns = _collection(errs, doc, "flag_patterns", nonempty=False)
    for fid, entry in flags.items():
        errs.extend(_check_flag_entry(fid, entry, repo))
        if "{" in fid or "}" in fid:
            errs.append(f"{fid}: a placeholder belongs in flag_patterns, not quest_flags")
        elif not (isinstance(entry, dict) and entry.get("legacy_id") is True) and not _FLAG_ID.match(fid):
            errs.append(f"{fid}: id must be dotted <city>.<venue>.<event> or <quest>.<city>.<event> "
                        "in [a-z0-9_] (or carry \"legacy_id\": true)")
    for pid, entry in patterns.items():
        errs.extend(_check_flag_entry(pid, entry, repo))
        holders = _PLACEHOLDER.findall(pid)
        if len(holders) != 1 or pid.count("{") != 1 or pid.count("}") != 1:
            errs.append(f"{pid}: a pattern must hold exactly one {{placeholder}}")
        elif not (isinstance(entry, dict) and entry.get("legacy_id") is True) \
                and not _FLAG_ID.match(pid.replace(holders[0], "x")):
            errs.append(f"{pid}: id must be dotted <city>.<venue>.<event> or <quest>.<city>.<event> "
                        "in [a-z0-9_] (or carry \"legacy_id\": true)")
    for fid in sorted(set(flags) & set(patterns)):
        errs.append(f"{fid}: declared in both quest_flags and flag_patterns (ids are unique across the file)")
    return errs


# --- quest flag registry, tier 3: cross-reference (Eurobound-pjas) -------------------------
# Approved spec §6 tier 3: collect every flag id the game reads or writes and check it against
# quest_flags.json. FAIL on an undeclared id; WARN on a declared id nothing reads, and on an id
# that is read but has no writer and no "NOT BUILT" note in set_by.
# In scope (FAIL): game/**/*.gd outside tests/ and addons/; quest_log/quest_log.json; quest JSON
# quest_flags blocks; and the engine-data keys a script reads as flag ids (TIER3_CODE_DATA_KEYS).
# Every other flag key in engine data (the write shapes in
# docs/superpowers/specs/2026-11-12-flag-write-shape-proposal.md §1, plus read conditions) is
# design intent no code reads yet: an undeclared id there is a WARN, never a FAIL (the bead keeps
# that data outside tier 3 until the author widens it).
TIER3_REL = "quest_flags tier 3"
QUEST_LOG_FILE = "quest_log/quest_log.json"
QUEST_LOG_READ_KEYS = {"started_when", "completed_when", "done_when", "all", "any"}  # quest_log.gd
# (file, key) -> role, for engine data whose flag ids a script reads at runtime.
TIER3_CODE_DATA_KEYS = {
    ("world_data/events/icqdialogues/icq_hotspot_messages.json", "requires_flags"): "read",   # icq_queue.gd
    ("world_data/events/icqdialogues/icq_hotspot_messages.json", "blocks_flags"): "read",     # icq_queue.gd
    ("enemies/debaucheryville_arcade_battle.json", "defeated_flag"): "write",                # taproom_battle.gd
    ("enemies/debaucheryville_arcade_battle.json", "survived_flag"): "write",                # taproom_battle.gd
    (STATUS_FILE, "flag"): "write",                                    # rest_events.gd (on_rest events)
}
# Every flag key shape found in engine data (write-shape proposal §1 and the read conditions).
DATA_FLAG_WRITE_KEYS = {"set_flags", "set_flag", "sets_flag", "sets_flags", "flag_set", "sets_state",
                        "quest_flags_on_acquire", "set_flags_on_acquire", "status_flag",
                        "defeated_flag", "survived_flag"}
DATA_FLAG_READ_KEYS = {"requires_flags", "blocks_flags", "flags_present", "flags_absent",
                       "requires_flag", "requires_flag_false", "state_not_set"}
# Undeclared ids already in code-side scope when tier 3 landed. Each reports WARN (not FAIL) until
# the bead named here declares it; an entry that is declared or no longer used warns to come out.
# Empty since Eurobound-0jfv declared the five tier 3 found; keep it empty so a regression FAILs.
TIER3_KNOWN_UNDECLARED = {}
_GD_CONST = re.compile(r"^\s*const\s+(\w+)\s*(?::\s*[\w\[\]]+\s*)?:?=\s*(.+)$")
_GD_FUNC = re.compile(r"^(?:static\s+)?func\s+(\w+)\s*\(([^)]*)\)")
_GD_CLASS = re.compile(r"^class_name\s+(\w+)")
_GD_ACCESS = re.compile(r"\bflags\s*(?:\.\s*(get|has|erase)\s*\(|\[)|\b(has_flag|set_flag)\s*\(")
_IDENT = re.compile(r"^[A-Za-z_]\w*$")
_DYN = None  # a segment whose text is only known at runtime


def _strip_gd_comment(line):
    quote = None
    for i, ch in enumerate(line):
        if quote:
            if ch == "\\":
                continue
            if ch == quote and line[i - 1] != "\\":
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#":
            return line[:i]
    return line


def _gd_arg(text, start):
    """The argument text from `start` to the first top-level ',', ')' or ']'."""
    depth, quote = 0, None
    for i in range(start, len(text)):
        ch = text[i]
        if quote:
            if ch == quote and text[i - 1] != "\\":
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch in "([{":
            depth += 1
        elif ch in ")]}":
            if depth == 0:
                return text[start:i]
            depth -= 1
        elif ch == "," and depth == 0:
            return text[start:i]
    return text[start:]


def _gd_args(text, start):
    args, i = [], start
    while i <= len(text):
        a = _gd_arg(text, i)
        args.append(a)
        i += len(a)
        if i >= len(text) or text[i] != ",":
            break
        i += 1
    return [a for a in (x.strip() for x in args) if a]


def _split_plus(expr):
    parts, depth, quote, cur = [], 0, None, ""
    for i, ch in enumerate(expr):
        if quote:
            if ch == quote and expr[i - 1] != "\\":
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        elif ch == "+" and depth == 0:
            parts.append(cur)
            cur = ""
            continue
        cur += ch
    parts.append(cur)
    return [p.strip() for p in parts]


class _GdFile:
    def __init__(self, rel, text):
        self.rel = rel
        self.lines = [_strip_gd_comment(l) for l in text.splitlines()]
        self.consts, self.funcs, self.class_name = {}, {}, None
        cur = None
        for n, line in enumerate(self.lines, 1):
            if line and not line[0].isspace() and line.strip():
                cur = None
            m = _GD_CLASS.match(line)
            if m:
                self.class_name = m.group(1)
            m = _GD_CONST.match(line)
            if m and cur is None:
                self.consts[m.group(1)] = m.group(2).strip()
            m = _GD_FUNC.match(line)
            if m:
                params = [p.split(":")[0].split("=")[0].strip() for p in m.group(2).split(",") if p.strip()]
                cur = {"params": params, "body": [], "line": n}
                self.funcs[m.group(1)] = cur
            elif cur is not None and line.strip():
                cur["body"].append(line.strip())


class _GdIndex:
    def __init__(self, game):
        self.files, self.classes = [], {}
        for p in sorted(Path(game).rglob("*.gd")):
            rel = p.relative_to(game).as_posix()
            if rel.split("/")[0] in ("tests", "addons"):
                continue
            f = _GdFile(rel, p.read_text(encoding="utf-8-sig", errors="replace"))
            self.files.append(f)
            if f.class_name:
                self.classes[f.class_name] = f
        proj = Path(game) / "project.godot"
        if proj.is_file():
            by_res = {"res://" + f.rel: f for f in self.files}
            section = None
            for line in proj.read_text(encoding="utf-8", errors="replace").splitlines():
                if line.startswith("["):
                    section = line.strip()
                elif section == "[autoload]" and "=" in line:
                    name, path = line.split("=", 1)
                    f = by_res.get(path.strip().strip('"').lstrip("*"))
                    if f:
                        self.classes[name.strip()] = f

    def segments(self, expr, f, env=None, depth=0):
        """Resolve a GDScript string expression to segments (str or _DYN), or None if unknown."""
        env = env or {}
        if depth > 10:
            return [_DYN]
        out = []
        for part in _split_plus(expr):
            m = re.fullmatch(r"(?:String|StringName|str)\s*\((.*)\)", part, re.S)
            if m and _gd_arg(m.group(1), 0).strip() == m.group(1).strip():
                part = m.group(1).strip()
            lit = re.fullmatch(r"&?(\"([^\"\\]*)\"|'([^'\\]*)')", part)
            if lit:
                out.append(lit.group(2) if lit.group(2) is not None else lit.group(3))
                continue
            if part in env:
                out.extend(env[part])
                continue
            qual, name, owner = None, part, f
            m = re.fullmatch(r"(\w+)\s*\.\s*(\w+)", part)
            if m and m.group(1) in self.classes:
                qual, name, owner = m.group(1), m.group(2), self.classes[m.group(1)]
            if _IDENT.match(name) and name in owner.consts:
                out.extend(self.segments(owner.consts[name], owner, None, depth + 1))
                continue
            m = re.fullmatch(r"(?:(\w+)\s*\.\s*)?(\w+)\s*\((.*)\)", part, re.S)
            if m and (m.group(1) is None or m.group(1) in self.classes):
                owner = self.classes[m.group(1)] if m.group(1) else f
                fn = owner.funcs.get(m.group(2))
                if fn and len(fn["body"]) == 1 and fn["body"][0].startswith("return "):
                    args = _gd_args(m.group(3), 0)
                    bound = {p: (self.segments(a, f, env, depth + 1) if i < len(args) else [_DYN])
                             for i, (p, a) in enumerate(zip(fn["params"], args + [""] * len(fn["params"])))}
                    out.extend(self.segments(fn["body"][0][7:], owner, bound, depth + 1))
                    continue
            out.append(_DYN)
        merged = []
        for s in out:
            if s is not _DYN and merged and merged[-1] is not _DYN:
                merged[-1] += s
            else:
                merged.append(s)
        return merged


def _as_ref(segs):
    """('id', text) for a literal, ('family', before, after) for one runtime part, else None."""
    if not segs:
        return None
    if all(s is not _DYN for s in segs):
        return ("id", "".join(segs))
    if segs.count(_DYN) == 1 and len(segs) <= 3:
        i = segs.index(_DYN)
        before = "".join(segs[:i])
        after = "".join(segs[i + 1:])
        return ("family", before, after) if before or after else None
    return None


def collect_gd_flag_refs(game):
    """Flag refs in game/**/*.gd: list of (ref, role, where). Unresolvable (data-driven) args skip."""
    idx = _GdIndex(game)
    refs, wrappers = [], {}
    for f in idx.files:
        for name, fn in f.funcs.items():
            for line in fn["body"]:
                for m in _GD_ACCESS.finditer(line):
                    arg = _gd_arg(line, m.end()).strip()
                    arg = re.sub(r"^(?:String|StringName|str)\s*\((\w+)\)$", r"\1", arg)
                    if arg in fn["params"]:
                        wrappers[(f.rel, name)] = (fn["params"].index(arg), _access_role(line, m))
    for f in idx.files:
        for n, line in enumerate(f.lines, 1):
            if _GD_FUNC.match(line.strip()) or _GD_CONST.match(line):
                continue
            for m in _GD_ACCESS.finditer(line):
                ref = _as_ref(idx.segments(_gd_arg(line, m.end()), f))
                if ref:
                    refs.append((ref, _access_role(line, m), f"game/{f.rel}:{n}"))
            for (wrel, wname), (pos, role) in wrappers.items():
                owner = next(x for x in idx.files if x.rel == wrel)
                quals = r"(?:(\w+)\s*\.\s*)?"
                for m in re.finditer(quals + r"\b" + re.escape(wname) + r"\s*\(", line):
                    if (m.group(1) is None and f.rel != wrel) or \
                            (m.group(1) is not None and idx.classes.get(m.group(1)) is not owner):
                        continue
                    args = _gd_args(line, m.end())
                    if len(args) > pos:
                        ref = _as_ref(idx.segments(args[pos], f))
                        if ref:
                            refs.append((ref, role, f"game/{f.rel}:{n}"))
    return refs


def _access_role(line, m):
    if m.group(2):
        return "write" if m.group(2) == "set_flag" else "read"
    if m.group(1) == "erase":
        return "write"
    if m.group(1) is None:  # flags[...]
        close = m.end() + len(_gd_arg(line, m.end()))
        rest = line[close + 1:].lstrip()
        return "write" if re.match(r"(=[^=]|[+\-*/]=)", rest) else "read"
    return "read"


def _ids_in(val):
    if isinstance(val, str):
        return [val]
    if isinstance(val, list):
        return [v for v in val if isinstance(v, str)]
    if isinstance(val, dict):
        return [k for k in val]
    return []


def collect_data_flag_refs(docs):
    """Flag refs in engine JSON: list of (ref, role, where, in_scope)."""
    refs = []

    def walk(rel, node, path):
        if isinstance(node, list):
            for i, v in enumerate(node):
                walk(rel, v, f"{path}[{i}]")
            return
        if not isinstance(node, dict):
            return
        for k, v in node.items():
            where = f"game/assets/data/{rel} {path}.{k}".replace(" .", " ")
            role = None
            if (rel, k) in TIER3_CODE_DATA_KEYS:
                role, scope = TIER3_CODE_DATA_KEYS[(rel, k)], True
            elif k in DATA_FLAG_WRITE_KEYS:
                role, scope = "write", False
            elif k in DATA_FLAG_READ_KEYS:
                role, scope = "read", False
            elif k == "flag":  # an outcome or effect entry writes it; a condition reads it
                role = "write" if {"effect", "action", "event"} & set(node) else "read"
                scope = False
            if role:
                refs.extend((("id", i), role, where, scope) for i in _ids_in(v))
            elif isinstance(v, (dict, list)):
                walk(rel, v, f"{path}.{k}")

    for rel, doc in sorted(docs.items()):
        if doc is None or rel == QUEST_FLAGS_FILE:
            continue
        if rel == QUEST_LOG_FILE:
            for qi, q in enumerate(doc.get("quests", []) if isinstance(doc, dict) else []):
                _quest_log_refs(refs, rel, q, f"quests[{qi}]")
            continue
        if rel.startswith("quests/") and isinstance(doc, dict) and isinstance(doc.get("quest_flags"), dict):
            for event, ids in doc["quest_flags"].items():
                for i in _ids_in(ids):
                    refs.append((("id", i), "write", f"game/assets/data/{rel} quest_flags.{event}", True))
            doc = {k: v for k, v in doc.items() if k != "quest_flags"}
        walk(rel, doc, "")
    return refs


def _quest_log_refs(refs, rel, node, path):
    if isinstance(node, list):
        for i, v in enumerate(node):
            _quest_log_refs(refs, rel, v, f"{path}[{i}]")
    elif isinstance(node, dict):
        for k, v in node.items():
            if k in QUEST_LOG_READ_KEYS:
                refs.extend((("id", i), "read", f"game/assets/data/{rel} {path}.{k}", True) for i in _ids_in(v))
            else:
                _quest_log_refs(refs, rel, v, f"{path}.{k}")


def _pattern_parts(pid):
    holder = _PLACEHOLDER.search(pid)
    return (pid[:holder.start()], pid[holder.end():]) if holder else None


def _declared_as(ref, flags, patterns):
    """The registry key a ref resolves to (flag id or pattern id), or None."""
    if ref[0] == "id":
        if ref[1] in flags:
            return ref[1]
        for pid in patterns:
            parts = _pattern_parts(pid)
            if parts and re.fullmatch(re.escape(parts[0]) + r"[a-z0-9_.]+" + re.escape(parts[1]), ref[1]):
                return pid
        return None
    for pid in patterns:
        if _pattern_parts(pid) == (ref[1], ref[2]):
            return pid
    return None


def _ref_text(ref):
    return ref[1] if ref[0] == "id" else f"{ref[1]}{{runtime}}{ref[2]}"


def check_flag_xref(docs, game, known=None):
    """Tier 3 of the quest flag registry (Eurobound-pjas): a list of Results under TIER3_REL."""
    known = TIER3_KNOWN_UNDECLARED if known is None else known
    reg = docs.get(QUEST_FLAGS_FILE)
    if not isinstance(reg, dict) or not isinstance(reg.get("quest_flags"), dict) \
            or not isinstance(reg.get("flag_patterns"), dict):
        return []
    flags, patterns = reg["quest_flags"], reg["flag_patterns"]
    refs = collect_data_flag_refs(docs)
    if game is not None and (Path(game) / "project.godot").is_file():
        refs += [(r, role, where, True) for r, role, where in collect_gd_flag_refs(game)]
    results, undeclared, roles = [], {}, {}
    for ref, role, where, scope in refs:
        key = _declared_as(ref, flags, patterns)
        if key is None:
            undeclared.setdefault(_ref_text(ref), []).append((where, scope))
        else:
            roles.setdefault(key, set()).add(role)
    for text, sites in sorted(undeclared.items()):
        core = [w for w, s in sites if s]
        where = ", ".join(core or [w for w, _ in sites])
        if core and text not in known:
            results.append(Result("FAIL", TIER3_REL, f"'{text}' is not declared in {QUEST_FLAGS_FILE} "
                                                     f"(used at {where})"))
        elif core:
            results.append(Result("WARN", TIER3_REL, f"'{text}' is not declared in {QUEST_FLAGS_FILE} "
                                                     f"(known, {known[text]}; used at {where})"))
        else:
            results.append(Result("WARN", TIER3_REL, f"'{text}' is not declared in {QUEST_FLAGS_FILE} "
                                                     f"(engine data no script reads yet: {where})"))
    for key in sorted(known):
        if key not in undeclared or not any(s for _, s in undeclared[key]):
            results.append(Result("WARN", TIER3_REL, f"'{key}' is in TIER3_KNOWN_UNDECLARED but is now "
                                                     "declared or unused: remove it"))
    for key, entry in sorted({**flags, **patterns}.items()):
        got = roles.get(key, set())
        set_by = entry.get("set_by", []) if isinstance(entry, dict) else []
        if "read" not in got:
            what = "nothing reads or writes it" if not got else "nothing reads it (written only)"
            results.append(Result("WARN", TIER3_REL, f"'{key}' is declared but {what}"))
        elif "write" not in got and not any("NOT BUILT" in s for s in set_by if isinstance(s, str)):
            results.append(Result("WARN", TIER3_REL, f"'{key}' is read but nothing writes it and set_by "
                                                     "has no NOT BUILT note"))
    return results


def _is_num(v, minimum=None, maximum=None):
    return (isinstance(v, (int, float)) and not isinstance(v, bool)
            and (minimum is None or v >= minimum) and (maximum is None or v <= maximum))


def _status_get(entry, dotted):
    """Like _get_path, but a numeric part indexes a list (on_rest.0.flag)."""
    cur = entry
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        elif isinstance(cur, list) and part.isdigit() and int(part) < len(cur):
            cur = cur[int(part)]
        else:
            return False, None
    return True, cur


def _null_paths(obj, prefix=""):
    """Dotted paths of every null value under obj (list items by index)."""
    if obj is None:
        return [prefix]
    items = obj.items() if isinstance(obj, dict) else enumerate(obj) if isinstance(obj, list) else ()
    out = []
    for k, v in items:
        out.extend(_null_paths(v, f"{prefix}.{k}" if prefix else str(k)))
    return out


def _check_status_entry(sid, e, statuses):
    """§3 shape for one status entry (ruling 2026-11-12, Eurobound-1m4)."""
    if not isinstance(e, dict):
        return [f"{sid}: entry must be an object"]
    errs = []

    def bad(path, what):
        errs.append(f"{sid}: {path} must be {what}")

    def obj(path, v, keys):
        """True when v is an object whose keys all come from `keys` (or v is null)."""
        if v is None:
            return False
        if not isinstance(v, dict):
            bad(path, f"an object with keys from {sorted(keys)}")
            return False
        for k in v:
            if k not in keys:
                errs.append(f"{sid}: {path} has unknown key '{k}' (allowed: {sorted(keys)})")
        return True

    def enum(path, v, allowed):
        if v is not None and v not in allowed:
            bad(path, f"one of {sorted(allowed)} or null")

    def check(path, v, ok, what):
        if v is not None and not ok(v):
            bad(path, what)

    if not _SNAKE.match(sid):
        errs.append(f"{sid}: status id must be snake_case")
    if not isinstance(e.get("display_name"), str) or not e["display_name"].strip():
        errs.append(f"{sid}: missing 'display_name' (the one required field)")
    for k in e:
        if k not in STATUS_FIELDS:
            errs.append(f"{sid}: unknown field '{k}' (not in the approved shape)")

    enum("section", e.get("section"), STATUS_SECTIONS)
    check("scope", e.get("scope"), lambda v: isinstance(v, list) and v and all(s in STATUS_SCOPES for s in v),
          f"a non-empty list from {sorted(STATUS_SCOPES)} or null")
    enum("bearer", e.get("bearer"), STATUS_BEARERS)
    dd = e.get("default_duration")
    if obj("default_duration", dd, STATUS_DURATION_KEYS):
        for k in ("battle_turns", "field_steps"):
            check(f"default_duration.{k}", dd.get(k), lambda v: _is_int(v, 1), "an int >= 1 or null")
        for k in ("ends_on_rest", "until_cured"):
            check(f"default_duration.{k}", dd.get(k), lambda v: isinstance(v, bool), "true, false or null")
    enum("stack_rule", e.get("stack_rule"), STATUS_STACK_RULES)
    stats = e.get("stats")
    if obj("stats", stats, STATUS_STATS):
        for k, v in stats.items():
            check(f"stats.{k}", v, lambda x: _is_int(x, -10**9), "an int delta or null")
    check("accuracy_steps", e.get("accuracy_steps"), lambda v: _is_int(v, -10**9), "an int or null")
    check("skip_turn_chance", e.get("skip_turn_chance"), lambda v: _is_num(v, 0, 1), "a number 0-1 or null")
    check("damage_out_mult", e.get("damage_out_mult"), lambda v: _is_num(v, 0), "a number >= 0 or null")
    tick = e.get("bravado_tick")
    if obj("bravado_tick", tick, STATUS_TICK_KEYS):
        for k in ("battle_per_turn", "field_amount"):
            check(f"bravado_tick.{k}", tick.get(k), lambda v: _is_int(v, -10**9), "an int or null")
        check("bravado_tick.field_every_steps", tick.get("field_every_steps"), lambda v: _is_int(v, 1),
              "an int >= 1 or null")

    ac = e.get("attack_conversion")
    if obj("attack_conversion", ac, {"kind", "applies_to", "damage_mult", "bravado_steal", "inflict",
                                     "battle_text", "animation"}):
        if ac.get("kind") not in STATUS_CONVERSIONS:
            bad("attack_conversion.kind", f"one of {sorted(STATUS_CONVERSIONS)}")
        if ac.get("applies_to") != "attack":
            bad("attack_conversion.applies_to", "'attack' (the Attack command only)")
        check("attack_conversion.damage_mult", ac.get("damage_mult"), lambda v: _is_num(v, 0),
              "a number >= 0 or null")
        steal = ac.get("bravado_steal")
        if obj("attack_conversion.bravado_steal", steal, {"per_hit", "cap"}):
            for k in ("per_hit", "cap"):
                check(f"attack_conversion.bravado_steal.{k}", steal.get(k), lambda v: _is_int(v, 0),
                      "an int >= 0 or null")
        inf = ac.get("inflict")
        if obj("attack_conversion.inflict", inf, {"status", "chance", "turns"}):
            check("attack_conversion.inflict.status", inf.get("status"),
                  lambda v: isinstance(v, str) and _SNAKE.match(v), "a snake_case status id or null")
            check("attack_conversion.inflict.chance", inf.get("chance"), lambda v: _is_num(v, 0, 1),
                  "a number 0-1 or null")
            check("attack_conversion.inflict.turns", inf.get("turns"), lambda v: _is_int(v, 1),
                  "an int >= 1 or null")
        check("attack_conversion.battle_text", ac.get("battle_text"),
              lambda v: isinstance(v, list) and v and all(isinstance(s, str) and s.strip() for s in v),
              "a non-empty list of lines or null")
        check("attack_conversion.animation", ac.get("animation"), lambda v: isinstance(v, str) and v,
              "an animation id or null")
    check("locks", e.get("locks"), lambda v: isinstance(v, list) and all(x in STATUS_LOCKS for x in v),
          f"a list from {sorted(STATUS_LOCKS)} or null")

    fld = e.get("field")
    if obj("field", fld, STATUS_FIELD_KEYS):
        comp = fld.get("compulsion")
        if obj("field.compulsion", comp, {"kind", "every", "lasts_seconds", "input_lock"}):
            if comp.get("kind") not in STATUS_COMPULSIONS:
                bad("field.compulsion.kind", f"one of {sorted(STATUS_COMPULSIONS)}")
            every = comp.get("every")
            if obj("field.compulsion.every", every, {"amount", "unit"}):
                check("field.compulsion.every.amount", every.get("amount"), lambda v: _is_int(v, 1),
                      "an int >= 1 or null")
                enum("field.compulsion.every.unit", every.get("unit"), STATUS_COMPULSION_UNITS)
            check("field.compulsion.lasts_seconds", comp.get("lasts_seconds"), lambda v: _is_num(v, 0),
                  "a number >= 0 or null")
            check("field.compulsion.input_lock", comp.get("input_lock"), lambda v: isinstance(v, bool),
                  "true, false or null")
        check("field.text_speed_mult", fld.get("text_speed_mult"), lambda v: _is_num(v, 0),
              "a number >= 0 or null")
        enum("field.text_filter", fld.get("text_filter"), STATUS_TEXT_FILTERS)
        ch = fld.get("choices")
        if obj("field.choices", ch, {"mode", "pool"}):
            enum("field.choices.mode", ch.get("mode"), STATUS_CHOICE_MODES)
            check("field.choices.pool", ch.get("pool"),
                  lambda v: isinstance(v, list) and all(isinstance(s, str) for s in v), "a list of lines or null")

    rest = e.get("on_rest")
    if rest is not None and not isinstance(rest, list):
        bad("on_rest", "a list of {event, flag, ...params} or null")
    for i, ev in enumerate(rest if isinstance(rest, list) else []):
        if not isinstance(ev, dict) or not isinstance(ev.get("event"), str) or not _SNAKE.match(ev["event"]):
            bad(f"on_rest.{i}.event", "a snake_case event id")
        elif "flag" in ev:
            check(f"on_rest.{i}.flag", ev["flag"], lambda v: isinstance(v, str) and v, "a flag id or null")
    lad = e.get("ladder")
    if obj("ladder", lad, STATUS_LADDER_KEYS):
        for k, v in lad.items():
            check(f"ladder.{k}", v, lambda x: _is_int(x, -10**9), "an int or null")
    inter = e.get("interactions")
    if inter is not None and not isinstance(inter, list):
        bad("interactions", "a list of {with, rule, ...} or null")
    for i, it in enumerate(inter if isinstance(inter, list) else []):
        if not isinstance(it, dict):
            bad(f"interactions.{i}", "an object {with, rule, ...}")
            continue
        if not isinstance(it.get("with"), str) or not _SNAKE.match(it["with"]):
            bad(f"interactions.{i}.with", "a snake_case status id")
        rule = it.get("rule")
        if rule not in STATUS_INTERACTION_RULES:
            bad(f"interactions.{i}.rule", f"one of {sorted(STATUS_INTERACTION_RULES)}")
        elif rule == "cancel_into" and "into" not in it:
            errs.append(f"{sid}: interactions.{i} is cancel_into but has no 'into' (null while pending)")
        elif rule == "modify_then" and not (isinstance(it.get("then"), str) and _SNAKE.match(it["then"])):
            bad(f"interactions.{i}.then", "the snake_case follow-up status id a modify_then changes")
    cures = e.get("cured_by")
    if cures is not None and not isinstance(cures, list):
        bad("cured_by", "a list of {kind, value} or null")
    for i, c in enumerate(cures if isinstance(cures, list) else []):
        kind = c.get("kind") if isinstance(c, dict) else None
        if kind not in STATUS_CURE_KINDS:
            bad(f"cured_by.{i}.kind", f"one of {sorted(STATUS_CURE_KINDS)}")
        elif kind == "item_subtype" and c.get("value") not in CONSUMABLE_SUBTYPES:
            bad(f"cured_by.{i}.value", f"a consumable subtype from {sorted(CONSUMABLE_SUBTYPES)}")
        elif kind == "item_id" and not (isinstance(c.get("value"), str) and c["value"]):
            bad(f"cured_by.{i}.value", "an item id")
    then = e.get("then")
    if then is not None:
        tst = then.get("status") if isinstance(then, dict) else None
        if not isinstance(tst, str) or not _SNAKE.match(tst):
            bad("then.status", "a snake_case status id")
        elif tst not in statuses:
            errs.append(f"{sid}: then.status '{tst}' has no entry in {STATUS_FILE}")
        if not isinstance(then, dict) or not isinstance(then.get("stacks"), bool):
            bad("then.stacks", "true or false")
    cues = e.get("cues")
    if obj("cues", cues, STATUS_CUE_KEYS):
        for k, v in cues.items():
            check(f"cues.{k}", v, lambda x: isinstance(x, str) and x, "an asset id or null")

    pending = e.get("_pending", {})
    if not isinstance(pending, dict):
        errs.append(f"{sid}: _pending must be an object of dotted path -> note")
        pending = {}
    for path, note in pending.items():
        if not isinstance(note, str) or not note.strip():
            errs.append(f"{sid}: _pending note for '{path}' must be a non-empty string")
        if not _status_get(e, path)[0] or path.startswith("_pending"):
            errs.append(f"{sid}: _pending note for '{path}', which is not a field of this entry")
    for path in _null_paths({k: v for k, v in e.items() if k != "_pending"}):
        parts = path.split(".")
        if not any(".".join(parts[:n]) in pending for n in range(1, len(parts) + 1)):
            errs.append(f"{sid}: '{path}' is null but has no _pending note (at it or a parent path)")
    return errs


def check_status_effects(doc, docs):
    """Status entries in the approved shape (Eurobound-1m4): see STATUS_FILE above."""
    if not isinstance(doc, dict):
        return ["status table must be an object"]
    errs = []
    if doc.get("schema_version") != STATUS_SCHEMA_VERSION:
        errs.append(f"schema_version must be \"{STATUS_SCHEMA_VERSION}\" until Eurobound-70z rules the full "
                    f"schema, got {json.dumps(doc.get('schema_version'))}")
    table = _collection(errs, doc, "status_effects", nonempty=False)
    for sid, entry in table.items():
        errs.extend(_check_status_entry(sid, entry, set(table)))
    return errs


CHECKS = {
    "party/party_members.json": check_party,
    "enemies/debaucheryville_enemies.json": check_enemies,
    "enemies/debaucheryville_arcade_battle.json": check_arcade_battle,
    "items/consumables.json": check_consumables,
    "items/key_items.json": check_key_items,
    "skills/party_abilities.json": check_abilities,
    STATUS_FILE: check_status_effects,
    "npcs/dialogue_trees/debaucheryville_dialogue.json": check_dialogue,
    "npcs/base_profiles/debaucheryville_core.json": check_npc_profiles,
    "locations/debaucheryville/debaucheryville_locations.json": check_location_list,
    "locations/debaucheryville/debaucheryville_locations_core.json": check_location_list,
    "locations/location_nodes_debaucheryville.json": check_location_nodes,
    "locations/debaucheryville/debaucheryville_environmental.json": check_locations_dict,
    "locations/debaucheryville/debaucheryville_interactions.json": check_locations_dict,
    "locations/debaucheryville/debaucheryville_sprite_mapping.json": check_locations_dict,
    "locations/debaucheryville/absinthe_arcade_microcopy.json": check_microcopy,
    QUEST_FLAGS_FILE: check_quest_flags,
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


def _duplicate_keys(text):
    """Keys that appear twice in one JSON object (json.loads silently keeps the last)."""
    dupes = []

    def hook(pairs):
        seen = set()
        for k, _ in pairs:
            if k in seen:
                dupes.append(k)
            seen.add(k)
        return dict(pairs)

    json.loads(text, object_pairs_hook=hook)
    return dupes


def validate(root=ROOT, game=None):
    """`game` is the Godot project dir for tier 3 (default: two levels above `root`)."""
    root = Path(root)
    game = root.parent.parent if game is None else Path(game)
    docs, results = {}, []
    files = sorted(p.relative_to(root).as_posix() for p in root.rglob("*.json"))
    for rel in REQUIRED_FILES:
        if rel not in files:
            results.append(Result("FAIL", rel, "missing (the engine loads this file)"))
    for rel in files:
        try:
            text = (root / rel).read_text(encoding="utf-8-sig")
            docs[rel] = json.loads(text)
            if rel == QUEST_FLAGS_FILE:  # flag ids are unique across the file (Eurobound-vyn)
                results.extend(Result("FAIL", rel, f"duplicate key '{k}'") for k in _duplicate_keys(text))
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
    results.extend(check_flag_xref(docs, game))
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
