extends Control
## EarthBound-style front-view battle. One party member vs one enemy.
## All numbers come from DataRepo/GameState; win/lose returns via SceneRouter.

var _enemy: Dictionary
var _enemy_hp: int
var _member: Dictionary
var _rng := RandomNumberGenerator.new()

var _log_label: Label
var _stats_label: Label
var _menu: VBoxContainer
var _enemy_visual: ColorRect

func _ready() -> void:
	_rng.randomize()
	_enemy = DataRepo.get_enemy(SceneRouter.pending_enemy_id)
	if _enemy.is_empty():
		push_error("BattleScene: no enemy for id '%s'" % SceneRouter.pending_enemy_id)
		SceneRouter.end_battle()
		return
	_enemy_hp = int(_enemy["max_hp"])
	_member = GameState.party[0]
	_build_ui()
	_log(String(_enemy.get("battle_intro", "%s appears!" % _enemy["display_name"])))
	_set_menu_enabled(true)

func _build_ui() -> void:
	var bg := ColorRect.new()
	bg.color = Color(0.08, 0.05, 0.12)
	bg.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(bg)

	_enemy_visual = ColorRect.new()
	_enemy_visual.color = Color(0.85, 0.25, 0.25)
	_enemy_visual.size = Vector2(120, 120)
	_enemy_visual.anchor_left = 0.5
	_enemy_visual.anchor_right = 0.5
	_enemy_visual.anchor_top = 0.25
	_enemy_visual.anchor_bottom = 0.25
	_enemy_visual.position = Vector2(-60, -60)
	add_child(_enemy_visual)

	var enemy_name := Label.new()
	enemy_name.text = String(_enemy["display_name"])
	enemy_name.anchor_left = 0.5
	enemy_name.anchor_right = 0.5
	enemy_name.anchor_top = 0.12
	enemy_name.position = Vector2(-100, 0)
	enemy_name.custom_minimum_size = Vector2(200, 0)
	enemy_name.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	add_child(enemy_name)

	_log_label = Label.new()
	_log_label.anchor_top = 0.55
	_log_label.anchor_left = 0.1
	_log_label.anchor_right = 0.9
	_log_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	add_child(_log_label)

	_stats_label = Label.new()
	_stats_label.anchor_top = 0.68
	_stats_label.anchor_left = 0.1
	add_child(_stats_label)

	_menu = VBoxContainer.new()
	_menu.anchor_top = 0.75
	_menu.anchor_left = 0.1
	_menu.anchor_right = 0.4
	add_child(_menu)
	_add_action("Bash", _on_bash)
	_add_action("Roast Line", _on_roast)
	_add_action("Item", _on_item)
	_add_action("Run", _on_run)
	_refresh_stats()

func _add_action(label: String, handler: Callable) -> void:
	var button := Button.new()
	button.text = label
	button.pressed.connect(handler)
	_menu.add_child(button)

func _refresh_stats() -> void:
	_stats_label.text = "%s  HP %d/%d  SP %d/%d" % [
		_member["display_name"], _member["hp"], _member["max_hp"],
		_member["sp"], _member["max_sp"]]

func _log(text: String) -> void:
	_log_label.text = text

func _set_menu_enabled(enabled: bool) -> void:
	for button in _menu.get_children():
		button.disabled = not enabled
	if enabled and _menu.get_child_count() > 0:
		_menu.get_child(0).grab_focus()

func _on_bash() -> void:
	_player_attack(1.0, "%s bashes!" % _member["display_name"])

func _on_roast() -> void:
	var ability: Dictionary = DataRepo.get_ability("roast_line")
	var cost := int(ability.get("sp_cost", 0))
	if int(_member["sp"]) < cost:
		_log("Not enough SP!")
		return
	_member["sp"] = int(_member["sp"]) - cost
	_player_attack(float(ability.get("power_multiplier", 1.0)),
		String(ability.get("battle_text", "")).format({"user": _member["display_name"]}))

func _on_item() -> void:
	if not GameState.use_item("lukewarm_kebab", DataRepo) \
			and not GameState.use_item("questionable_goulash", DataRepo) \
			and not GameState.use_item("absinthe_shot", DataRepo):
		_log("No usable items!")
		return
	_refresh_stats()
	_log("%s scarfs something questionable." % _member["display_name"])
	_enemy_turn()

func _on_run() -> void:
	if _rng.randf() < 0.5:
		_log("Got away safely!")
		_finish(true)
	else:
		_log("Couldn't escape!")
		_enemy_turn()

func _player_attack(multiplier: float, flavor: String) -> void:
	_set_menu_enabled(false)
	var result := DamageCalculator.compute(_member, _enemy, _rng, multiplier)
	_enemy_hp -= int(result["damage"])
	var text := "%s %d damage!" % ["SMAAAASH!!" if result["crit"] else flavor, result["damage"]]
	_log(text)
	_refresh_stats()
	if _enemy_hp <= 0:
		_win()
	else:
		_enemy_turn()

func _enemy_turn() -> void:
	_set_menu_enabled(false)
	await get_tree().create_timer(0.9).timeout
	var result := DamageCalculator.compute(_enemy, _member, _rng)
	_member["hp"] = int(_member["hp"]) - int(result["damage"])
	_log("%s attacks! %d damage!" % [_enemy["display_name"], result["damage"]])
	_refresh_stats()
	if int(_member["hp"]) <= 0:
		_lose()
	else:
		_set_menu_enabled(true)

func _win() -> void:
	await get_tree().create_timer(0.9).timeout
	var xp := int(_enemy.get("xp_reward", 0))
	var gold := int(_enemy.get("gold_reward", 0))
	var drop := ""
	if _rng.randf() < float(_enemy.get("drop_chance", 0.0)):
		drop = String(_enemy.get("item_drop", ""))
	GameState.grant_rewards(xp, gold, drop)
	var summary := "You won! +%d XP, +%d gold." % [xp, gold]
	if drop != "":
		summary += " Found: %s!" % String(DataRepo.get_item(drop).get("display_name", drop))
	_log(summary)
	_finish(true)

func _lose() -> void:
	await get_tree().create_timer(0.9).timeout
	_member["hp"] = 1
	_log("%s got wrecked... crawling back to the plaza." % _member["display_name"])
	_finish(false)

func _finish(restore_position: bool) -> void:
	_set_menu_enabled(false)
	await get_tree().create_timer(1.5).timeout
	SceneRouter.end_battle(restore_position)
