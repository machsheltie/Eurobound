extends GutTest
## TaproomBattle: Mirror Chad (package A) and the Green Fairy Wisp (72 HP), round v44.
## the_absinthium_taproom.md:152-185; docs/superpowers/proposals/2026-11-12-v43-design-proposals.md 1.2-1.4.


class FakeState:
	var sovs := 20
	var inventory := {}
	var flags := {}
	var party: Array = [
		{"id": "lord_pilsner", "display_name": "Lord Pilsner", "hp": 45, "max_hp": 45, "bravado": 12,
		 "max_bravado": 12, "offense": 8, "defense": 6, "speed": 5, "charm": 9, "luck": 4, "grit": 3,
		 "skills": []},
		{"id": "chadwick", "display_name": "Chadwick", "hp": 35, "max_hp": 35, "bravado": 12,
		 "max_bravado": 12, "offense": 6, "defense": 3, "speed": 7, "charm": 10, "luck": 4, "grit": 2,
		 "skills": []},
	]

	func add_item(id: String, count: int = 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func _rng(seed_value: int) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	return r


func _texts(core: BattleCore) -> Array:
	return core.events.map(func(ev: Dictionary) -> String: return String(ev["text"]))


## Plays one enemy turn for `e` directly (the bros' turns are not the point here).
func _enemy_turn(core: BattleCore, e: BattleUnit) -> void:
	core._enemy_turn(e)
	core._finish_turn(e)


func test_taproom_mirror_chad_stat_line_matches_option_a() -> void:
	var core := TaproomBattle.build_mirror_chad(FakeState.new(), _rng(1))
	var c: BattleUnit = core.enemies[0]
	assert_eq([c.max_hp, c.offense, c.defense, c.speed, c.charm, c.grit, c.luck], [54, 9, 5, 4, 8, 3, 3])


func test_taproom_mirror_chad_is_not_toughened_like_a_cabinet() -> void:
	var core := TaproomBattle.build_mirror_chad(FakeState.new(), _rng(1))
	assert_eq(core.enemies[0].hp, 54)


func test_taproom_mirror_chad_opens_with_the_leaders_mirror_line() -> void:
	var core := TaproomBattle.build_mirror_chad(FakeState.new(), _rng(1))
	assert_true(_texts(core).has("Mirror Chad: \"You peaked in college. Everything since has been a long, sad encore.\""))
	assert_eq(core.enemies[0].uses["mirror_of"], "lord_pilsner")


func test_taproom_mirror_chad_each_bro_gets_their_own_mirror_line() -> void:
	var lines := {
		"chadwick": "Nobody watches your content. The algorithm hates you. It's personal.",
		"bradley": "You're not the smart one. You're the one who talks like he is."}
	for id in lines:
		var state := FakeState.new()
		state.party[0]["id"] = id
		var core := TaproomBattle.build_mirror_chad(state, _rng(1))
		assert_true(_texts(core).has("Mirror Chad: \"%s\"" % lines[id]), id)


func test_taproom_mirror_chad_barks_turns_one_to_three_verbatim() -> void:
	var core := TaproomBattle.build_mirror_chad(FakeState.new(), _rng(1))
	var c: BattleUnit = core.enemies[0]
	core.events.clear()
	for i in 3:
		_enemy_turn(core, c)
	var t := _texts(core)
	assert_true(t.has("Mirror Chad: \"You ever think maybe you're the problem, bro?\""))
	assert_true(t.has("Mirror Chad: \"Everyone you've annoyed? They remember. They ALL remember.\""))
	assert_true(t.has("Mirror Chad: \"You're exactly like your father. Think about it.\""))


func test_taproom_mirror_chad_third_turn_applies_confused_and_cycle_repeats() -> void:
	var core := TaproomBattle.build_mirror_chad(FakeState.new(), _rng(1))
	var c: BattleUnit = core.enemies[0]
	_enemy_turn(core, c)
	_enemy_turn(core, c)
	for b in core.party:
		assert_false(b.has_status("confused"))
	_enemy_turn(core, c)
	var confused := core.party.filter(func(b: BattleUnit) -> bool: return b.has_status("confused"))
	assert_eq(confused.size(), 1)
	assert_eq(int(confused[0].statuses["confused"]), 2)
	core.events.clear()
	_enemy_turn(core, c)
	assert_true(_texts(core).has("Mirror Chad: \"You ever think maybe you're the problem, bro?\""))


func test_taproom_mirror_chad_never_damages_and_is_immune_to_his_own_statuses() -> void:
	var core := TaproomBattle.build_mirror_chad(FakeState.new(), _rng(2))
	var c: BattleUnit = core.enemies[0]
	for i in 6:
		_enemy_turn(core, c)
	for b in core.party:
		assert_eq(b.hp, b.max_hp)
	assert_false(core._apply_status(c, "confused", 2, 1.0))
	assert_false(core._apply_status(c, "embarrassed", 2, 1.0))


func test_taproom_mirror_chad_win_pays_12_sovs_shard_flag_no_tickets() -> void:
	var state := FakeState.new()
	var core := TaproomBattle.build_mirror_chad(state, _rng(1))
	core.enemies[0].take_damage(54)
	core._enemy_down(core.enemies[0], null)
	core._check_outcome()
	var r := TaproomBattle.settle("mirror_chad", core, state)
	assert_eq(core.outcome, "won")
	assert_eq(state.sovs, 32)
	assert_eq(r["tickets"], 0)
	assert_eq(state.inventory.get("cracked_mirror_shard", 0), 1)
	assert_true(state.flags[TaproomBattle.FLAG_MIRROR_CHAD_DEFEATED])


func test_taproom_wisp_stat_line_is_72_hp_and_not_toughened() -> void:
	var core := TaproomBattle.build_wisp(FakeState.new(), _rng(1))
	var w: BattleUnit = core.enemies[0]
	assert_eq([w.max_hp, w.offense, w.defense, w.speed, w.charm, w.grit, w.luck], [72, 9, 4, 8, 10, 2, 5])


func test_taproom_wisp_phase_thresholds_at_72_hp() -> void:
	var core := TaproomBattle.build_wisp(FakeState.new(), _rng(1))
	var w: BattleUnit = core.enemies[0]
	w.hp = 48   # 66% of 72 is 47.52
	core._check_phase(w)
	assert_eq(w.phase, 1)
	w.hp = 47
	core._check_phase(w)
	assert_eq(w.phase, 2)
	w.hp = 24   # 33% is 23.76
	core._check_phase(w)
	assert_eq(w.phase, 2)
	w.hp = 23
	core._check_phase(w)
	assert_eq(w.phase, 3)


func test_taproom_wisp_phase_one_opens_with_her_line_and_hides_the_illusions() -> void:
	var core := TaproomBattle.build_wisp(FakeState.new(), _rng(1))
	var t := _texts(core)
	assert_true(t.has("Green Fairy Wisp: \"You sought me, and now you've found me. Was it worth it?\""))
	assert_eq(t.filter(func(s: String) -> bool: return s.ends_with("appears!")).size(), 1)
	assert_eq(core.targetable_enemies().size(), 1)


func test_taproom_wisp_splits_into_three_with_exactly_one_real() -> void:
	var core := TaproomBattle.build_wisp(FakeState.new(), _rng(3))
	var w: BattleUnit = core.enemies[0]
	core.events.clear()
	w.hp = 47
	core._check_phase(w)
	assert_true(_texts(core).has("Green Fairy Wisp: \"Which version of yourself would you prefer?\""))
	var live := core.targetable_enemies()
	assert_eq(live.size(), 3)
	assert_eq(live.filter(func(u: BattleUnit) -> bool: return not u.illusion).size(), 1)
	var slots := live.map(func(u: BattleUnit) -> int: return u.slot)
	slots.sort()
	assert_eq(slots, [0, 1, 2])
	var ill: BattleUnit = live.filter(func(u: BattleUnit) -> bool: return u.illusion)[0]
	assert_eq([ill.max_hp, ill.offense, ill.defense, ill.speed], [16, 5, 2, 8])


func test_taproom_wisp_split_gives_no_tell_in_names_or_sprites() -> void:
	var core := TaproomBattle.build_wisp(FakeState.new(), _rng(3))
	core.enemies[0].hp = 47
	core._check_phase(core.enemies[0])
	var bases := core.enemies.map(func(u: BattleUnit) -> String: return u.display_name.substr(0, 17))
	assert_eq(bases, ["Green Fairy Wisp ", "Green Fairy Wisp ", "Green Fairy Wisp "])
	var paths := core.enemies.map(func(u: BattleUnit) -> String: return BattleScreen.enemy_sprite_path(u))
	assert_eq(paths[0], paths[1])
	assert_eq(paths[0], paths[2])


func test_taproom_wisp_illusion_pops_on_any_hit_and_does_not_end_the_fight() -> void:
	var core := TaproomBattle.build_wisp(FakeState.new(), _rng(3))
	core.enemies[0].hp = 47
	core._check_phase(core.enemies[0])
	var ill: BattleUnit = core.enemies[1]
	var rng_hit := _rng(5)
	core._rng = rng_hit
	var tries := 0
	while not ill.is_down() and tries < 50:
		core._hit(core.party[0], ill, 0.7, false, 3)
		tries += 1
	assert_true(ill.is_down())
	assert_eq(core.outcome, "")


func test_taproom_wisp_killing_the_real_one_wins_and_fades_illusions() -> void:
	var core := TaproomBattle.build_wisp(FakeState.new(), _rng(3))
	var w: BattleUnit = core.enemies[0]
	w.hp = 47
	core._check_phase(w)
	w.take_damage(w.hp)
	core._enemy_down(w, null)
	core._check_outcome()
	assert_eq(core.outcome, "won")
	assert_true(core.enemies[1].is_down())


func test_taproom_wisp_phase_three_fades_illusions() -> void:
	var core := TaproomBattle.build_wisp(FakeState.new(), _rng(3))
	var w: BattleUnit = core.enemies[0]
	w.hp = 23
	core._check_phase(w)
	assert_eq(w.phase, 3)
	assert_eq(core.targetable_enemies().size(), 1)


func test_taproom_wisp_confusion_breath_chance_is_40_percent() -> void:
	var core := TaproomBattle.build_wisp(FakeState.new(), _rng(11))
	var w: BattleUnit = core.enemies[0]
	var breath: Dictionary = w.moves.filter(func(m: Dictionary) -> bool: return m["id"] == "confusion_breath")[0]
	var landed := 0
	for i in 500:
		core.party[0].statuses.clear()
		core._move_effects(w, breath, core.party[0])
		if core.party[0].has_status("confused"):
			landed += 1
	assert_almost_eq(float(landed) / 500.0, 0.4, 0.07)


func test_taproom_wisp_the_truth_drains_five_and_leaves_saw_yourself_on_each_hit() -> void:
	var state := FakeState.new()
	var core := TaproomBattle.build_wisp(state, _rng(4))
	var w: BattleUnit = core.enemies[0]
	w.hp = 10   # under 20%
	core._check_phase(w)
	assert_eq(core._forced_move(w)["id"], "the_truth")
	core.events.clear()
	var truth: Dictionary = w.moves.filter(func(m: Dictionary) -> bool: return m["id"] == "the_truth")[0]
	core._wind_up(w, truth)
	assert_false(w.telegraph.is_empty())
	var before := core.party.map(func(b: BattleUnit) -> int: return b.bravado)
	core._rng = _rng(9)
	_enemy_turn(core, w)
	var hit_ids := core.field_hits.map(func(h: Dictionary) -> String: return h["bro"])
	assert_gt(hit_ids.size(), 0)
	for i in core.party.size():
		if hit_ids.has(core.party[i].id):
			assert_eq(core.party[i].bravado, maxi(before[i] - 5, 0))
	core._forced_move(w)
	assert_true(w.uses.has("the_truth"))   # once only


func test_taproom_wisp_leaves_after_round_six_and_counts_as_survived() -> void:
	var state := FakeState.new()
	var core := TaproomBattle.build_wisp(state, _rng(1))
	core.round_number = 5
	core._new_round()
	assert_eq(core.outcome, "")
	assert_eq(core.round_number, 6)
	core._new_round()
	assert_eq(core.outcome, "survived")
	var r := TaproomBattle.settle("green_fairy_wisp", core, state)
	assert_true(state.flags[TaproomBattle.FLAG_WISP_SURVIVED])
	assert_false(state.flags.has(TaproomBattle.FLAG_WISP_DEFEATED))
	assert_eq(r["sovs"], 0)
	assert_eq(state.inventory.size(), 0)


func test_taproom_wisp_win_pays_25_sovs_essence_flag_no_tickets() -> void:
	var state := FakeState.new()
	var core := TaproomBattle.build_wisp(state, _rng(1))
	var w: BattleUnit = core.enemies[0]
	w.take_damage(72)
	core._enemy_down(w, null)
	core._check_outcome()
	var r := TaproomBattle.settle("green_fairy_wisp", core, state)
	assert_eq(core.outcome, "won")
	assert_eq(state.sovs, 45)
	assert_eq(r["tickets"], 0)
	assert_eq(state.inventory.get("green_fairy_essence", 0), 1)
	assert_true(state.flags[TaproomBattle.FLAG_WISP_DEFEATED])


func test_taproom_absinthe_lager_price_is_recorded_as_12_sovs() -> void:
	assert_eq(TaproomBattle.lager_price(), 12)


# --- no running from the Taproom fights; Reality Anchor in battle (author rulings 2026-11-12) -------

func _anchor_state() -> FakeState:
	var st := FakeState.new()
	FieldStatus.grant_reality_anchor(st, "lord_pilsner")
	FieldStatus.grant_reality_anchor(st, "chadwick")
	return st


func _confused_blocks(state: FakeState, tries: int) -> int:
	var core := TaproomBattle.build_mirror_chad(state, _rng(77))
	var blocked := 0
	for i in tries:
		var bro: BattleUnit = core.party[0]
		bro.statuses.erase("confused")
		if not core._apply_status(bro, "confused", 2, 1.0):
			blocked += 1
	return blocked


func test_taproom_run_is_refused_in_both_fights() -> void:
	for fight in [TaproomBattle.MIRROR_CHAD, TaproomBattle.WISP]:
		var core := TaproomBattle.build(fight, FakeState.new(), _rng(3))
		core.start()
		assert_false(core.can_run, fight)
		core.run_away()
		assert_ne(core.outcome, "ran", fight)


func test_arcade_cabinet_fight_still_allows_run() -> void:
	var core := ArcadeBattle.build("cabinet_kebab_kombat", FakeState.new(), _rng(1))
	assert_true(core.can_run)


func test_taproom_reality_anchor_blocks_confused_about_ten_percent() -> void:
	var blocked := _confused_blocks(_anchor_state(), 2000)
	assert_between(blocked, 140, 260)


func test_taproom_without_reality_anchor_confused_is_never_blocked() -> void:
	assert_eq(_confused_blocks(FakeState.new(), 500), 0)
