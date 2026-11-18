extends GutTest
## Each bro's first signature move (Eurobound-g0jr; author, Eurobound Desk Eurobound-g0jr-q2,
## 2026-11-16, "Approve as proposed"; docs/superpowers/specs/2026-11-16-eurobound-g0jr-numbers-proposal.md):
## Keg Smash (Bradley), Like & Hype (Chadwick), Beer Belly Bash (Lord Pilsner).


func after_each() -> void:
	AbilityTable.reset()
	StatusTable.reset()


func _abilities() -> Dictionary:
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string("res://assets/data/skills/party_abilities.json"))
	return Dictionary(Dictionary(parsed)["abilities"])


func _party() -> Dictionary:
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string("res://assets/data/party/party_members.json"))
	return Dictionary(Dictionary(parsed)["party_members"])


func _bro(id: String, offense: int, max_bravado: int, speed: int, luck: int = 0) -> BattleUnit:
	return BattleUnit.from_member({"id": id, "display_name": id, "max_hp": 40, "hp": 40,
		"max_bravado": max_bravado, "bravado": max_bravado, "offense": offense, "defense": 2,
		"speed": speed, "luck": luck, "grit": 0, "charm": 4, "skills": []})


## A villain with no moves: it just hesitates on its turns.
func _villain(defense: int = 6, hp: int = 500) -> BattleUnit:
	return BattleUnit.from_enemy("croc", {"display_name": "croc", "max_hp": hp, "offense": 9,
		"defense": defense, "speed": 1, "luck": 0, "ticket_reward": 5}, {})


func _core(bros: Array, villains: Array, seed_value: int = 1) -> BattleCore:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	var core := BattleCore.new(r)
	for b in bros:
		core.party.append(b)
	for v in villains:
		core.add_enemy(v)
	core.start()
	core.step()
	return core


## The first seed whose RNG passes `pred` (the core's first rolls are the ones under test).
func _seed_where(pred: Callable) -> int:
	for s in range(1, 2000):
		var r := RandomNumberGenerator.new()
		r.seed = s
		if pred.call(r):
			return s
	return -1


## Plays round after round until `who` needs a command again (the villain only hesitates).
func _next_turn_of(core: BattleCore, who: BattleUnit) -> void:
	for i in 20:
		core.step()
		if core.current() == who and core.needs_input():
			return


# --- shipped numbers ---------------------------------------------------------------------------

func test_shipped_keg_smash_numbers() -> void:
	var k: Dictionary = _abilities()["keg_smash"]
	assert_eq(k["display_name"], "Keg Smash")
	assert_eq(int(k["bravado_cost"]), 5)
	assert_almost_eq(float(k["power_multiplier"]), 2.5, 0.0001)
	assert_eq(k["spoken"], false, "a smash, not a line: Cottonmouth does not block it")
	assert_eq(k["is_ultimate"], false)


func test_shipped_like_and_hype_numbers() -> void:
	var h: Dictionary = _abilities()["like_and_hype"]
	assert_eq(h["display_name"], "Like & Hype")
	assert_eq(int(h["bravado_cost"]), 4)
	assert_eq(h["spoken"], true, "Bro-Mancy is motivational yelling: Cottonmouth blocks it")
	assert_eq(h["target"], "other_bro")
	assert_eq(h["ally_status"]["status"], "gains_bro")
	assert_eq(int(h["ally_status"]["turns"]), 3)
	assert_almost_eq(float(h["viral"]["chance"]), 0.25, 0.0001)
	assert_eq(int(h["viral"]["crit_bonus"]), 10)
	assert_eq(int(h["viral"]["turns"]), 3)
	assert_eq(h["is_ultimate"], false)


func test_shipped_beer_belly_bash_numbers() -> void:
	var b: Dictionary = _abilities()["beer_belly_bash"]
	assert_eq(b["display_name"], "Beer Belly Bash")
	assert_eq(int(b["bravado_cost"]), 3)
	assert_almost_eq(float(b["power_multiplier"]), 1.0, 0.0001)
	assert_eq(b["spoken"], false)
	assert_eq(b["inflict"]["status"], "stun")
	assert_almost_eq(float(b["inflict"]["chance"]), 0.4, 0.0001)
	assert_eq(int(b["inflict"]["turns"]), 1)
	assert_eq(int(b["cooldown_rounds"]), 3)
	assert_eq(b["is_ultimate"], false)


func test_shipped_starting_kits() -> void:
	var p := _party()
	assert_eq(Array(p["bradley"]["skills"]).has("keg_smash"), true)
	assert_eq(Array(p["chadwick"]["skills"]).has("like_and_hype"), true)
	assert_eq(Array(p["lord_pilsner"]["skills"]).has("beer_belly_bash"), true)
	assert_eq(Array(p["lord_pilsner"]["skills"]).has("roast_line"), true, "Roast Line stays")


func test_no_battle_text_is_written_for_the_new_moves() -> void:
	# The Writers' Room writes these lines later; until then the field is null with a note.
	var a := _abilities()
	for id in ["keg_smash", "like_and_hype", "beer_belly_bash"]:
		assert_eq(a[id]["battle_text"], null, id)
		assert_true(Dictionary(a[id].get("_pending", {})).has("battle_text"), id)


# --- Keg Smash ---------------------------------------------------------------------------------

func test_keg_smash_pays_five_first_then_hits_at_two_and_a_half() -> void:
	# Bradley 12 Off, 14 Bravado. He pays 5 first (14 -> 9, Mid +3): (12 + 3 - 6) x 2.5 = 22.5.
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool:
		var hit := r.randf() < 0.95
		r.randi_range(-2, 2)
		return hit and r.randf() * 100.0 >= 1.0)
	var bradley := _bro("bradley", 12, 14, 9)
	var croc := _villain(6)
	var core := _core([bradley], [croc], s)
	# Act
	var used := core.use_skill(_abilities()["keg_smash"], croc)
	# Assert
	assert_true(used)
	assert_eq(bradley.bravado, 9)
	var dealt := 500 - croc.hp
	assert_between(dealt, 21, 25)


func test_keg_smash_with_no_battle_text_says_the_move_name() -> void:
	var bradley := _bro("bradley", 12, 14, 9)
	var croc := _villain(6)
	var core := _core([bradley], [croc])
	core.events.clear()
	core.use_skill(_abilities()["keg_smash"], croc)
	assert_eq(String(core.events[0]["text"]), "bradley uses Keg Smash!")


# --- Like & Hype -------------------------------------------------------------------------------

func test_like_and_hype_gives_another_bro_gains_bro_for_three_turns() -> void:
	var chadwick := _bro("chadwick", 6, 20, 9)
	var bradley := _bro("bradley", 12, 14, 8)
	var croc := _villain()
	var core := _core([chadwick, bradley], [croc])
	assert_eq(core.current(), chadwick)
	var hp_before := croc.hp
	# Act
	var used := core.use_skill(_abilities()["like_and_hype"], bradley)
	# Assert
	assert_true(used)
	assert_eq(chadwick.bravado, 16)
	assert_eq(int(bradley.statuses.get("gains_bro", 0)), 3)
	assert_eq(croc.hp, hp_before, "no damage")


func test_like_and_hype_cannot_target_chadwick_or_a_villain() -> void:
	var chadwick := _bro("chadwick", 6, 20, 9)
	var bradley := _bro("bradley", 12, 14, 8)
	var croc := _villain()
	var core := _core([chadwick, bradley], [croc])
	var hype: Dictionary = _abilities()["like_and_hype"]
	assert_false(core.use_skill(hype, chadwick), "not on himself")
	assert_false(core.use_skill(hype, croc), "not on a villain")
	assert_eq(chadwick.bravado, 20, "nothing paid")
	assert_eq(core.skill_targets(hype), [bradley])


func test_like_and_hype_recast_resets_to_three_and_does_not_stack() -> void:
	var chadwick := _bro("chadwick", 6, 20, 9)
	var bradley := _bro("bradley", 12, 14, 8)
	var core := _core([chadwick, bradley], [_villain()])
	bradley.statuses["gains_bro"] = 1
	core.use_skill(_abilities()["like_and_hype"], bradley)
	assert_eq(int(bradley.statuses["gains_bro"]), 3)


func test_like_and_hype_viral_gives_ten_crit_for_three_turns() -> void:
	var chadwick := _bro("chadwick", 6, 20, 9)
	var bradley := _bro("bradley", 12, 14, 8)
	var core := _core([chadwick, bradley], [_villain()])
	var hype: Dictionary = _abilities()["like_and_hype"].duplicate(true)
	hype["viral"]["chance"] = 1.0
	core.use_skill(hype, bradley)
	assert_eq(bradley.own_crit_bonus, 10.0)
	assert_eq(bradley.own_crit_turns, 3)


func test_like_and_hype_no_viral_gives_no_crit() -> void:
	var chadwick := _bro("chadwick", 6, 20, 9)
	var bradley := _bro("bradley", 12, 14, 8)
	var core := _core([chadwick, bradley], [_villain()])
	var hype: Dictionary = _abilities()["like_and_hype"].duplicate(true)
	hype["viral"]["chance"] = 0.0
	core.use_skill(hype, bradley)
	assert_eq(bradley.own_crit_bonus, 0.0)
	assert_eq(bradley.own_crit_turns, 0)


func test_viral_crit_bonus_counts_down_on_the_bearers_turns() -> void:
	var bradley := _bro("bradley", 12, 14, 8)
	bradley.own_crit_bonus = 10.0
	bradley.own_crit_turns = 3
	bradley.end_own_turn()
	bradley.end_own_turn()
	assert_eq(bradley.own_crit_bonus, 10.0)
	bradley.end_own_turn()
	assert_eq(bradley.own_crit_turns, 0)
	assert_eq(bradley.own_crit_bonus, 0.0)


func test_viral_crit_bonus_lands_smaaaash() -> void:
	# Luck 0 against Grit 0 is a 1% crit at Mid; +100 from a viral bonus makes every hit crit.
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() < 0.95)
	var bradley := _bro("bradley", 12, 14, 9)
	bradley.bravado = 7
	bradley.own_crit_bonus = 100.0
	bradley.own_crit_turns = 1
	var core := _core([bradley], [_villain(0)], s)
	core.events.clear()
	core.attack(core.enemies[0])
	var texts := core.events.map(func(e: Dictionary) -> String: return String(e["text"]))
	assert_true(texts.any(func(t: String) -> bool: return t.begins_with("SMAAAASH!")), str(texts))


# --- Beer Belly Bash ---------------------------------------------------------------------------

func test_beer_belly_bash_costs_three_and_hits_at_one() -> void:
	# Pilsner 8 Off, 12 Bravado: pays 3 (12 -> 9, High +6): (8 + 6 - 6) x 1.0 = 8.
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool:
		var hit := r.randf() < 0.95
		r.randi_range(-2, 2)
		return hit and r.randf() * 100.0 >= 10.0)
	var pilsner := _bro("lord_pilsner", 8, 12, 9)
	var croc := _villain(6)
	var core := _core([pilsner], [croc], s)
	var bash: Dictionary = _abilities()["beer_belly_bash"].duplicate(true)
	bash["inflict"]["chance"] = 0.0
	assert_true(core.use_skill(bash, croc))
	assert_eq(pilsner.bravado, 9)
	assert_between(500 - croc.hp, 6, 10)
	assert_false(croc.statuses.has("stun"))


func test_beer_belly_bash_stun_makes_the_villain_lose_its_next_turn() -> void:
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() < 0.95)
	var pilsner := _bro("lord_pilsner", 8, 12, 9)
	var croc := _villain(6)
	var core := _core([pilsner], [croc], s)
	var bash: Dictionary = _abilities()["beer_belly_bash"].duplicate(true)
	bash["inflict"]["chance"] = 1.0
	core.use_skill(bash, croc)
	assert_eq(int(croc.statuses.get("stun", 0)), 1)
	core.events.clear()
	core.step()   # the villain's turn
	var texts := core.events.map(func(e: Dictionary) -> String: return String(e["text"]))
	assert_true(texts.has("croc is stunned."), str(texts))
	assert_false(croc.statuses.has("stun"), "one turn only")


func test_beer_belly_bash_has_a_three_round_cooldown() -> void:
	var pilsner := _bro("lord_pilsner", 8, 12, 9)
	var core := _core([pilsner], [_villain()])
	var bash: Dictionary = _abilities()["beer_belly_bash"]
	assert_true(core.use_skill(bash, core.enemies[0]), "round 1")
	_next_turn_of(core, pilsner)
	assert_eq(core.round_number, 2)
	assert_false(core.can_use_skill(pilsner, bash), "round 2: cooling down")
	core.attack(core.enemies[0])
	_next_turn_of(core, pilsner)
	assert_false(core.can_use_skill(pilsner, bash), "round 3: cooling down")
	core.attack(core.enemies[0])
	_next_turn_of(core, pilsner)
	assert_eq(core.round_number, 4)
	assert_true(core.can_use_skill(pilsner, bash), "round 4: ready")


# --- locks -------------------------------------------------------------------------------------

func test_cottonmouth_blocks_like_and_hype_only() -> void:
	var bro := _bro("chadwick", 6, 20, 9)
	bro.statuses["cottonmouth"] = -1
	var core := _core([bro], [_villain()])
	var a := _abilities()
	assert_false(core.can_use_skill(bro, a["like_and_hype"]))
	assert_true(core.can_use_skill(bro, a["keg_smash"]))
	assert_true(core.can_use_skill(bro, a["beer_belly_bash"]))


func test_embarrassed_locks_all_three() -> void:
	var bro := _bro("chadwick", 6, 20, 9)
	bro.statuses["embarrassed"] = 2
	var core := _core([bro], [_villain()])
	var a := _abilities()
	for id in ["keg_smash", "like_and_hype", "beer_belly_bash"]:
		assert_false(core.can_use_skill(bro, a[id]), id)
