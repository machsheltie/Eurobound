extends GutTest
## Quest data loader (Eurobound-zkhb): assets/data/quests/*.json -> the Quest Log's registry shape.
## The loader never fills a gap: a quest missing a field the log needs is reported, not shown.

const TMP := "user://test_quest_data"

class FakeState:
	var flags := {}


func _doc() -> Dictionary:
	return {
		"quest_id": "testville_sidequest_fixture_01",
		"display_name": "Fixture Quest",
		"quest_stages": [
			{"stage_id": 1, "name": "first_bit", "done_when": ["testville.venue.first_done"]},
			{"stage_id": "2a", "name": "second_bit", "objective": "Do the second bit.",
				"done_when": ["testville.venue.second_done", "testville.venue.second_skipped"]},
		],
		"quest_flags": {
			"on_start": ["testville.venue.fixture_started"],
			"on_complete_a": ["testville.venue.fixture_complete", "testville.venue.path_a"],
			"on_complete_b": ["testville.venue.fixture_complete", "testville.venue.path_b"],
			"permanent": ["testville.venue.never_read_by_the_log"],
		},
	}


func _write(name: String, text: String) -> void:
	DirAccess.make_dir_recursive_absolute(TMP)
	var f := FileAccess.open(TMP + "/" + name, FileAccess.WRITE)
	f.store_string(text)
	f.close()


func after_each() -> void:
	if DirAccess.dir_exists_absolute(TMP):
		for f in DirAccess.get_files_at(TMP):
			DirAccess.remove_absolute(TMP + "/" + f)
		DirAccess.remove_absolute(TMP)


func test_quest_data_complete_quest_converts_to_the_quest_log_shape() -> void:
	var r := QuestData.to_log_entry(_doc())
	assert_eq(r["missing"], [])
	var e: Dictionary = r["entry"]
	assert_eq(e["quest_id"], "testville_sidequest_fixture_01")
	assert_eq(e["display_name"], "Fixture Quest")
	assert_eq(e["started_when"], ["testville.venue.fixture_started"])
	assert_eq(e["completed_when"], ["testville.venue.fixture_complete", "testville.venue.path_a",
		"testville.venue.path_b"], "on_complete* lists, de-duplicated; other groups are not read")
	assert_eq(e["steps"], [
		{"id": "first_bit", "objective": "", "done_when": ["testville.venue.first_done"]},
		{"id": "second_bit", "objective": "Do the second bit.",
			"done_when": ["testville.venue.second_done", "testville.venue.second_skipped"]},
	])


func test_quest_data_plain_on_complete_list_is_read() -> void:
	var d := _doc()
	d["quest_flags"] = {"on_start": ["a.b.s"], "on_complete": ["a.b.c"]}
	assert_eq(QuestData.to_log_entry(d)["entry"]["completed_when"], ["a.b.c"])


func test_quest_data_converted_quest_runs_through_the_quest_log() -> void:
	var q: Dictionary = QuestData.to_log_entry(_doc())["entry"]
	var s := FakeState.new()
	assert_eq(QuestLog.status(s, q), "hidden")
	s.flags["testville.venue.fixture_started"] = true
	s.flags["testville.venue.first_done"] = true
	assert_eq(QuestLog.status(s, q), "active")
	assert_eq(QuestLog.steps(s, q).map(func(x): return x["state"]), ["done", "current"])
	assert_eq(QuestLog.label(QuestLog.steps(s, q)[0]), "First Bit")
	s.flags["testville.venue.path_b"] = true
	assert_eq(QuestLog.status(s, q), "completed")


func test_quest_data_missing_name_is_reported_not_invented() -> void:
	var d := _doc()
	d.erase("display_name")
	var r := QuestData.to_log_entry(d)
	assert_eq(r["missing"], ["display_name"])
	assert_eq(r["entry"], {})


func test_quest_data_missing_states_are_reported() -> void:
	var d := _doc()
	d["quest_flags"] = {"permanent": ["a.b.c"]}
	assert_eq(QuestData.to_log_entry(d)["missing"],
		["quest_flags.on_start", "quest_flags.on_complete*"])


func test_quest_data_missing_steps_are_reported_per_stage() -> void:
	var d := _doc()
	d["quest_stages"][0].erase("done_when")
	d["quest_stages"][1].erase("name")
	assert_eq(QuestData.to_log_entry(d)["missing"],
		["quest_stages[first_bit].done_when", "quest_stages[2a].name"])
	d["quest_stages"] = []
	assert_eq(QuestData.to_log_entry(d)["missing"], ["quest_stages"])


func test_quest_data_missing_quest_id_is_reported() -> void:
	var d := _doc()
	d.erase("quest_id")
	assert_eq(QuestData.to_log_entry(d)["missing"], ["quest_id"])


func test_quest_data_load_dir_splits_complete_from_incomplete_in_file_order() -> void:
	var bad := _doc()
	bad["quest_id"] = "testville_sidequest_gappy_01"
	bad["quest_flags"].erase("on_start")
	_write("b_good.json", JSON.stringify(_doc()))
	_write("a_gappy.json", JSON.stringify(bad))
	_write("c_broken.json", "{ not json")
	_write("notes.txt", "ignored")
	var r := QuestData.load_dir(TMP)
	assert_eq(r["quests"].map(func(q): return q["quest_id"]), ["testville_sidequest_fixture_01"])
	assert_eq(r["incomplete"], [
		{"file": "a_gappy.json", "quest_id": "testville_sidequest_gappy_01",
			"missing": ["quest_flags.on_start"]},
		{"file": "c_broken.json", "quest_id": "", "missing": ["valid JSON object"]},
	])


func test_quest_data_load_dir_of_a_missing_folder_is_empty() -> void:
	assert_eq(QuestData.load_dir("user://no_such_quest_folder"), {"quests": [], "incomplete": []})


func test_quest_data_report_lines_name_the_file_and_the_gaps() -> void:
	var lines := QuestData.report([{"file": "x.json", "quest_id": "q_01", "missing": ["display_name", "quest_stages"]}])
	assert_eq(lines, ["x.json (q_01): missing display_name, quest_stages"])


func test_quest_data_merge_keeps_the_registry_first_and_wins_duplicates() -> void:
	var registry := [{"quest_id": "a", "display_name": "Registry A"}]
	var data := [{"quest_id": "a", "display_name": "Data A"}, {"quest_id": "b", "display_name": "Data B"}]
	assert_eq(QuestLog.merged(registry, data).map(func(q): return q["display_name"]),
		["Registry A", "Data B"])


func test_quest_data_every_shipped_quest_file_is_loaded_or_reported() -> void:
	var r := QuestData.load_dir()
	var files := Array(DirAccess.get_files_at(QuestData.DIR)).filter(func(f): return f.ends_with(".json"))
	assert_gt(files.size(), 0)
	assert_eq(r["quests"].size() + r["incomplete"].size(), files.size())
	for row in r["incomplete"]:
		assert_gt(row["missing"].size(), 0, row["file"])


## Step markers approved by the author (Eurobound Desk Eurobound-wn1f-q2 "Approve as proposed",
## wn1f-q3 "A for all four"): docs/superpowers/specs/2026-11-15-quest-step-markers-proposal.md.
const SQUARE := "debaucheryville.astronomical_cockup_square."
const CLUB := "debaucheryville.velvet_curtain_club."
const APPROVED_STEPS := {
	"debaucheryville_sidequest_astronomical_cockup_01": [
		["the_gathering", SQUARE + "astronomical_cockup_started"],
		["scam_gauntlet", SQUARE + "cockup_scam_gauntlet_done"],
		["the_show", SQUARE + "clock_show_witnessed"],
		["emotional_response", SQUARE + "crying_triggered"],
		["path_choice", SQUARE + "cockup_path_chosen"],
		["full_clock_experience", SQUARE + "cockup_full_clock_experience_done"],
		["the_tattoo", "debaucheryville.euro_ink_4_less.duck_tattoo_acquired"],
		["secret_show_seekers", SQUARE + "secret_show_sucker"],
	],
	"debaucheryville_sidequest_vip_wristbands_01": [
		["the_approach", SQUARE + "vip_wristband_quest_started"],
		["the_transaction", SQUARE + "wristbands_purchased"],
		["wristband_application", SQUARE + "vip_wristbands_all_bros"],
		["velvet_curtain_approach", CLUB + "wristband_approach_seen"],
		["bouncer_encounter", CLUB + "bouncer_read_wristband"],
		["the_revelation_ignored", CLUB + "birthday_wristband_explained"],
		["entry_granted", CLUB + "vip_wristband_quest_complete"],
	],
	# Author, Eurobound Desk Eurobound-3ddh-q1 "Approve; path A is done after the six postering jobs (A)":
	# docs/superpowers/specs/2026-11-17-club-flyers-step-markers-proposal.md.
	"debaucheryville_sidequest_club_flyers_01": [
		["quest_initiation", CLUB + "club_flyers_started"],
		["the_design_phase", CLUB + "club_flyers_design_phase_done"],
		["the_flyer_creation", CLUB + "club_flyers_flyer_created"],
		["binary_path_choice", CLUB + "club_flyers_path_chosen"],
		["web_1_0_marketing_mastery", CLUB + "club_flyers_path_a_done"],
		["alpha_male_vandalism_2001", CLUB + "club_flyers_path_b_done"],
	],
}


func _shipped(quest_id: String) -> Dictionary:
	for q in QuestData.load_dir()["quests"]:
		if q["quest_id"] == quest_id:
			return q
	return {}


func test_quest_data_shipped_quest_files_are_all_complete() -> void:
	var r := QuestData.load_dir()
	assert_eq(QuestData.report(r["incomplete"]), [], "every shipped quest file reaches the Quest Log")


func test_quest_data_shipped_steps_carry_the_approved_markers() -> void:
	for quest_id in APPROVED_STEPS:
		var q := _shipped(quest_id)
		assert_false(q.is_empty(), quest_id + " loads")
		if q.is_empty():
			continue
		var got: Array = q["steps"].map(func(s): return [s["id"], s["done_when"]])
		var want: Array = APPROVED_STEPS[quest_id].map(func(p): return [p[0], [p[1]]])
		assert_eq(got, want, quest_id)


func test_quest_data_shipped_completion_markers_are_the_approved_ones() -> void:
	var cockup := _shipped("debaucheryville_sidequest_astronomical_cockup_01")
	var vip := _shipped("debaucheryville_sidequest_vip_wristbands_01")
	assert_eq(vip.get("completed_when"), [CLUB + "vip_wristband_quest_complete"],
		"VIP finishes when the bros walk into the club")
	# Reading A for Cock-Up 7a: the tattoo marker stays in both on_complete lists (no change).
	assert_eq(cockup.get("completed_when"), [SQUARE + "astronomical_cockup_complete",
		SQUARE + "cockup_path_a_chosen", "debaucheryville.euro_ink_4_less.duck_tattoo_acquired",
		SQUARE + "cockup_path_b_chosen", SQUARE + "secret_show_sucker"])


func test_quest_data_shipped_markers_are_declared_in_the_flag_registry() -> void:
	var reg = JSON.parse_string(FileAccess.get_file_as_string(
		"res://assets/data/world_data/quest_flags.json"))
	var declared: Dictionary = reg["quest_flags"]
	for q in QuestData.load_dir()["quests"]:
		var ids: Array = q["started_when"] + q["completed_when"]
		for s in q["steps"]:
			ids += s["done_when"]
		for id in ids:
			assert_true(declared.has(id), "%s declares %s" % [q["quest_id"], id])


func test_quest_data_shipped_step_markers_tick_the_vip_log_in_order() -> void:
	var q := _shipped("debaucheryville_sidequest_vip_wristbands_01")
	var s := FakeState.new()
	s.flags[SQUARE + "vip_wristband_quest_started"] = true
	s.flags[SQUARE + "wristbands_purchased"] = true
	assert_eq(QuestLog.status(s, q), "active")
	assert_eq(QuestLog.steps(s, q).map(func(x): return x["state"]).slice(0, 3),
		["done", "done", "current"])
	s.flags[CLUB + "vip_wristband_quest_complete"] = true
	assert_eq(QuestLog.status(s, q), "completed")


func test_quest_data_cockup_scam_gauntlet_total_is_the_ruled_270() -> void:
	# Author ruling (Eurobound Desk Eurobound-r61w-q1): "270 SOVS: the prices are right, fix the
	# total". 30 viewing spot + 60 Monk blessing + three bottles of clock wine at 60.
	var doc = JSON.parse_string(FileAccess.get_file_as_string(QuestData.DIR + "/astronomical_cockup.json"))
	var price := {}
	for npc in doc["npcs"]:
		price[npc["npc_id"]] = npc.get("cost", npc.get("cost_per_bottle", 0))
	var gauntlet: Dictionary = doc["quest_stages"][1]
	assert_eq(gauntlet["name"], "scam_gauntlet")
	assert_eq(int(gauntlet["total_money_spent"]), 270)
	assert_eq(int(price["viewing_spot_scammer"] + price["party_monk"] + 3 * price["clock_wine_vendor"]), 270)


func test_quest_data_quest_log_lists_registry_then_every_complete_data_quest() -> void:
	var ids := QuestLog.quests().map(func(q): return q["quest_id"])
	assert_eq(ids[0], "debaucheryville_sidequest_grandpa_provides_01")
	for q in QuestData.load_dir()["quests"]:
		assert_has(ids, q["quest_id"])
	for row in QuestData.load_dir()["incomplete"]:
		assert_does_not_have(ids, row["quest_id"])
