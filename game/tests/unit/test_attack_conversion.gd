extends GutTest
## Attack-conversion resolvers in BattleCore.attack() (Eurobound-wrmf). Fixture numbers only;
## the shipped status_effects.json is null here and a test proves null is inert.


class FakeWallet:
	var sovs := 0
	var inventory := {}
	var flags := {}
	var party: Array = []


func after_each() -> void:
	StatusTable.reset()


func _table(clean: Dictionary, pacify: Dictionary) -> Dictionary:
	# accuracy_steps 50 makes every swing land, so the tests do not depend on the RNG.
	return {
		"sugar_rush_hour": {"accuracy_steps": 50, "attack_conversion": clean},
		"gush_locked": {"accuracy_steps": 50, "attack_conversion": pacify},
		"mellow": {"display_name": "Mellow"},
	}


func _clean(per_hit: Variant, cap: Variant, mult: Variant = null, text: Variant = null) -> Dictionary:
	return {"kind": "cleaning", "applies_to": "attack", "damage_mult": mult,
		"bravado_steal": {"per_hit": per_hit, "cap": cap}, "battle_text": text}


func _pacify(status: Variant, chance: Variant, turns: Variant, mult: Variant = null) -> Dictionary:
	return {"kind": "pacification", "applies_to": "attack", "damage_mult": mult,
		"inflict": {"status": status, "chance": chance, "turns": turns}, "battle_text": null}


func _fight(statuses: Dictionary, enemy_sp: int) -> BattleCore:
	var bro := BattleUnit.from_member({"id": "bro", "display_name": "Bro", "max_hp": 30, "hp": 30, "max_bravado": 12,
		"bravado": 4, "offense": 8, "defense": 2, "speed": 99, "luck": 0, "grit": 1, "charm": 4, "skills": [],
		"statuses": statuses})
	var r := RandomNumberGenerator.new()
	r.seed = 1
	var core := BattleCore.new(r)
	core.wallet = FakeWallet.new()
	core.party.append(bro)
	core.add_enemy(BattleUnit.from_enemy("foe", {"display_name": "Foe", "max_hp": 500, "offense": 1, "defense": 0,
		"speed": 1, "luck": 0, "ticket_reward": 0}, {}))
	core.start()
	core.step()
	core.enemies[0].sp = enemy_sp
	return core


func _hp_lost(core: BattleCore) -> int:
	return 500 - core.enemies[0].hp


func test_conversion_cleaning_moves_sp_to_bravado() -> void:
	StatusTable.set_entries(_table(_clean(3, null), _pacify(null, null, null)))
	var core := _fight({"sugar_rush_hour": -1}, 10)
	core.attack(core.enemies[0])
	assert_eq(core.enemies[0].sp, 7)
	assert_eq(core.party[0].bravado, 7)


func test_conversion_cleaning_limited_by_target_sp_and_cap() -> void:
	StatusTable.set_entries(_table(_clean(5, 6), _pacify(null, null, null)))
	var core := _fight({"sugar_rush_hour": -1}, 2)
	core.attack(core.enemies[0])
	assert_eq(core.enemies[0].sp, 0)
	assert_eq(core.party[0].bravado, 6)


func test_conversion_cleaning_enemy_with_zero_sp_yields_nothing_and_does_not_crash() -> void:
	StatusTable.set_entries(_table(_clean(3, 10), _pacify(null, null, null)))
	var core := _fight({"sugar_rush_hour": -1}, 0)
	core.attack(core.enemies[0])
	assert_eq(core.enemies[0].sp, 0)
	assert_eq(core.party[0].bravado, 4)
	assert_gt(_hp_lost(core), 0)


func test_conversion_damage_mult_scales_the_hit() -> void:
	StatusTable.set_entries(_table(_clean(null, null), _pacify(null, null, null)))
	var plain := _fight({"sugar_rush_hour": -1}, 0)
	plain.attack(plain.enemies[0])
	StatusTable.set_entries(_table(_clean(null, null, 0.5), _pacify(null, null, null)))
	var halved := _fight({"sugar_rush_hour": -1}, 0)
	halved.attack(halved.enemies[0])
	assert_lt(_hp_lost(halved), _hp_lost(plain))


func test_conversion_pacification_rolls_the_named_status() -> void:
	StatusTable.set_entries(_table(_clean(null, null), _pacify("mellow", 1.0, 2)))
	var core := _fight({"gush_locked": -1}, 0)
	core.attack(core.enemies[0])
	assert_true(core.enemies[0].has_status("mellow"))
	assert_eq(core.party[0].bravado, 4, "pacification steals no Bravado")


func test_conversion_picked_by_status_not_mixed() -> void:
	StatusTable.set_entries(_table(_clean(3, null), _pacify("mellow", 1.0, 2)))
	var core := _fight({"sugar_rush_hour": -1}, 10)
	core.attack(core.enemies[0])
	assert_false(core.enemies[0].has_status("mellow"))
	assert_eq(core.enemies[0].sp, 7)


func test_conversion_null_values_are_inert() -> void:
	StatusTable.set_entries(_table(_clean(null, null), _pacify(null, null, null)))
	for sid in ["sugar_rush_hour", "gush_locked"]:
		var core := _fight({sid: -1}, 0)
		core.attack(core.enemies[0])
		assert_eq(core.enemies[0].sp, 0, sid)
		assert_eq(core.party[0].bravado, 4, sid)
		assert_true(core.enemies[0].statuses.is_empty(), sid)
		assert_gt(_hp_lost(core), 0, sid)


func test_conversion_shipped_file_is_inert_until_tuned() -> void:
	var core := _fight({"sugar_rush_hour": -1, "gush_locked": -1}, 5)
	core.attack(core.enemies[0])
	assert_eq(core.enemies[0].sp, 5)
	assert_eq(core.party[0].bravado, 4)
	assert_true(core.enemies[0].statuses.is_empty())


func test_conversion_battle_text_replaces_attack_line_with_tokens() -> void:
	StatusTable.set_entries(_table(_clean(3, null, null, ["{user} scrubs {target} for {amount}."]), _pacify(null, null, null)))
	var core := _fight({"sugar_rush_hour": -1}, 10)
	core.attack(core.enemies[0])
	var texts: Array = core.events.map(func(e: Dictionary) -> String: return String(e.get("text", "")))
	assert_true(texts.has("Bro scrubs Foe for 3."), str(texts))
	assert_false(texts.has("Bro attacks!"))
