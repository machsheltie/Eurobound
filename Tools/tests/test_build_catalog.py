"""Tests for Tools/catalog/build_catalog.py, on a tiny fixture tree."""
import datetime
import importlib.util
import json
import os
import shutil
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(os.path.dirname(HERE), "catalog", "build_catalog.py")
spec = importlib.util.spec_from_file_location("build_catalog", SCRIPT)
bc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bc)

FILES = {
    "design/worlds/testville/the_pit.md": (
        "# The Pit\n\n*A hole with a cover charge*\n\n## Location Identity\n"
        "- **Location ID**: testville_pit_01\n- **Display Name**: The Pit\n"
        "- **Area Zone**: Low Street\n- **Location Type**: Dive Bar\n"),
    "design/worlds/testville/testville.md": "TESTVILLE\nCity overview.\n",
    "design/worlds/testville/core/the_pit_core.json": json.dumps({
        "location_id": "testville_pit_01", "display_name": "The Pit",
        "satirical_subtitle": "Mind the drop", "location_type": "dive_bar"}),
    "design/worlds/testville/core/annex_core.json": json.dumps({
        "location_id": "testville_annex_01", "display_name": "The Annex",
        "satirical_subtitle": "Overflow seating", "location_type": "annex"}),
    "design/worlds/testville/core/broken_core.json": "{ this is not json",
    "design/worlds/testville/npcs/The_Pit/npc_big_dave.md": (
        "# NPC Profile: Big Dave\n\n*\"Stairs are for closers.\"*\n\n"
        "## NPC Identity\n- **NPC ID**: `testville_npc_big_dave_01`\n"
        "- **Display Name**: Big Dave\n- **Role**: Doorman\n"),
    "design/worlds/testville/npcs/The_Pit/npc_quiet_sue.md": (
        "# NPC Profile: Quiet Sue\n\n## NPC Identity\n"
        "- **NPC ID**: `testville_npc_quiet_sue_01`\n- **Role**: Regular\n"),
    "design/worlds/testville/npcs/The_Pit/the_pit_npcs.json": json.dumps({
        "location_id": "testville_pit_01", "location_name": "The Pit",
        "npcs": [
            {"npc_id": "tp_npc_dave", "display_name": "Dave", "role": "doorman",
             "profile": "design/worlds/testville/npcs/The_Pit/npc_big_dave.md"},
            {"npc_id": "tp_npc_ghost", "display_name": "Nameless Regular",
             "role": "regular"}],
        "ambient_npcs": [{"group_id": "tp_crowd", "display_name": "drinkers"}]}),
    "design/worlds/testville/villains/the_pit/the_landlord.md": (
        "# Villain Profile: The Landlord\n\n*\"Rent is a feeling.\"*\n\n"
        "- **Villain ID**: `testville_villain_landlord_01`\n"
        "- **Display Name**: The Landlord\n- **Tier**: Minor Villain\n"),
    "design/worlds/testville/items/the_pit_items.json": json.dumps({
        "location_id": "testville_pit_01",
        "items": [{"item_id": "item_pit_helmet", "display_name": "Pit Helmet",
                   "item_type": "equipment"},
                  {"item_id": "item_other_pint", "display_name": "Warm Pint",
                   "item_type": "consumable", "description": "A second warm pint."}]}),
    "design/items/warm_pint_item.md": (
        "# Item Definition: Warm Pint\n\n*Room temperature, by design*\n\n"
        "- **Item ID**: `item_warm_pint`\n- **Display Name**: Warm Pint\n"
        "- **Item Type**: Consumable\n- **Source**: The Pit, Testville\n"),
    "design/items/brewery_tour/stamp_the_pit_item.md": (
        "# Stamp: The Pit\n\n- **Item ID**: `stamp_the_pit`\n- **City**: Testville\n"
        "- **Stamp Face**: A hole\n"),
    "design/legacy/old_item.md": (
        "# Item Definition: Legacy Thing\n- **Item ID**: `item_legacy_thing`\n"),
    "design/World Design/Testville/the_pit.md": (
        "# The Pit\n- **Location ID**: testville_pit_99\n"),
    "design/quests/testville/find_the_stairs.md": (
        "# Sidequest: Find the Stairs\n\n- **Quest ID:** `testville_sidequest_stairs_01`\n"),
    "design/quests/general_quests/plainquest.md": (
        "Plain Quest\nBros look for a thing and do not find it.\n"),
    "design/mechanics/Battle/status_effects.md": (
        "Status Effects\nPOSITIVE STATUS EFFECTS\n\"Pit Fever\"\n"
        "    • +1 Charm\n    • Description: \"Feeling low and loving it\"\n"),
    "design/mechanics/Battle/battle_system.md": (
        "Dave (The Door Bro)\nRole: Tank\nCore Abilities:\n"
        "    • Door Slam — Stuns one enemy.\nPersonality Combat Flavor:\n"
        "    • Slow but reliable — keeps the door shut.\n"),
    "game/assets/data/items/consumables.json": json.dumps({
        "consumables": {
            "warm_pint": {"display_name": "Warm Pint", "description": "x"},
            "mystery_crisps": {"display_name": "Mystery Crisps",
                               "description": "Flavour: beige."}}}),
    "game/assets/data/enemies/testville_enemies.json": json.dumps({
        "world_name": "testville",
        "enemies": {"stair_goblin": {"display_name": "Stair Goblin",
                                     "battle_intro": "A Stair Goblin trips you!"}}}),
    "game/assets/data/skills/status_effects.json": json.dumps({
        "status_effects": {"pit_fever": {"display_name": "Pit Fever"}}}),
    "game/assets/worlds/testville/the_pit/exterior/front.png": "png",
    "game/assets/characters/npcs/testville/big_dave.aseprite": "art",
    "game/core/door.gd": "extends Node\n",
    "game/tests/unit/test_door.gd": "extends Node\n",
    "docs/research/audit.md": (
        "### Battle\n\n"
        "| Mechanic | Design | Rulings open | Code | Tests | Data | What's missing | Beads |\n"
        "|---|---|---|---|---|---|---|---|\n"
        "| Battle doors | `mechanics/Battle/battle_system.md:2-5` | None | `core/door.gd` | "
        "`test_door` | n/a | Nothing | none |\n"
        "| Save and load | Ledger only | Yes: when it fires | `core/missing.gd` | None | "
        "n/a | Everything | **ab12**, cd3 (art) |\n"),
}

BEADS = [
    {"id": "Eurobound-ab12", "title": "Make the game save", "status": "open",
     "description": "Nothing calls it."},
    {"id": "Eurobound-cd3", "title": "Title art", "status": "closed", "description": ""},
    {"id": "Eurobound-zz9", "title": "Draw Big Dave", "status": "open",
     "description": "Sprite for testville_npc_big_dave_01."},
    {"id": "Eurobound-zz8", "title": "Old Big Dave task", "status": "closed",
     "description": "Big Dave"},
]


class BuildCatalogTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = tempfile.mkdtemp(prefix="catalog_fixture_")
        for rel, text in FILES.items():
            path = os.path.join(cls.root, *rel.split("/"))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(text)
        ctx = bc.Context(cls.root)
        cls.seed = bc.seed_from_audit(ctx, "docs/research/audit.md")
        bc.write(os.path.join(cls.root, "Tools", "catalog", "game_elements.json"),
                 json.dumps(cls.seed))
        cls.now = datetime.datetime(2026, 11, 14, 12, 0, tzinfo=datetime.timezone.utc)
        cls.payload = bc.build(cls.root, beads=BEADS, now=cls.now)
        cls.rows = {c["id"]: c["rows"] for c in cls.payload["categories"]}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.root, ignore_errors=True)

    def row(self, category, name):
        hits = [r for r in self.rows[category] if r["name"] == name]
        self.assertEqual(len(hits), 1, "%s rows named %r" % (len(hits), name))
        return hits[0]

    def read(self, name):
        with open(os.path.join(self.root, "docs", "catalog", name), encoding="utf-8") as handle:
            return handle.read()

    def test_every_file_is_written_with_the_header_line(self):
        names = [cid + ".md" for cid, _title in bc.CATEGORY_TITLES]
        names.append("game_elements_status.md")
        for name in names:
            first = self.read(name).splitlines()[0]
            self.assertIn("Generated 2026-11-14 12:00 UTC", first, name)
            self.assertIn("do not edit by hand; run Tools/catalog/build_catalog.py", first)
        data = json.loads(self.read("catalog.json"))
        self.assertEqual(data["generated_at"], "2026-11-14T12:00:00Z")
        self.assertEqual([c["id"] for c in data["categories"]],
                         [cid for cid, _title in bc.CATEGORY_TITLES])

    def test_location_merges_doc_and_core_json(self):
        pit = self.row("locations", "The Pit")
        self.assertEqual(pit["city"], "Testville")
        self.assertEqual(pit["summary"], "A hole with a cover charge")
        self.assertTrue(pit["doc"].endswith("the_pit.md"))
        self.assertTrue(pit["art"])
        self.assertFalse(pit["engine_data"])
        annex = self.row("locations", "The Annex")
        self.assertIn("no location doc (companion JSON only)", annex["flags"])
        self.assertEqual(len(self.rows["locations"]), 2)

    def test_legacy_and_world_design_are_skipped(self):
        text = json.dumps(self.payload)
        self.assertNotIn("Legacy Thing", text)
        self.assertNotIn("testville_pit_99", text)

    def test_bad_json_is_reported_not_fatal(self):
        self.assertTrue(any(p["path"].endswith("broken_core.json")
                            for p in self.payload["problems"]))

    def test_npc_doc_and_json_merge_and_flags(self):
        dave = self.row("npcs", "Big Dave")
        self.assertEqual(dave["kind"], "Doorman")
        self.assertTrue(dave["art"])
        self.assertEqual(dave["open_beads"], ["Eurobound-zz9"])
        self.assertTrue(any("tp_npc_dave" in f for f in dave["flags"]))
        ghost = self.row("npcs", "Nameless Regular")
        self.assertIn("no profile doc (companion JSON only)", ghost["flags"])
        sue = self.row("npcs", "Quiet Sue")
        self.assertEqual(sue["summary"], "")
        self.assertIn(bc.NO_SUMMARY, sue["flags"])
        self.assertTrue(self.row("npcs", "drinkers")["ambient"])

    def test_items_are_grouped_and_engine_only_rows_appear(self):
        groups = {r["name"]: r["group"] for r in self.rows["items"]}
        self.assertEqual(groups["Pit Helmet"], "equipment")
        self.assertEqual(groups["Stamp: The Pit"], "stamp")
        self.assertEqual(groups["Mystery Crisps"], "consumable")
        crisps = self.row("items", "Mystery Crisps")
        self.assertFalse(crisps["design_doc"])
        self.assertTrue(crisps["engine_data"])
        self.assertEqual(crisps["summary"], "Flavour: beige.")
        items_md = self.read("items.md")
        self.assertIn("## Consumables (3)", items_md)
        self.assertIn("## Passport stamps (1)", items_md)

    def test_duplicate_names_are_flagged(self):
        names = {d["name"]: d for d in self.payload["duplicates"]}
        self.assertIn("Warm Pint", names)
        self.assertEqual(names["Warm Pint"]["scope"], "same category")
        self.assertEqual(len(names["Warm Pint"]["entries"]), 2)
        self.assertIn("**Warm Pint** (same category)", self.read("items.md"))
        self.assertNotIn("drinkers", names)

    def test_villains_quests_status_and_abilities(self):
        landlord = self.row("enemies_and_villains", "The Landlord")
        self.assertEqual(landlord["kind"], "Villain: Minor Villain")
        goblin = self.row("enemies_and_villains", "Stair Goblin")
        self.assertFalse(goblin["design_doc"])
        self.assertEqual(self.row("quests", "Find the Stairs")["city"], "Testville")
        plain = self.row("quests", "Plain Quest")
        self.assertEqual(plain["summary"], "Bros look for a thing and do not find it.")
        fever = self.row("status_effects_and_abilities", "Pit Fever")
        self.assertEqual(fever["summary"], "Feeling low and loving it")
        self.assertTrue(fever["engine_data"])
        slam = self.row("status_effects_and_abilities", "Door Slam")
        self.assertEqual(slam["kind"], "Ability (Dave)")
        names = [r["name"] for r in self.rows["status_effects_and_abilities"]]
        self.assertNotIn("Slow but reliable", names)

    def test_rows_are_sorted_by_name_within_city(self):
        for rows in self.rows.values():
            keys = [(r["city"].lower(), r["name"].lower()) for r in rows]
            self.assertEqual(keys, sorted(keys))

    def test_seed_from_audit_maps_systems_and_files(self):
        systems = {s["id"]: s["elements"] for s in self.seed["systems"]}
        self.assertEqual([s["id"] for s in self.seed["systems"]][:3],
                         ["battle", "levelling", "intoxication"])
        doors = systems["battle"][0]
        self.assertEqual(doors["code_files"], ["game/core/door.gd"])
        self.assertEqual(doors["test_files"], ["game/tests/unit/test_door.gd"])
        self.assertEqual(doors["design_files"], ["design/mechanics/Battle/battle_system.md"])
        save = systems["save_load"][0]
        self.assertEqual(save["beads"], ["Eurobound-ab12", "Eurobound-cd3"])

    def test_game_elements_follow_files_and_bead_status(self):
        systems = {s["id"]: s["rows"] for s in self.payload["game_elements"]}
        doors = systems["battle"][0]
        self.assertEqual(doors["status"], "complete")
        self.assertEqual(doors["built"]["state"], "yes")
        self.assertEqual(doors["tested"]["state"], "yes")
        save = systems["save_load"][0]
        self.assertEqual(save["ruled"]["state"], "no")
        self.assertEqual(save["tested"]["state"], "no")
        self.assertEqual({b["id"]: b["status"] for b in save["beads"]},
                         {"Eurobound-ab12": "open", "Eurobound-cd3": "closed"})
        self.assertEqual(save["open_beads"], ["Eurobound-ab12"])
        page = self.read("game_elements_status.md")
        self.assertIn("## Save and load", page)
        self.assertIn("ab12 (open), cd3 (closed)", page)
        self.assertIn("## Audio", page)

    def test_closing_a_bead_and_deleting_code_changes_the_page(self):
        closed = [dict(b, status="closed") for b in BEADS]
        os.remove(os.path.join(self.root, "game", "core", "door.gd"))
        try:
            payload = bc.build(self.root, out_rel="docs/catalog_b", beads=closed, now=self.now)
        finally:
            bc.write(os.path.join(self.root, "game", "core", "door.gd"), "extends Node\n")
        systems = {s["id"]: s["rows"] for s in payload["game_elements"]}
        self.assertEqual(systems["battle"][0]["built"]["state"], "files missing")
        self.assertEqual(systems["save_load"][0]["status"],
                         "all beads closed; re-check this row")
        npcs = [r for c in payload["categories"] if c["id"] == "npcs" for r in c["rows"]]
        self.assertEqual([r["open_beads"] for r in npcs if r["name"] == "Big Dave"], [[]])

    def test_build_without_beads_says_so(self):
        payload = bc.build(self.root, out_rel="docs/catalog_c", beads=None,
                           beads_note="bd was skipped (--no-beads)", now=self.now)
        self.assertEqual(payload["beads_note"], "bd was skipped (--no-beads)")
        with open(os.path.join(self.root, "docs", "catalog_c", "game_elements_status.md"),
                  encoding="utf-8") as handle:
            self.assertIn("Bead statuses are missing from this build", handle.read())

    def test_helpers(self):
        self.assertEqual(bc.norm("Jiří the Commuter"), "jiri_the_commuter")
        self.assertEqual(bc.clean_name("Napster | legacy_vault_cards.md:63"), "Napster")
        self.assertEqual(
            bc.clean_name("Grandpa Provides (title only, round v30: nobody says it aloud)"),
            "Grandpa Provides")
        self.assertEqual(bc.item_group("Permanent Hybrid, not a consumable"), "permanent")
        self.assertEqual(bc.item_group("", "sea_monkeys_nft_item"), "nft")
        self.assertEqual(bc.md_field("- **Quest ID:** `q_1`", "Quest ID"), "`q_1`")
        self.assertEqual(bc.md_field("| **Style** | Golden Ale |", "Style"), "Golden Ale")


if __name__ == "__main__":
    unittest.main()
