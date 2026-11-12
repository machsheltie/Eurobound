"""Tests for tools/validate_data.py. Run: python -I -m unittest discover -s tools/tests

Each test copies the real engine data to a temp dir, breaks one thing, and checks the
validator reports exactly that thing (or, for the baseline, does not report it).
"""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "game" / "assets" / "data"

_spec = importlib.util.spec_from_file_location("validate_data", REPO / "tools" / "validate_data.py")
vd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(vd)


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "data"
        shutil.copytree(DATA, self.root)

    def tearDown(self):
        self._tmp.cleanup()

    def load(self, rel):
        return json.loads((self.root / rel).read_text(encoding="utf-8-sig"))

    def save(self, rel, data):
        (self.root / rel).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def fails(self):
        return [f"{r.rel}: {r.msg}" for r in vd.validate(self.root) if r.status == "FAIL"]

    def statuses(self):
        return {r.rel: r.status for r in vd.validate(self.root)}

    def assertFailMentions(self, *needles):
        hits = [f for f in self.fails() if all(n in f for n in needles)]
        self.assertTrue(hits, f"no FAIL mentioning {needles}; got {self.fails()}")

    # --- coverage -------------------------------------------------------------
    def test_every_json_file_is_reported(self):
        reported = set(self.statuses())
        on_disk = {p.relative_to(self.root).as_posix() for p in self.root.rglob("*.json")}
        self.assertEqual(on_disk, reported)

    def test_unparseable_json_anywhere_fails(self):
        p = self.root / "world_data" / "events" / "icqdialogues" / "icq_group_sauce_apostates.json"
        p.write_text("{ not json", encoding="utf-8")
        self.assertFailMentions("icq_group_sauce_apostates.json", "invalid JSON")

    def test_new_unknown_file_is_still_parsed(self):
        (self.root / "world_data" / "events" / "new_thing.json").write_text("[1,", encoding="utf-8")
        self.assertFailMentions("new_thing.json", "invalid JSON")

    def test_exit_code_nonzero_on_failure(self):
        (self.root / "items" / "consumables.json").write_text("nope", encoding="utf-8")
        self.assertEqual(vd.main(self.root), 1)

    # --- pending schema (Eurobound-70z) ---------------------------------------
    def test_empty_pending_schema_file_is_pending_not_failure(self):
        st = self.statuses()
        self.assertEqual(st["items/equipment.json"], "PENDING")
        self.assertEqual(st["world_data/Shops.json"], "PENDING")
        self.assertNotIn("items/equipment.json", " ".join(self.fails()))

    def test_pending_file_missing_its_collection_fails(self):
        self.save("items/equipment.json", {"schema_version": "1.0"})
        self.assertFailMentions("items/equipment.json", "equipment")

    # --- key items (ruling 2026-08-06 + amendments) ---------------------------
    def test_key_item_missing_item_class_fails(self):
        d = self.load("items/key_items.json")
        del d["key_items"]["student_id"]["item_class"]
        self.save("items/key_items.json", d)
        self.assertFailMentions("key_items.json", "student_id", "item_class")

    def test_key_item_bad_item_class_fails(self):
        d = self.load("items/key_items.json")
        d["key_items"]["sea_monkeys"]["item_class"] = "consumable"
        self.save("items/key_items.json", d)
        self.assertFailMentions("key_items.json", "sea_monkeys", "item_class")

    def test_arcade_prize_without_effect_key_fails(self):
        d = self.load("items/key_items.json")
        del d["key_items"]["aa_prize_paraffin_pucker"]["effect"]
        self.save("items/key_items.json", d)
        self.assertFailMentions("aa_prize_paraffin_pucker", "effect")

    def test_prize_counter_item_without_ticket_price_fails(self):
        d = self.load("items/key_items.json")
        del d["key_items"]["aa_junk_promise_ish_ring"]["ticket_price"]
        self.save("items/key_items.json", d)
        self.assertFailMentions("aa_junk_promise_ish_ring", "ticket_price")

    # --- consumable intoxicant fields (ruling 2026-11-12, Eurobound-sue) -------
    def edit_item(self, iid, fn):
        d = self.load("items/consumables.json")
        fn(d["consumables"][iid])
        self.save("items/consumables.json", d)

    def test_live_consumables_pass(self):
        self.assertEqual(self.statuses()["items/consumables.json"], "OK", self.fails())

    def test_master_pool_has_huff(self):
        self.assertIn("huff", vd.master_pool_coins())

    def test_bad_subtype_fails(self):
        self.edit_item("mango_og_gushers", lambda it: it.update(subtype="edible"))
        self.assertFailMentions("mango_og_gushers", "subtype")

    def test_usable_in_unknown_place_fails(self):
        def f(it):
            it["usable_in"] = ["hot_tub"]
            del it["_pending"]["usable_in"]
        self.edit_item("mango_og_gushers", f)
        self.assertFailMentions("mango_og_gushers", "usable_in")

    def test_price_coin_must_be_in_master_pool(self):
        self.edit_item("strawberry_shortcake_speedcakes", lambda it: it["price"].update(coin="euro"))
        self.assertFailMentions("strawberry_shortcake_speedcakes", "price.coin")

    def test_price_coin_upper_case_fails(self):
        self.edit_item("strawberry_shortcake_speedcakes", lambda it: it["price"].update(coin="HUFF"))
        self.assertFailMentions("strawberry_shortcake_speedcakes", "price.coin")

    def test_bundle_qty_below_two_fails(self):
        self.edit_item("mango_og_gushers", lambda it: it["bundles"][0].update(qty=1))
        self.assertFailMentions("mango_og_gushers", "bundles[0].qty")

    def test_bundles_without_price_fail(self):
        def f(it):
            del it["price"]
            del it["_pending"]["price.amount"]
        self.edit_item("mango_og_gushers", f)
        self.assertFailMentions("mango_og_gushers", "bundles need a price")

    def test_bad_stack_rule_fails(self):
        self.edit_item("mango_og_gushers", lambda it: it["intoxicant"].update(stack_rule="double"))
        self.assertFailMentions("mango_og_gushers", "stack_rule")

    def test_intoxicant_needs_status(self):
        self.edit_item("mango_og_gushers", lambda it: it["intoxicant"].pop("status"))
        self.assertFailMentions("mango_og_gushers", "intoxicant.status")

    def test_duration_must_be_positive_int_or_null(self):
        def f(it):
            it["intoxicant"]["duration"]["battle_turns"] = 0
            del it["_pending"]["intoxicant.duration.battle_turns"]
        self.edit_item("strawberry_shortcake_speedcakes", f)
        self.assertFailMentions("strawberry_shortcake_speedcakes", "battle_turns")

    def test_then_stacks_must_be_bool(self):
        self.edit_item("strawberry_shortcake_speedcakes", lambda it: it["intoxicant"]["then"].update(stacks="yes"))
        self.assertFailMentions("strawberry_shortcake_speedcakes", "then.stacks")

    def test_null_without_pending_note_fails(self):
        self.edit_item("mango_og_gushers", lambda it: it["_pending"].pop("max_stack"))
        self.assertFailMentions("mango_og_gushers", "max_stack", "_pending")

    def test_stale_pending_note_fails(self):
        self.edit_item("strawberry_shortcake_speedcakes", lambda it: it.update(max_stack=5))
        self.assertFailMentions("strawberry_shortcake_speedcakes", "stale", "max_stack")

    def test_status_checked_against_status_table_once_it_has_entries(self):
        self.save("skills/status_effects.json", {"status_effects": {"crash": {}}})
        self.assertFailMentions("strawberry_shortcake_speedcakes", "sugar_rush_hour")

    # --- enemies, arcade battle, cross-references -----------------------------
    def test_enemy_missing_stat_fails(self):
        d = self.load("enemies/debaucheryville_enemies.json")
        del d["enemies"]["feral_segway_tourist"]["max_hp"]
        self.save("enemies/debaucheryville_enemies.json", d)
        self.assertFailMentions("feral_segway_tourist", "max_hp")

    def test_enemy_drop_must_be_a_defined_item(self):
        d = self.load("enemies/debaucheryville_enemies.json")
        d["enemies"]["feral_segway_tourist"]["item_drop"] = "no_such_item"
        self.save("enemies/debaucheryville_enemies.json", d)
        self.assertFailMentions("feral_segway_tourist", "no_such_item")

    def test_currency_enemy_drop_is_allowed(self):
        d = self.load("enemies/debaucheryville_enemies.json")
        d["enemies"]["feral_segway_tourist"]["item_drop"] = "arcade_tickets"
        self.save("enemies/debaucheryville_enemies.json", d)
        drop_fails = [f for f in self.fails() if "item_drop" in f]
        self.assertFalse([f for f in drop_fails if "feral_segway_tourist" in f])
        self.assertFalse([f for f in drop_fails if "item_absinthe_arcade_token" in f])

    def test_null_enemy_drop_is_allowed(self):
        self.assertFalse([f for f in self.fails() if "accounts_receivable" in f and "item_drop" in f])

    def test_cabinet_release_must_name_a_villain(self):
        d = self.load("enemies/debaucheryville_arcade_battle.json")
        d["cabinets"]["cabinet_frogger"]["releases"][0]["enemies"] = ["ghost_villain"]
        self.save("enemies/debaucheryville_arcade_battle.json", d)
        self.assertFailMentions("cabinet_frogger", "ghost_villain")

    def test_ladder_cabinet_needs_rungs(self):
        d = self.load("enemies/debaucheryville_arcade_battle.json")
        del d["cabinets"]["cabinet_kebab_kombat"]["rungs"]
        self.save("enemies/debaucheryville_arcade_battle.json", d)
        self.assertFailMentions("cabinet_kebab_kombat", "rungs")

    def test_villain_needs_engine_stats(self):
        d = self.load("enemies/debaucheryville_enemies.json")
        del d["enemies"]["sinking_fund"]
        self.save("enemies/debaucheryville_enemies.json", d)
        self.assertFailMentions("arcade_battle", "sinking_fund")

    def test_party_skill_must_exist(self):
        d = self.load("party/party_members.json")
        d["party_members"]["chadwick"]["skills"] = ["no_such_skill"]
        self.save("party/party_members.json", d)
        self.assertFailMentions("chadwick", "no_such_skill")

    # --- locations, microcopy, quests -----------------------------------------
    def test_locations_list_files_must_stay_lists(self):
        self.save("locations/debaucheryville/debaucheryville_locations.json", {"locations": []})
        self.assertFailMentions("debaucheryville_locations.json", "list")

    def test_location_entry_needs_location_id(self):
        d = self.load("locations/debaucheryville/debaucheryville_locations_core.json")
        del d[0]["location_id"]
        self.save("locations/debaucheryville/debaucheryville_locations_core.json", d)
        self.assertFailMentions("debaucheryville_locations_core.json", "location_id")

    def test_microcopy_needs_every_bro(self):
        d = self.load("locations/debaucheryville/absinthe_arcade_microcopy.json")
        del d["ddr_expert"]["difficulty_bounce"]["bradley"]
        self.save("locations/debaucheryville/absinthe_arcade_microcopy.json", d)
        self.assertFailMentions("microcopy", "bradley")

    def test_quest_with_legacy_mobile_optimization_key_fails(self):
        d = self.load("quests/vip_wristbands.json")
        d["mobile_optimization"] = d.pop("presentation")
        self.save("quests/vip_wristbands.json", d)
        self.assertFailMentions("vip_wristbands.json", "mobile_optimization")

    def test_quest_items_acquired_needs_known_subkeys(self):
        d = self.load("quests/vip_wristbands.json")
        d["items_acquired"] = {"acquired": d["items_acquired"]["standard"]}
        self.save("quests/vip_wristbands.json", d)
        self.assertFailMentions("vip_wristbands.json", "items_acquired")

    # --- quest flag registry, tier 2 (ruling 2026-11-12, Eurobound-vyn) -------
    QF = "world_data/quest_flags.json"
    TAB_OPEN = "debaucheryville.absinthe_arcade.cara_tab_open"

    def edit_flags(self, fn):
        d = self.load(self.QF)
        fn(d)
        self.save(self.QF, d)

    def test_quest_flags_live_registry_passes(self):
        self.assertEqual(self.statuses()[self.QF], "OK", self.fails())

    def test_quest_flags_no_longer_pending(self):
        self.assertNotIn(self.QF, vd.PENDING_SCHEMA)

    def test_quest_flags_missing_field_fails(self):
        self.edit_flags(lambda d: d["quest_flags"][self.TAB_OPEN].pop("write_once"))
        self.assertFailMentions("quest_flags.json", self.TAB_OPEN, "write_once")

    def test_quest_flags_unknown_type_fails(self):
        self.edit_flags(lambda d: d["quest_flags"][self.TAB_OPEN].update(type="counter"))
        self.assertFailMentions("quest_flags.json", self.TAB_OPEN, "type 'counter'")

    def test_quest_flags_bool_with_int_default_fails(self):
        self.edit_flags(lambda d: d["quest_flags"][self.TAB_OPEN].update(default=0))
        self.assertFailMentions("quest_flags.json", self.TAB_OPEN, "default")

    def test_quest_flags_int_with_bool_default_fails(self):
        self.edit_flags(lambda d: d["quest_flags"]["debaucheryville.absinthe_arcade.cara_tab_credit"].update(default=False))
        self.assertFailMentions("quest_flags.json", "cara_tab_credit", "default")

    def test_quest_flags_bad_category_fails(self):
        self.edit_flags(lambda d: d["quest_flags"][self.TAB_OPEN].update(category="quests"))
        self.assertFailMentions("quest_flags.json", self.TAB_OPEN, "category")

    def test_quest_flags_bad_status_fails(self):
        self.edit_flags(lambda d: d["quest_flags"][self.TAB_OPEN].update(status="approved"))
        self.assertFailMentions("quest_flags.json", self.TAB_OPEN, "status")

    def test_quest_flags_set_by_must_be_list_of_strings(self):
        self.edit_flags(lambda d: d["quest_flags"][self.TAB_OPEN].update(set_by="Fight won"))
        self.assertFailMentions("quest_flags.json", self.TAB_OPEN, "set_by")

    def test_quest_flags_flat_new_id_fails_without_legacy_id(self):
        entry = {"type": "bool", "default": False, "category": "quest", "write_once": True,
                 "set_by": [], "read_by": [], "doc": "NONE: code only", "status": "ruled"}
        self.edit_flags(lambda d: d["quest_flags"].update(path_a_chosen=entry))
        self.assertFailMentions("quest_flags.json", "path_a_chosen", "dotted")

    def test_quest_flags_legacy_id_keeps_flat_id(self):
        self.assertFalse([f for f in self.fails() if "tony420_unlocked" in f])

    def test_quest_flags_dead_doc_path_fails(self):
        self.edit_flags(lambda d: d["quest_flags"][self.TAB_OPEN].update(doc="design/quests/no_such_quest.md:12"))
        self.assertFailMentions("quest_flags.json", self.TAB_OPEN, "does not exist")

    def test_quest_flags_doc_without_line_fails(self):
        self.edit_flags(lambda d: d["quest_flags"][self.TAB_OPEN].update(doc="design/quests/debaucheryville/grandpa_provides.md"))
        self.assertFailMentions("quest_flags.json", self.TAB_OPEN, "path:line")

    def test_quest_flags_pattern_needs_exactly_one_placeholder(self):
        def f(d):
            d["flag_patterns"]["brewery_{city}_{brewery_id}"] = d["flag_patterns"].pop("brewery_stamp_{brewery_id}")
        self.edit_flags(f)
        self.assertFailMentions("quest_flags.json", "brewery_{city}_{brewery_id}", "exactly one")

    def test_quest_flags_placeholder_outside_patterns_fails(self):
        self.edit_flags(lambda d: d["quest_flags"].update({"nft_vault_{card_id}": d["flag_patterns"]["nft_vault_{card_id}"]}))
        self.assertFailMentions("quest_flags.json", "nft_vault_{card_id}", "flag_patterns")

    def test_quest_flags_duplicate_id_in_raw_json_fails(self):
        p = self.root / self.QF
        text = p.read_text(encoding="utf-8")
        p.write_text(text.replace('"quest_flags": {', '"quest_flags": {\n    "tony420_unlocked": {},', 1), encoding="utf-8")
        self.assertFailMentions("quest_flags.json", "duplicate key 'tony420_unlocked'")

    def test_quest_flags_missing_flag_patterns_fails(self):
        self.edit_flags(lambda d: d.pop("flag_patterns"))
        self.assertFailMentions("quest_flags.json", "flag_patterns")


if __name__ == "__main__":
    unittest.main()
