class_name StreetEncounters
extends Node
## Street encounters on one screen, Option A "EarthBound straight" (author, Eurobound Desk
## Eurobound-skjd-q2, 2026-11-16; docs/superpowers/specs/2026-11-16-Eurobound-skjd-proposal.md
## section 3; design/mechanics/Battle/street_encounters.md). Put one under a screen's root next to
## its StreetEnemy nodes. It:
##  - starts the existing battle (BattleCore + BattleScreen) when an enemy and the leader touch
##    (point 2), with the first strike judged by facing (point 3);
##  - wins on the spot when the bros clearly outclass the enemy (point 4; off until ruled);
##  - holds the map still during the fight, then gives a grace period after a win or a Run
##    (point 5; none until ruled);
##  - removes a beaten enemy until the screen loads again (point 6, StreetEnemy);
##  - on a loss, sends the bros back to the last save with part of their SOVS gone (point 7,
##    StreetLoss).
## The unruled numbers come from StreetEncounterRules (all off); tests set fixture values here.
##
## No screen has one yet: which enemy goes where is the author's (Eurobound-iqgo).

## touch() results.
const STARTED := "started"
const AUTO_WON := "auto_won"
const IGNORED := "ignored"

signal fight_started(enemy: StreetEnemy, core: BattleCore)
## After the fight is written back. `result`: {"outcome", "sovs", "xp", "drops"} (+ "loss" on a loss).
signal fight_settled(outcome: String, result: Dictionary)

## GameState (the autoload unless set).
var state
## SaveSystem (the autoload unless set).
var save_system
var rng: RandomNumberGenerator
## The leader (the screen's PlayerController unless set).
var player: PlayerController
## The street fight backdrop. None is painted yet.
var backdrop: Texture2D
## Moves the bros after a loss: called with StreetLoss.apply's plan. StreetLoss.travel unless set.
var traveler: Callable

var grace_length: Variant = StreetEncounterRules.GRACE_LENGTH
var grace_unit: String = StreetEncounterRules.GRACE_UNIT
var first_strike_rounds: Variant = StreetEncounterRules.FIRST_STRIKE_ROUNDS
var auto_win_gap: Variant = StreetEncounterRules.AUTO_WIN_LEVEL_GAP
var auto_win_measure: String = StreetEncounterRules.AUTO_WIN_PARTY_LEVEL
var loss_sovs_share: Variant = StreetEncounterRules.LOSS_SOVS_SHARE

## The fight on screen now, or null.
var battle_screen: BattleScreen
## What is left of the grace period, in grace_unit (0 = none).
var grace_left := 0.0

var _enemies: Array[StreetEnemy] = []
var _last_leader_pos: Variant = null


func _ready() -> void:
	if state == null:
		state = get_node_or_null("/root/GameState")
	if save_system == null:
		save_system = get_node_or_null("/root/SaveSystem")
	if rng == null:
		rng = RandomNumberGenerator.new()
		rng.randomize()
	if not traveler.is_valid():
		traveler = func(plan: Dictionary) -> void: StreetLoss.travel(get_tree(), plan)
	var screen := get_parent()
	for n in get_tree().get_nodes_in_group(StreetEnemy.GROUP):
		if screen != null and screen.is_ancestor_of(n):
			register(n as StreetEnemy)


## Listens to an enemy's contacts (every StreetEnemy on the screen at _ready is registered).
func register(e: StreetEnemy) -> void:
	if e == null or _enemies.has(e):
		return
	_enemies.append(e)
	e.touched_bros.connect(touch)


func _leader() -> PlayerController:
	if is_instance_valid(player):
		return player
	for n in get_tree().get_nodes_in_group("player"):
		if n is PlayerController:
			player = n
			return player
	return null


## An enemy and the leader touched. Starts the fight (STARTED), wins it on the spot (AUTO_WON), or
## does nothing (IGNORED: a fight is already up, the grace period runs, or the enemy has no fight).
func touch(e: StreetEnemy) -> String:
	if battle_screen != null or in_grace() or state == null:
		return IGNORED
	if not is_instance_valid(e) or e.is_queued_for_deletion() or e.enemy_ids.is_empty():
		return IGNORED
	var leader := _leader()
	var core := ArcadeBattle.build_fight(Array(e.enemy_ids), state, rng)
	core.loss_line = ""
	var what := STARTED
	var enemy_level: Variant = null if e.level == StreetEnemy.NO_LEVEL else e.level
	if StreetEncounterRules.auto_win(StreetEncounterRules.party_level(state.party, auto_win_measure),
			enemy_level, auto_win_gap, auto_win_measure):
		# Point 4: straight to the win (its SOVS, XP and drops are settled as for any win).
		for u in core.enemies:
			u.take_damage(u.hp)
		core.events.clear()
		core.outcome = "won"
		what = AUTO_WON
	elif first_strike_rounds != null and leader != null:
		var side := StreetEncounterRules.first_strike(leader.global_position, leader.facing_dir,
			e.global_position, e.facing_dir)
		if side != StreetEncounterRules.NONE:
			core.set_first_strike(side, int(first_strike_rounds))
	_hold(true)
	battle_screen = BattleScreen.new()
	battle_screen.name = "street_battle_screen"
	battle_screen.setup(core, backdrop, ArcadeBattle.skills())
	add_sibling(battle_screen)
	battle_screen.finished.connect(_on_finished.bind(e, core))
	fight_started.emit(e, core)
	return what


func _on_finished(_outcome: String, e: StreetEnemy, core: BattleCore) -> void:
	battle_screen = null
	settle(e, core)


## Writes the fight back into the state, as the Taproom fights do (TaproomBattle.settle): the
## party's HP, Bravado and lasting statuses; on a win the enemies' SOVS and drops (XP is reported,
## not paid: no XP system pays out anywhere yet). Then the win, the Run or the loss rule.
func settle(e: StreetEnemy, core: BattleCore) -> Dictionary:
	var result := {"outcome": core.outcome, "sovs": 0, "xp": 0, "drops": []}
	ArcadeBattle.settle_party(core, state)
	match core.outcome:
		"won":
			var engine: Dictionary = ArcadeBattle._json(ArcadeBattle.ENEMY_DATA).get("enemies", {})
			for u in core.enemies:
				var row: Dictionary = engine.get(u.id, {})
				result["sovs"] += int(row.get("sovs_reward", 0))
				result["xp"] += int(row.get("xp_reward", 0))
			state.sovs = int(state.sovs) + int(result["sovs"])
			for id: String in core.roll_drops():
				state.add_item(id)
				result["drops"].append(id)
			if is_instance_valid(e):
				_enemies.erase(e)
				e.defeat()
			_start_grace()
		"lost":
			result["loss"] = StreetLoss.apply(state, save_system, loss_sovs_share, _fallback_scene())
			_hold(false)
			fight_settled.emit(core.outcome, result)
			traveler.call(result["loss"])
			return result
		_:
			_start_grace()   # a Run (or a fight the enemy walked out of)
	_hold(false)
	fight_settled.emit(core.outcome, result)
	return result


## With no save, the loss goes back to the start of this screen.
func _fallback_scene() -> String:
	var screen := get_parent()
	if screen != null and not screen.scene_file_path.is_empty():
		return screen.scene_file_path
	return String(state.current_scene_path)


## Holds the bros and every enemy on the screen still while a fight is up.
func _hold(on: bool) -> void:
	var leader := _leader()
	if leader != null:
		leader.input_locked = on
	for x in _enemies:
		if is_instance_valid(x):
			x.frozen = on


# --- grace after a fight or a Run (point 5) ----------------------------------------------------

func in_grace() -> bool:
	return grace_left > 0.0


func _start_grace() -> void:
	grace_left = 0.0
	if grace_length == null or float(grace_length) <= 0.0:
		return
	if grace_unit != StreetEncounterRules.UNIT_STEPS and grace_unit != StreetEncounterRules.UNIT_SECONDS:
		return
	grace_left = float(grace_length)
	var leader := _leader()
	_last_leader_pos = leader.global_position if leader != null else null


## Counts the grace down by `seconds` or by `metres` the leader walked, by grace_unit.
func advance_grace(seconds: float, metres: float) -> void:
	if grace_left <= 0.0:
		return
	grace_left -= seconds if grace_unit == StreetEncounterRules.UNIT_SECONDS else metres
	grace_left = maxf(grace_left, 0.0)


func _physics_process(delta: float) -> void:
	if grace_left <= 0.0:
		return
	var moved := 0.0
	var leader := _leader()
	if leader != null:
		var pos := leader.global_position
		if _last_leader_pos != null:
			var d := Vector2(pos.x - _last_leader_pos.x, pos.z - _last_leader_pos.z).length()
			if d <= PlayerController.STEP_JUMP_M:   # a teleport is not walking (FieldStatus steps)
				moved = d
		_last_leader_pos = pos
	advance_grace(delta, moved)
