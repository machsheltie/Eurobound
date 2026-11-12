class_name TaproomBattle
extends RefCounted
## The Absinthium Taproom's two fights: Mirror Chad and the Green Fairy Wisp.
## Implements design/worlds/debaucheryville/the_absinthium_taproom.md:152-185 (fights, rewards) with
## the author's round v44 numbers (docs/superpowers/proposals/2026-11-12-v43-design-proposals.md 1.2-1.4):
##  - Mirror Chad: package A, Words Only (54 HP, he never damages; his three barks cost Bravado and
##    statuses, and Confused lands on his third turn).
##  - Green Fairy Wisp: 72 HP, three phases at 66% / 33%, the split into three (2 illusions), and
##    "defeat OR survive": she leaves after round 6.
##  - Rewards: 12 SOVS (Mirror Chad), 25 SOVS (Wisp), no tickets. The stat lines live in
##    debaucheryville_enemies.json, the moves in debaucheryville_arcade_battle.json ("villains" and
##    the "taproom" block, which also records the Absinthe Lager price: data only, buying is elsewhere).
## NOT WIRED INTO ANY ROOM: where each fight starts is an open author question. A room calls
## start_mirror_chad(host, state) / start_wisp(host, state) when the author rules it.
## `state` is GameState (party, inventory, sovs, flags, add_item).

const MIRROR_CHAD := "mirror_chad"
const WISP := "green_fairy_wisp"
const FLAG_MIRROR_CHAD_DEFEATED := "mirror_chad_defeated"
const FLAG_WISP_DEFEATED := "green_fairy_wisp_defeated"
const FLAG_WISP_SURVIVED := "green_fairy_wisp_survived"


static func config() -> Dictionary:
	return ArcadeBattle._json(ArcadeBattle.BATTLE_DATA).get("taproom", {})


static func fight_data(fight: String) -> Dictionary:
	return Dictionary(config().get("fights", {})).get(fight, {})


static func backdrop_path() -> String:
	return ArcadeBattle.BACKDROP_DIR + String(config().get("backdrop", ""))


## Data only: Dr. Vanek sells it (another task).
static func lager_price() -> int:
	return int(config().get("absinthe_lager_price_sovs", 0))


static func build(fight: String, state, rng: RandomNumberGenerator) -> BattleCore:
	return ArcadeBattle.build_fight(fight_data(fight).get("enemies", []), state, rng)


static func build_mirror_chad(state, rng: RandomNumberGenerator) -> BattleCore:
	return build(MIRROR_CHAD, state, rng)


static func build_wisp(state, rng: RandomNumberGenerator) -> BattleCore:
	return build(WISP, state, rng)


## Writes the fight back into GameState. Returns {"outcome", "sovs", "xp", "drops", "tickets"}.
## Won: SOVS, the guaranteed drops and the defeated flag. Survived (the Wisp left): her survived
## flag only (proposal 1.3: no Essence, no XP). Everything else leaves the party's HP, as ArcadeBattle does.
## XP is reported, not paid: no XP system pays out anywhere yet.
static func settle(fight: String, core: BattleCore, state) -> Dictionary:
	var result := {"outcome": core.outcome, "sovs": 0, "xp": 0, "drops": [], "tickets": 0}
	ArcadeBattle.settle_party(core, state)
	for hit in core.field_hits:
		if String(hit["status"]) == FieldStatus.SAW_YOURSELF:
			FieldStatus.apply_saw_yourself(state, String(hit["bro"]))
	var data := fight_data(fight)
	match core.outcome:
		"won":
			var engine: Dictionary = ArcadeBattle._json(ArcadeBattle.ENEMY_DATA)["enemies"]
			for e in core.enemies:
				var row: Dictionary = engine.get(e.id, {})
				result["sovs"] += int(row.get("sovs_reward", 0))
				result["xp"] += int(row.get("xp_reward", 0))
			state.sovs += int(result["sovs"])
			for id: String in data.get("drops", []):
				state.add_item(id)
				result["drops"].append(id)
			state.flags[String(data.get("defeated_flag", ""))] = true
		"survived":
			state.flags[String(data.get("survived_flag", ""))] = true
	return result


## Runs the fight on `host` and settles it. Returns the outcome ("won", "lost", "ran", "survived").
static func start_mirror_chad(host: Node, state, rng: RandomNumberGenerator = null) -> String:
	return await _run(host, MIRROR_CHAD, state, rng)


static func start_wisp(host: Node, state, rng: RandomNumberGenerator = null) -> String:
	return await _run(host, WISP, state, rng)


static func _run(host: Node, fight: String, state, rng: RandomNumberGenerator) -> String:
	if rng == null:
		rng = RandomNumberGenerator.new()
		rng.randomize()
	var core := build(fight, state, rng)
	var screen := BattleScreen.new()
	screen.name = "battle_screen"
	screen.setup(core, load(backdrop_path()), ArcadeBattle.skills())
	host.add_child(screen)
	var outcome: String = await screen.finished
	settle(fight, core, state)
	return outcome
