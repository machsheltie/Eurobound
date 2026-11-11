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


if __name__ == "__main__":
    unittest.main()
