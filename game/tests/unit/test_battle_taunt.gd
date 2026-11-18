extends GutTest
## Taunt, Bradley's counter-brag and the venue beat (Eurobound-wuyu; author, Eurobound Desk
## Eurobound-wuyu-q2, 2026-11-16, "Approve as proposed";
## docs/superpowers/specs/2026-11-16-eurobound-wuyu-numbers-proposal.md).


func after_each() -> void:
	AbilityTable.reset()


func _bro(id: String, speed: int, charm: int = 4, skills: Array = []) -> BattleUnit:
	return BattleUnit.from_member({"id": id, "display_name": id, "max_hp": 40, "hp": 40,
		"max_bravado": 12, "bravado": 12, "offense": 8, "defense": 2, "speed": speed, "luck": 0,
		"grit": 0, "charm": charm, "skills": skills})


## A villain whose only move is `move` (weight 100).
func _villain(move: Dictionary, grit: int = 0) -> BattleUnit:
	var m := move.duplicate(true)
	m["id"] = "jab"
	m["name"] = "Jab"
	m["weight"] = 100
	return BattleUnit.from_enemy("croc", {"display_name": "croc", "max_hp": 500, "offense": 9,
		"defense": 0, "speed": 5, "luck": 0, "ticket_reward": 5}, {"grit": grit, "moves": [m]})


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


func _seed_where(pred: Callable) -> int:
	for s in range(1, 4000):
		var r := RandomNumberGenerator.new()
		r.seed = s
		if pred.call(r):
			return s
	return -1


func _counter_brag(chance: float) -> Dictionary:
	return {"bro_do_you_even_lift": {"display_name": "Bro, Do You Even Lift?", "kind": "counter_brag",
		"bravado_cost": 0, "trigger": "enemy_bravado_drain", "blocked_by_status": ["embarrassed", "stun"],
		"chance_by_tier": {"high": chance, "mid": chance, "low": chance}}}


# --- Taunt: numbers ----------------------------------------------------------------------------

func test_battle_taunt_chance_is_fifty_plus_five_a_point_clamped() -> void:
	assert_almost_eq(BattleRulings.taunt_pct(10, 6), 70.0, 0.001, "Chadwick on Croc Monsieur")
	assert_almost_eq(BattleRulings.taunt_pct(4, 8), 30.0, 0.001, "Bradley on Shish Kahn")
	assert_almost_eq(BattleRulings.taunt_pct(9, 2), 85.0, 0.001, "Pilsner on a Hatchback")
	assert_almost_eq(BattleRulings.taunt_pct(20, 0), 90.0, 0.001, "ceiling")
	assert_almost_eq(BattleRulings.taunt_pct(0, 20), 10.0, 0.001, "floor")


# --- Taunt: the minor action -------------------------------------------------------------------

func test_battle_taunt_uses_the_minor_action_and_costs_no_bravado() -> void:
	var chad := _bro("chadwick", 9, 10)
	var core := _core([chad], [_villain({"target": "one", "type": "physical"})])
	assert_true(core.can_taunt())
	assert_true(core.taunt(core.enemies[0]))
	assert_eq(chad.bravado, 12)
	assert_false(core.can_taunt(), "one minor action a turn")
	assert_false(core.can_flex(), "Taunt took the minor action")
	assert_true(core.needs_input(), "the main action is still to come")


func test_battle_taunt_embarrassed_bro_cannot_taunt_but_can_flex() -> void:
	var chad := _bro("chadwick", 9, 10)
	chad.statuses["embarrassed"] = 2
	var core := _core([chad], [_villain({"target": "one", "type": "physical"})])
	assert_false(core.can_taunt())
	assert_false(core.taunt(core.enemies[0]))
	assert_true(core.can_flex())


func test_battle_taunt_lands_on_the_roll() -> void:
	# Chadwick Charm 10 against Grit 6: 70%.
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() * 100.0 < 70.0)
	var core := _core([_bro("chadwick", 9, 10)], [_villain({"target": "one", "type": "physical"}, 6)], s)
	core.taunt(core.enemies[0])
	assert_eq(core.enemies[0].taunted_by, "chadwick")


func test_battle_taunt_misses_on_the_roll() -> void:
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() * 100.0 >= 70.0)
	var core := _core([_bro("chadwick", 9, 10)], [_villain({"target": "one", "type": "physical"}, 6)], s)
	core.taunt(core.enemies[0])
	assert_eq(core.enemies[0].taunted_by, "")


func test_battle_taunt_latest_taunt_wins() -> void:
	# Chadwick's Taunt is already on the villain; Pilsner's lands on top of it.
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool: return r.randf() * 100.0 < 90.0)
	var pils := _bro("lord_pilsner", 9, 30)
	var chad := _bro("chadwick", 8, 30)
	var core := _core([pils, chad], [_villain({"target": "one", "type": "physical"})], s)
	core.enemies[0].taunted_by = "chadwick"
	core.taunt(core.enemies[0])
	assert_eq(core.enemies[0].taunted_by, "lord_pilsner")


# --- Taunt: the pull ---------------------------------------------------------------------------

func test_battle_taunt_pulls_a_single_target_move_onto_the_taunter() -> void:
	var pils := _bro("lord_pilsner", 9)
	var chad := _bro("chadwick", 9)
	var brad := _bro("bradley", 9)
	var croc := _villain({"target": "lowest_hp", "type": "physical"})
	var core := _core([pils, chad, brad], [croc])
	brad.hp = 5
	croc.taunted_by = "lord_pilsner"
	for i in 10:
		var t := core._move_targets(croc, croc.moves[0])
		assert_eq(t, [pils])


func test_battle_taunt_leaves_hit_everyone_moves_alone() -> void:
	var pils := _bro("lord_pilsner", 9)
	var chad := _bro("chadwick", 9)
	var croc := _villain({"target": "all", "type": "physical"})
	var core := _core([pils, chad], [croc])
	croc.taunted_by = "lord_pilsner"
	assert_eq(core._move_targets(croc, croc.moves[0]).size(), 2)


func test_battle_taunt_leaves_named_bro_moves_alone() -> void:
	var pils := _bro("lord_pilsner", 9)
	var chad := _bro("chadwick", 9)
	var croc := _villain({"target": "prefer_or_lowest_hp", "prefer": "chadwick", "type": "physical"})
	var core := _core([pils, chad], [croc])
	croc.taunted_by = "lord_pilsner"
	assert_eq(core._move_targets(croc, croc.moves[0]), [chad])
	var dip := _villain({"target": "one", "type": "none", "always_on": "chadwick"})
	core.add_enemy(dip)
	dip.taunted_by = "lord_pilsner"
	var seen := {}
	for i in 30:
		seen[core._move_targets(dip, dip.moves[0])[0].id] = true
	assert_true(seen.has("chadwick"), "Buy the Dip-style moves still pick freely")


func test_battle_taunt_wears_off_after_the_villains_next_turn() -> void:
	var pils := _bro("lord_pilsner", 9)
	var croc := _villain({"target": "one", "type": "physical"})
	var core := _core([pils], [croc])
	croc.taunted_by = "lord_pilsner"
	core.attack(croc)
	core.step()   # the villain's turn
	assert_eq(croc.taunted_by, "")


func test_battle_taunt_ignored_when_the_taunter_is_down() -> void:
	var pils := _bro("lord_pilsner", 9)
	var chad := _bro("chadwick", 9)
	var croc := _villain({"target": "one", "type": "physical"})
	var core := _core([pils, chad], [croc])
	croc.taunted_by = "lord_pilsner"
	pils.hp = 0
	pils.meter = 0.0
	assert_eq(core._move_targets(croc, croc.moves[0]), [chad])


# --- the counter-brag --------------------------------------------------------------------------

func test_battle_taunt_shipped_counter_brag_numbers() -> void:
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string("res://assets/data/skills/party_abilities.json"))
	var cb: Dictionary = Dictionary(parsed)["abilities"]["bro_do_you_even_lift"]
	assert_eq(cb["display_name"], "Bro, Do You Even Lift?")
	assert_eq(cb["kind"], "counter_brag")
	assert_eq(cb["trigger"], "enemy_bravado_drain")
	assert_almost_eq(float(cb["chance_by_tier"]["high"]), 0.4, 0.0001)
	assert_almost_eq(float(cb["chance_by_tier"]["mid"]), 0.3, 0.0001)
	assert_almost_eq(float(cb["chance_by_tier"]["low"]), 0.2, 0.0001)
	assert_eq(Array(cb["blocked_by_status"]), ["embarrassed", "stun"])
	var party: Variant = JSON.parse_string(FileAccess.get_file_as_string("res://assets/data/party/party_members.json"))
	var kits: Dictionary = Dictionary(party)["party_members"]
	assert_true(Array(kits["bradley"]["skills"]).has("bro_do_you_even_lift"), "Bradley, from the start")
	assert_false(Array(kits["chadwick"]["skills"]).has("bro_do_you_even_lift"))
	assert_false(Array(kits["lord_pilsner"]["skills"]).has("bro_do_you_even_lift"))


func test_battle_taunt_counter_brag_turns_a_drain_into_a_gain() -> void:
	AbilityTable.set_tables(_counter_brag(1.0), {})
	var brad := _bro("bradley", 9, 4, ["bro_do_you_even_lift"])
	brad.bravado = 6
	var croc := _villain({"target": "one", "type": "none", "bravado_drain": 3})
	var core := _core([brad], [croc])
	core.attack(croc)
	core.step()
	assert_eq(brad.bravado, 9)


func test_battle_taunt_counter_brag_miss_still_drains() -> void:
	AbilityTable.set_tables(_counter_brag(0.0), {})
	var brad := _bro("bradley", 9, 4, ["bro_do_you_even_lift"])
	brad.bravado = 6
	var croc := _villain({"target": "one", "type": "none", "bravado_drain": 3})
	var core := _core([brad], [croc])
	core.attack(croc)
	core.step()
	assert_eq(brad.bravado, 3)


func test_battle_taunt_counter_brag_blocked_while_embarrassed() -> void:
	AbilityTable.set_tables(_counter_brag(1.0), {})
	var brad := _bro("bradley", 9, 4, ["bro_do_you_even_lift"])
	brad.bravado = 6
	brad.statuses["embarrassed"] = 5
	var croc := _villain({"target": "one", "type": "none", "bravado_drain": 3})
	var core := _core([brad], [croc])
	core.attack(croc)
	var before := brad.bravado
	core.step()
	assert_eq(brad.bravado, before - 3)


func test_battle_taunt_counter_brag_blocked_while_stunned() -> void:
	AbilityTable.set_tables(_counter_brag(1.0), {})
	var brad := _bro("bradley", 9, 4, ["bro_do_you_even_lift"])
	brad.bravado = 6
	var croc := _villain({"target": "one", "type": "none", "bravado_drain": 3})
	var core := _core([brad], [croc])
	core.attack(croc)
	brad.statuses["stun"] = 1
	core.step()
	assert_eq(brad.bravado, 3)


func test_battle_taunt_counter_brag_does_not_stop_the_damage() -> void:
	AbilityTable.set_tables(_counter_brag(1.0), {})
	# The villain's first roll picks its move, the second is the hit.
	var s := _seed_where(func(r: RandomNumberGenerator) -> bool:
		r.randf()
		return r.randf() < 0.95)
	var brad := _bro("bradley", 9, 4, ["bro_do_you_even_lift"])
	brad.bravado = 6
	var croc := _villain({"target": "one", "type": "physical", "bravado_drain": 3})
	var core := _core([brad], [croc])
	core.attack(croc)
	var r := RandomNumberGenerator.new()
	core._rng = r
	r.seed = s
	core.step()
	assert_lt(brad.hp, 40, "the hit still lands")
	assert_eq(brad.bravado, 9)


func test_battle_taunt_counter_brag_chance_follows_bradleys_tier() -> void:
	var tables := _counter_brag(0.0)
	tables["bro_do_you_even_lift"]["chance_by_tier"] = {"high": 0.4, "mid": 0.3, "low": 0.2}
	AbilityTable.set_tables(tables, {})
	var brad := _bro("bradley", 9, 4, ["bro_do_you_even_lift"])
	var core := _core([brad], [_villain({"target": "one", "type": "none"})])
	assert_almost_eq(core.counter_brag_chance(brad), 0.4, 0.0001)
	brad.bravado = 6
	assert_almost_eq(core.counter_brag_chance(brad), 0.3, 0.0001)
	brad.bravado = 1
	assert_almost_eq(core.counter_brag_chance(brad), 0.2, 0.0001)


# --- the venue beat ----------------------------------------------------------------------------

func test_battle_taunt_beat_wait_is_at_most_one_beat() -> void:
	assert_almost_eq(BattleRulings.beat_wait(0.2, 120.0), 0.3, 0.0001)
	assert_almost_eq(BattleRulings.beat_wait(0.5, 120.0), 0.0, 0.0001, "on the beat")
	assert_almost_eq(BattleRulings.beat_wait(1.01, 120.0), 0.49, 0.0001)
	assert_almost_eq(BattleRulings.beat_wait(3.7, 0.0), 0.0, 0.0001, "not a beat venue")
