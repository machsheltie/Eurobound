extends GutTest
## Shamsterdam Navigation roll (Eurobound-eggq). Ruled values: voetgangerstunnel.md Navigation
## Mechanics (N1-N5, Display) and docs/superpowers/specs/2026-11-12-shamsterdam-navigation-base-odds-proposal.md
## §3-§4 (approved, Eurobound-76gz; clamp and Sober, Eurobound-eb8).

const C := NavigationRoll.SIGN_CENTRAAL
const M := NavigationRoll.SIGN_MUSEUM_PLEIN

var st
var nav: NavigationRoll


func before_each() -> void:
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	st.party = [{"id": "lord_pilsner"}, {"id": "chadwick"}, {"id": "bradley"}]
	nav = NavigationRoll.new(st)


func after_each() -> void:
	st.free()


func _drunk() -> void:
	NavigationRoll.note_item_used(st, {"alcohol": true})


func _status(id: String) -> void:
	FieldStatus.apply_until_cured(st, "chadwick", id)


# --- data ---------------------------------------------------------------------------------------

func test_navigation_data_is_valid() -> void:
	assert_eq(NavigationRoll.validate(nav.data), [])


func test_navigation_exit_tables_match_the_doc() -> void:
	assert_eq(nav.base_chance(C), 40)
	assert_eq(nav.base_chance(M), 50)
	var c := nav.exit_odds(C, {})
	assert_eq(c.size(), 4)
	_drunk()
	c = nav.exit_odds(C, {})
	assert_eq(c.map(func(e): return e["chance"]), [40, 35, 15, 10])
	assert_eq(nav.exit_odds(M, {}).map(func(e): return e["chance"]), [50, 30, 20])


func test_navigation_unknown_sign_is_inert() -> void:
	assert_eq(nav.base_chance("nowhere"), -1)
	assert_eq(nav.exit_odds("nowhere", {}), [])
	assert_eq(nav.roll("nowhere", {}), {})


# --- N2 wrong-exit split (proposal §4) ----------------------------------------------------------

func test_navigation_wrong_split_centraal() -> void:
	var w := [35, 15, 10]
	assert_eq(NavigationRoll.split(w, 60), [35, 15, 10])
	assert_eq(NavigationRoll.split(w, 40), [23, 10, 7])
	assert_eq(NavigationRoll.split(w, 25), [15, 6, 4])
	assert_eq(NavigationRoll.split(w, 10), [6, 2, 2])
	assert_eq(NavigationRoll.split(w, 90), [53, 22, 15])  # tie .5/.5 goes to the higher row


func test_navigation_wrong_split_museum_plein() -> void:
	var w := [30, 20]
	assert_eq(NavigationRoll.split(w, 50), [30, 20])
	assert_eq(NavigationRoll.split(w, 30), [18, 12])
	assert_eq(NavigationRoll.split(w, 10), [6, 4])
	assert_eq(NavigationRoll.split(w, 90), [54, 36])


func test_navigation_exit_odds_sum_to_100_and_roodelicht_stays_likeliest() -> void:
	for pts in [-60, -30, -15, 0, 5, 20, 35, 50, 70]:
		var odds := nav.exit_odds(C, {"extra_points": pts})
		var total := 0
		for e in odds:
			total += int(e["chance"])
		assert_eq(total, 100, "sum at %d" % pts)
		assert_true(int(odds[1]["chance"]) >= int(odds[2]["chance"]), "Roodelicht at %d" % pts)
		assert_eq(String(odds[1]["id"]), "roodelicht_row")


# --- modifiers ----------------------------------------------------------------------------------

func test_navigation_sober_by_default_plus_20() -> void:
	assert_true(NavigationRoll.is_sober(st))
	assert_eq(nav.modifier_sum({}), 20)
	assert_eq(nav.correct_chance(C, {}), 60)
	assert_eq(nav.correct_chance(M, {}), 70)


func test_navigation_sober_lost_on_first_alcohol_and_back_at_rest() -> void:
	NavigationRoll.note_item_used(st, {"alcohol": false})
	assert_true(NavigationRoll.is_sober(st), "food or a drug does not end Sober")
	_drunk()
	assert_false(NavigationRoll.is_sober(st))
	assert_eq(nav.correct_chance(C, {}), 40)
	GameClock.rest(st)
	assert_true(NavigationRoll.is_sober(st))


func test_navigation_drinking_through_game_state_use_item_ends_sober() -> void:
	var repo := FakeRepo.new()
	st.party = [{"id": "lord_pilsner", "hp": 1, "max_hp": 10, "bravado": 0, "max_bravado": 0}]
	st.inventory = {"test_beer": 1}
	assert_true(st.use_item("test_beer", repo))
	assert_false(NavigationRoll.is_sober(st))


class FakeRepo:
	func get_item(_id: String) -> Dictionary:
		return {"alcohol": true}


func test_navigation_status_modifiers() -> void:
	_drunk()
	var cases := {
		"wobbly_windmill_navigation": -20,
		"contact_high": -15,
		"space_cake_gamble": -30,
		"canal_confusion": -25,
		"tunnel_confusion": -15,
		"tunnel_vision": 10,
	}
	for id in cases:
		FieldStatus.remove(st, id)
		assert_eq(nav.modifier_sum({}), 0, "clean before %s" % id)
		_status(id)
		assert_eq(nav.modifier_sum({}), cases[id], id)
		FieldStatus.remove(st, id)


func test_navigation_status_on_two_bros_counts_once() -> void:
	_drunk()
	FieldStatus.apply_until_cured(st, "chadwick", "wobbly_windmill_navigation")
	FieldStatus.apply_until_cured(st, "bradley", "wobbly_windmill_navigation")
	assert_eq(nav.modifier_sum({}), -20)


func test_navigation_map_guide_and_flag_modifiers() -> void:
	_drunk()
	assert_eq(nav.modifier_sum({"map_equipped": true}), 15)
	assert_eq(nav.modifier_sum({"local_guide": true}), 40)
	st.flags[NavigationRoll.FLAG_OPA_CEES] = true
	assert_eq(nav.modifier_sum({}), 5)
	st.flags.erase(NavigationRoll.FLAG_OPA_CEES)
	assert_eq(nav.modifier_sum({"opa_cees": true}), 5, "rental insurance passes it in")
	st.flags[NavigationRoll.FLAG_UNDERGROUND_NAVIGATOR] = true
	assert_eq(nav.modifier_sum({}), 5)


func test_navigation_modifier_breakdown_lists_each_source() -> void:
	_status("contact_high")
	var ids := nav.modifiers({"map_equipped": true}).map(func(m): return m["id"])
	assert_eq(ids, ["sober", "map_equipped", "contact_high"])


# --- clamp (N3) and proposal §3 cases -----------------------------------------------------------

func test_navigation_clamp_ceiling_and_floor() -> void:
	assert_eq(nav.correct_chance(C, {"local_guide": true}), 90)  # 100 -> 90
	assert_eq(nav.correct_chance(M, {"local_guide": true}), 90)  # 110 -> 90
	_drunk()
	_status("canal_confusion")
	_status("tunnel_confusion")
	assert_eq(nav.correct_chance(C, {}), 10)  # 0 -> 10
	assert_eq(nav.correct_chance(M, {}), 10)
	_status("space_cake_gamble")
	_status("wobbly_windmill_navigation")
	assert_eq(nav.correct_chance(C, {}), 10)  # -50 -> 10
	assert_eq(nav.unclamped_chance(C, {}), -50)


func test_navigation_proposal_section_3_rows() -> void:
	assert_eq(nav.correct_chance(C, {"map_equipped": true}), 75)  # row 4
	st.flags[NavigationRoll.FLAG_OPA_CEES] = true
	st.flags[NavigationRoll.FLAG_UNDERGROUND_NAVIGATOR] = true
	assert_eq(nav.correct_chance(C, {"map_equipped": true}), 85)  # row 5
	assert_eq(nav.correct_chance(M, {"map_equipped": true}), 90)  # row 5, 95 clamped
	st.flags.erase(NavigationRoll.FLAG_OPA_CEES)
	st.flags.erase(NavigationRoll.FLAG_UNDERGROUND_NAVIGATOR)
	_drunk()
	assert_eq(nav.correct_chance(C, {"local_guide": true}), 80)  # row 6
	_status("canal_confusion")
	assert_eq(nav.correct_chance(C, {"local_guide": true, "map_equipped": true}), 70)  # row 22


# --- per-visit counter (N4) ---------------------------------------------------------------------

func test_navigation_per_visit_success_counter_and_reset() -> void:
	_drunk()
	assert_eq(nav.successes_this_visit(), 0)
	var r := nav.roll(C, {}, 0)  # draw 0 lands on the correct exit
	assert_true(r["correct"])
	assert_eq(String(r["exit"]), "centraal_chaos")
	assert_eq(nav.successes_this_visit(), 1)
	assert_eq(nav.modifier_sum({}), 5)
	nav.roll(C, {}, 0)
	assert_eq(nav.modifier_sum({}), 10)
	assert_eq(nav.correct_chance(C, {}), 50)
	nav.leave_tunnel()
	assert_eq(nav.successes_this_visit(), 0)
	assert_eq(nav.modifier_sum({}), 0)


func test_navigation_counter_survives_a_new_instance_until_leaving() -> void:
	_drunk()
	nav.roll(M, {}, 0)
	var again := NavigationRoll.new(st)
	assert_eq(again.successes_this_visit(), 1)
	again.leave_tunnel()
	assert_eq(NavigationRoll.new(st).successes_this_visit(), 0)


func test_navigation_wrong_exit_does_not_count() -> void:
	_drunk()
	var r := nav.roll(C, {}, 99)
	assert_false(r["correct"])
	assert_eq(String(r["exit"]), "where_you_started")
	assert_eq(nav.successes_this_visit(), 0)


# --- the roll -----------------------------------------------------------------------------------

func test_navigation_roll_draw_maps_onto_cumulative_odds() -> void:
	_drunk()  # Centraal 40 / 35 / 15 / 10
	assert_eq(String(nav.roll(C, {}, 39)["exit"]), "centraal_chaos")
	nav.leave_tunnel()
	assert_eq(String(nav.roll(C, {}, 40)["exit"]), "roodelicht_row")
	assert_eq(String(nav.roll(C, {}, 74)["exit"]), "roodelicht_row")
	assert_eq(String(nav.roll(C, {}, 75)["exit"]), "coffeeshop_quarter")
	assert_eq(String(nav.roll(C, {}, 89)["exit"]), "coffeeshop_quarter")
	assert_eq(String(nav.roll(C, {}, 90)["exit"]), "where_you_started")
	assert_eq(String(nav.roll(M, {}, 50)["exit"]), "frietomat")
	assert_eq(String(nav.roll(M, {}, 80)["exit"]), "canal_surface")


func test_navigation_roll_reports_the_chance_used() -> void:
	var r := nav.roll(M, {"map_equipped": true}, 0)
	assert_eq(int(r["chance"]), 85)
	assert_eq(r["odds"].size(), 3)


func test_navigation_rng_roll_respects_the_floor_and_ceiling() -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = 7
	var seeded := NavigationRoll.new(st, rng)
	var hits := 0
	for i in 2000:
		if seeded.roll(C, {"local_guide": true})["correct"]:
			hits += 1
		seeded.leave_tunnel()
	assert_between(hits, 1700, 1900, "90% cap over 2000 rolls")


# --- display (map only) -------------------------------------------------------------------------

func test_navigation_display_only_with_map() -> void:
	assert_eq(nav.display_chance(C, {}), -1)
	assert_eq(nav.display_chance(C, {"map_equipped": true}), 75)
	assert_eq(nav.display_text(C, {}), "")
	assert_eq(nav.display_text(C, {"map_equipped": true}), "75%")
