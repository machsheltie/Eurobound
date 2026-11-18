extends GutTest
## Combos, the starter set (Eurobound-rl4c; author, Eurobound Desk Eurobound-rl4c-q2, 2026-11-16,
## "Approve as proposed"; docs/superpowers/specs/2026-11-16-eurobound-rl4c-numbers-proposal.md):
## Beeramid, Like & Subscribe, Who Flexed Harder?


func after_each() -> void:
	AbilityTable.reset()


func _combos() -> Dictionary:
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string("res://assets/data/skills/combos.json"))
	return Dictionary(Dictionary(parsed)["combos"])


## v26 sheets. Speeds put the bros first, in the order given, then the villains.
func _pilsner(speed: int = 9) -> BattleUnit:
	return BattleUnit.from_member({"id": "lord_pilsner", "display_name": "Lord Pilsner", "max_hp": 45,
		"max_bravado": 12, "offense": 8, "defense": 6, "speed": speed, "luck": 4, "grit": 3, "charm": 9, "skills": []})


func _chadwick(speed: int = 9) -> BattleUnit:
	return BattleUnit.from_member({"id": "chadwick", "display_name": "Chadwick", "max_hp": 35,
		"max_bravado": 20, "offense": 6, "defense": 3, "speed": speed, "luck": 6, "grit": 2, "charm": 10, "skills": []})


func _bradley(speed: int = 10) -> BattleUnit:
	return BattleUnit.from_member({"id": "bradley", "display_name": "Bradley", "max_hp": 30,
		"max_bravado": 14, "offense": 12, "defense": 2, "speed": speed, "luck": 5, "grit": 3, "charm": 4, "skills": []})


func _villain(id: String = "croc", defense: int = 6, hp: int = 500) -> BattleUnit:
	return BattleUnit.from_enemy(id, {"display_name": id, "max_hp": hp, "offense": 9,
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


## The first seed whose RNG passes `pred` (the combo's success roll is the core's first roll).
func _seed_where(pred: Callable) -> int:
	for s in range(1, 4000):
		var r := RandomNumberGenerator.new()
		r.seed = s
		if pred.call(r):
			return s
	return -1


func _texts(core: BattleCore) -> Array:
	return core.events.map(func(e: Dictionary) -> String: return String(e["text"]))


# --- shipped numbers ---------------------------------------------------------------------------

func test_battle_combos_rules_match_the_ruling() -> void:
	assert_eq(BattleRulings.COMBO_SUCCESS, {"high": 0.8, "mid": 0.6, "low": 0.4})
	assert_eq(BattleRulings.COMBO_SELF_DAMAGE, 5)
	assert_eq(BattleRulings.COMBO_BRAVADO_LOSS, 3)
	assert_eq(BattleRulings.COMBO_EMBARRASSED_TURNS, 2)


func test_battle_combos_shipped_starter_set() -> void:
	var c := _combos()
	assert_eq(c.keys().size(), 3)
	var bee: Dictionary = c["beeramid"]
	assert_eq(bee["display_name"], "Beeramid")
	assert_eq(Array(bee["participants"]), ["bradley", "lord_pilsner"])
	assert_eq(bee["striker"], "bradley")
	assert_eq(Array(bee["requires_high"]), ["lord_pilsner"])
	assert_eq(bee["target"], "all_enemies")
	assert_almost_eq(float(bee["multiplier"]), 3.0, 0.0001)
	assert_eq(bee["inflict"]["status"], "stun")
	assert_eq(int(bee["inflict"]["turns"]), 1)
	assert_eq(int(bee["bravado_each"]), 2)
	assert_eq(Array(bee["backfire"]["self_damage"]), ["bradley", "lord_pilsner"])
	assert_eq(Array(bee["backfire"]["embarrassed"]), ["bradley", "lord_pilsner"])
	var ls: Dictionary = c["like_and_subscribe"]
	assert_eq(ls["display_name"], "Like & Subscribe")
	assert_eq(Array(ls["participants"]), ["chadwick", "bradley"])
	assert_eq(ls["striker"], "bradley")
	assert_almost_eq(float(ls["multiplier"]), 2.0, 0.0001)
	assert_almost_eq(float(ls["viral"]["chance"]), 0.25, 0.0001)
	assert_almost_eq(float(ls["viral"]["multiplier"]), 4.0, 0.0001)
	assert_eq(int(ls["viral"]["bravado_each_min"]), 1)
	assert_eq(int(ls["viral"]["bravado_each_max"]), 3)
	assert_eq(Array(ls["backfire"]["bravado_loss"]), ["bradley"])
	var wf: Dictionary = c["who_flexed_harder"]
	assert_eq(wf["display_name"], "Who Flexed Harder?")
	assert_eq(Array(wf["participants"]), ["bradley", "chadwick"])
	assert_eq(wf["striker"], "winner")
	assert_almost_eq(float(wf["multiplier"]), 2.5, 0.0001)
	assert_eq(int(wf["contest"]["winner_bravado"]), 3)
	assert_eq(int(wf["contest"]["loser_bravado"]), -3)
	assert_eq(Array(wf["backfire"]["embarrassed"]), ["bradley", "chadwick"])
	for id in c.keys():
		assert_eq(c[id]["battle_text"], null, "%s: the Writers' Room writes the line" % id)


# --- the roll ----------------------------------------------------------------------------------

func test_battle_combos_success_chance_reads_combined_bravado_tier() -> void:
	var bradley := _bradley()
	var pilsner := _pilsner()
	var core := _core([bradley, pilsner], [_villain()])
	assert_almost_eq(core.combo_chance("beeramid"), 0.8, 0.0001, "26/26: High")
	bradley.bravado = 4
	pilsner.bravado = 8
	assert_almost_eq(core.combo_chance("beeramid"), 0.6, 0.0001, "12/26: Mid")
	bradley.bravado = 0
	pilsner.bravado = 8
	assert_almost_eq(core.combo_chance("beeramid"), 0.4, 0.0001, "8/26: Low")


# --- who can start one -------------------------------------------------------------------------

func test_battle_combos_ready_when_partner_has_not_acted() -> void:
	var core := _core([_bradley(), _pilsner()], [_villain()])
	assert_true(core.can_combo("beeramid"))
	assert_true(core.available_combos().has("beeramid"))


func test_battle_combos_not_ready_once_the_partner_has_acted() -> void:
	# Pilsner first this time; he attacks, then Bradley cannot pull him into a combo.
	var core := _core([_pilsner(12), _bradley(9)], [_villain()])
	core.attack(core.enemies[0])
	core.step()
	assert_eq(core.current().id, "bradley")
	assert_false(core.can_combo("beeramid"))


func test_battle_combos_embarrassed_or_stunned_partner_cannot_join() -> void:
	var bradley := _bradley()
	var pilsner := _pilsner()
	var core := _core([bradley, pilsner], [_villain()])
	pilsner.statuses["embarrassed"] = 2
	assert_false(core.can_combo("beeramid"), "Embarrassed partner")
	pilsner.statuses = {"stun": 1}
	assert_false(core.can_combo("beeramid"), "Stunned partner")
	pilsner.statuses = {}
	bradley.statuses["embarrassed"] = 2
	assert_false(core.can_combo("beeramid"), "Embarrassed starter")


func test_battle_combos_beeramid_needs_pilsner_at_high() -> void:
	var pilsner := _pilsner()
	var core := _core([_bradley(), pilsner], [_villain()])
	pilsner.bravado = 7   # 7 of 12: Mid
	assert_false(core.can_combo("beeramid"))


func test_battle_combos_only_a_participant_can_start_one() -> void:
	var core := _core([_bradley(), _pilsner()], [_villain()])
	assert_false(core.can_combo("like_and_subscribe"), "no Chadwick in this fight")


func test_battle_combos_spend_the_partners_turn() -> void:
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() < 0.8)
	var bradley := _bradley()
	var pilsner := _pilsner()
	var core := _core([bradley, pilsner], [_villain()], s)
	assert_true(core.use_combo("beeramid", null))
	assert_false(core.turn_order().has(pilsner), "Pilsner's slot is gone from the strip")
	core.step()
	assert_ne(core.current(), pilsner, "no command for Pilsner this round")
	assert_eq(core.round_number, 1)


# --- Beeramid ----------------------------------------------------------------------------------

func test_battle_combos_beeramid_success_hits_every_enemy_stuns_and_pays_two() -> void:
	# Bradley at High: (12 + 7 - 6) x 3 = 39 to each villain.
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool:
		if r.randf() >= 0.8:
			return false
		r.randi_range(-2, 2)
		return r.randf() * 100.0 >= 30.0)
	var bradley := _bradley()
	var pilsner := _pilsner()
	bradley.bravado = 12
	pilsner.bravado = 10
	var a := _villain("swap_a")
	var b := _villain("swap_b")
	var core := _core([bradley, pilsner], [a, b], s)
	assert_true(core.use_combo("beeramid", null))
	assert_between(500 - a.hp, 30, 82, "a")
	assert_between(500 - b.hp, 30, 82, "b")
	assert_eq(int(a.statuses.get("stun", 0)), 1)
	assert_eq(int(b.statuses.get("stun", 0)), 1)
	assert_eq(bradley.bravado, 14)
	assert_eq(pilsner.bravado, 12)


func test_battle_combos_beeramid_first_hit_is_three_times_bradleys_attack() -> void:
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool:
		if r.randf() >= 0.8:
			return false
		r.randi_range(-2, 2)
		return r.randf() * 100.0 >= 30.0)
	var core := _core([_bradley(), _pilsner()], [_villain()], s)
	core.use_combo("beeramid", null)
	assert_between(500 - core.enemies[0].hp, 37, 41)


func test_battle_combos_beeramid_backfire_hurts_and_embarrasses_both() -> void:
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() >= 0.8)
	var bradley := _bradley()
	var pilsner := _pilsner()
	var croc := _villain()
	var core := _core([bradley, pilsner], [croc], s)
	core.use_combo("beeramid", null)
	core.step()   # Pilsner's spent turn ends with the usual countdown too
	assert_eq(croc.hp, 500)
	assert_eq(bradley.hp, 25)
	assert_eq(pilsner.hp, 40)
	assert_eq(int(bradley.statuses.get("embarrassed", 0)), 2, "Embarrassed for his next 2 turns")
	assert_eq(int(pilsner.statuses.get("embarrassed", 0)), 2)


# --- Like & Subscribe --------------------------------------------------------------------------

func test_battle_combos_like_and_subscribe_success_is_double_bradleys_attack() -> void:
	# Bradley at High: (12 + 7 - 6) x 2 = 26.
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool:
		if r.randf() >= 0.8 or r.randf() < 0.25:
			return false
		r.randi_range(-2, 2)
		return r.randf() * 100.0 >= 30.0)
	var croc := _villain()
	var core := _core([_chadwick(11), _bradley()], [croc], s)
	assert_true(core.use_combo("like_and_subscribe", croc))
	assert_between(500 - croc.hp, 24, 28)


func test_battle_combos_like_and_subscribe_viral_is_four_times_and_feeds_every_bro() -> void:
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() < 0.8 and r.randf() < 0.25)
	var chadwick := _chadwick(11)
	var bradley := _bradley()
	var pilsner := _pilsner(3)
	chadwick.bravado = 14
	bradley.bravado = 10
	pilsner.bravado = 5
	var croc := _villain()
	var core := _core([chadwick, bradley, pilsner], [croc], s)
	core.use_combo("like_and_subscribe", croc)
	# Bradley 10/14 is High (+7): (12 + 7 - 6) x 4 = 52, never a SMAAAASH on top.
	assert_between(500 - croc.hp, 50, 54)
	assert_false(_texts(core).any(func(t: String) -> bool: return t.begins_with("SMAAAASH")))
	assert_between(chadwick.bravado, 15, 17)
	assert_between(bradley.bravado, 11, 13)
	assert_between(pilsner.bravado, 6, 8)


func test_battle_combos_like_and_subscribe_backfire_costs_bradley_three() -> void:
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() >= 0.8)
	var chadwick := _chadwick(11)
	var bradley := _bradley()
	var croc := _villain()
	var core := _core([chadwick, bradley], [croc], s)
	core.use_combo("like_and_subscribe", croc)
	assert_eq(croc.hp, 500, "the attack fizzles")
	assert_eq(bradley.bravado, 11)
	assert_eq(chadwick.bravado, 20)


# --- Who Flexed Harder? ------------------------------------------------------------------------

func test_battle_combos_who_flexed_harder_winner_hits_and_gains_loser_pays() -> void:
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() < 0.8)
	var bradley := _bradley()
	var chadwick := _chadwick()
	var croc := _villain()
	var core := _core([bradley, chadwick], [croc], s)
	bradley.bravado = 10
	chadwick.bravado = 14
	assert_true(core.use_combo("who_flexed_harder", croc))
	var won_b := bradley.bravado == 13 and chadwick.bravado == 11
	var won_c := chadwick.bravado == 17 and bradley.bravado == 7
	assert_true(won_b or won_c, "B %d C %d" % [bradley.bravado, chadwick.bravado])
	assert_lt(croc.hp, 500)


func test_battle_combos_who_flexed_harder_picks_by_crit_share() -> void:
	# Bradley 15 (Luck 5 + 10 at High), Chadwick 16 (Luck 6 + 10): Bradley wins 15/31 of rolls.
	var core := _core([_bradley(), _chadwick()], [_villain()])
	assert_almost_eq(core.flex_share(core.party[0], core.party[1]), 15.0 / 31.0, 0.0001)


func test_battle_combos_who_flexed_harder_backfire_embarrasses_both() -> void:
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() >= 0.8)
	var bradley := _bradley()
	var chadwick := _chadwick()
	var croc := _villain()
	var core := _core([bradley, chadwick], [croc], s)
	core.use_combo("who_flexed_harder", croc)
	core.step()   # Chadwick's spent turn
	assert_eq(croc.hp, 500)
	assert_eq(int(bradley.statuses.get("embarrassed", 0)), 2)
	assert_eq(int(chadwick.statuses.get("embarrassed", 0)), 2)
