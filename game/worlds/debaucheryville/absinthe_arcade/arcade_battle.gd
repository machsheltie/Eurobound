class_name ArcadeBattle
extends RefCounted
## The Absinthe Arcade's battle cabinets: which villains a play releases, building the fight from
## GameState, and writing the result back.
##  - Frogger and Street Fighter: a weighted random release table (ruled 2026-11-09). Frogger's Full
##    Crossing only appears once that cabinet has been beaten.
##  - Kebab Kombat: a fixed resetting ladder (ruled 2026-11-09). Each play fights the next rung; a win
##    on the last rung resets it, and a party wipe sends it back to the first rung. Each Clan ninja
##    slot rolls 5% to be MYSTERY BROWN (approved 2026-11-09).
##  - Win: tickets (ef4_multi_tickets) and each villain's drop roll. Loss: everyone at 1 HP
##    in front of the cabinet (ruling ef_arcade_loss). Run: tokens stay spent, HP kept (ef3_run).
## `state` is GameState (party, inventory, sovs, flags, add_item).

const BATTLE_DATA := "res://assets/data/enemies/debaucheryville_arcade_battle.json"
const ENEMY_DATA := "res://assets/data/enemies/debaucheryville_enemies.json"
const CONSUMABLES := "res://assets/data/items/consumables.json"
const SKILLS := "res://assets/data/skills/party_abilities.json"
const BACKDROP_DIR := "res://assets/worlds/debaucheryville/absinthe_arcade/interior/battle_backdrops/"
const LOSS_HP := 1
const NINJA := "condiment_clan_ninja"
const ACCOUNTS_RECEIVABLE := "accounts_receivable"
const NINJA_PALETTES := ["garlic", "chili"]

static var _cache: Dictionary = {}


static func _json(path: String) -> Dictionary:
	if not _cache.has(path):
		var parsed = JSON.parse_string(FileAccess.get_file_as_string(path))
		_cache[path] = parsed if parsed is Dictionary else {}
	return _cache[path]


static func is_battle_cabinet(machine_id: String) -> bool:
	return _json(BATTLE_DATA).get("cabinets", {}).has(machine_id)


static func cabinet(machine_id: String) -> Dictionary:
	return _json(BATTLE_DATA)["cabinets"].get(machine_id, {})


static func backdrop_path(machine_id: String) -> String:
	return BACKDROP_DIR + String(cabinet(machine_id).get("backdrop", ""))


static func skills() -> Dictionary:
	return _json(SKILLS).get("abilities", {})


static func won_flag(machine_id: String) -> String:
	return machine_id + "_won"


const RUNG_FLAG := "cabinet_kebab_kombat_rung"


## Jarmila's per-villain defeat counter (villain_leftovers): she comes back one word longer.
static func defeats_flag(id: String) -> String:
	return id + "_defeats"


static func rung(state) -> int:
	return int(state.flags.get(RUNG_FLAG, 0))


## The villain ids this play releases.
static func pick_release(machine_id: String, state, rng: RandomNumberGenerator) -> Array:
	var cab := cabinet(machine_id)
	if cab.get("structure", "") == "ladder":
		var rungs: Array = cab["rungs"]
		return Array(rungs[clampi(rung(state), 0, rungs.size() - 1)]["enemies"]).duplicate()
	var pool: Array = []
	var total := 0.0
	for r in cab.get("releases", []):
		if r.get("after_first_win", false) and not state.flags.get(won_flag(machine_id), false):
			continue  # ef4_full_crossing_locked: its weight is spread over the rest
		pool.append(r)
		total += float(r["weight"])
	var roll := rng.randf() * total
	for r in pool:
		roll -= float(r["weight"])
		if roll < 0.0:
			return Array(r["enemies"]).duplicate()
	return Array(pool[-1]["enemies"]).duplicate()


static func build(machine_id: String, state, rng: RandomNumberGenerator) -> BattleCore:
	return build_fight(pick_release(machine_id, state, rng), state, rng)


## A fight against these villain ids (a cabinet release, or Accounts Receivable at the door).
static func build_fight(enemy_ids: Array, state, rng: RandomNumberGenerator) -> BattleCore:
	var core := BattleCore.new(rng)
	core.wallet = state
	core.items = _json(CONSUMABLES).get("consumables", {})
	var villains: Dictionary = _json(BATTLE_DATA)["villains"]
	var engine: Dictionary = _json(ENEMY_DATA)["enemies"]
	for m in state.party:
		var member: Dictionary = m.duplicate()
		member["statuses"] = Dictionary(m.get("lasting_statuses", {})).duplicate()
		for id in member["statuses"].keys():
			member["statuses"][id] = -1
		member["statuses"].merge(FieldStatus.battle_statuses(state, String(m.get("id", ""))))
		var bro := BattleUnit.from_member(member)
		bro.gain_bravado(BreweryPassport.party_prep_bravado(state))  # v44 Party Prep; 0 while switched off
		core.party.append(bro)
	var ninjas := 0
	var seen := {}
	for id: String in enemy_ids:
		var battle: Dictionary = villains.get(id, {})
		var u := BattleUnit.from_enemy(id, engine.get(id, {}), battle)
		u.uses["base_name"] = u.display_name
		if battle.get("illusion", false):   # the Wisp's split: waits, unseen, until phase 2
			u.illusion = true
			u.dormant = true
		if battle.has("mirror_barks") and not state.party.is_empty():
			# Mirror Chad is the party leader's own reflection; that bro's mirror line opens the fight.
			var leader := String(state.party[0].get("id", ""))
			u.uses["mirror_of"] = leader
			u.data = battle.duplicate()
			u.data["intro_bark"] = String(Dictionary(battle["mirror_barks"]).get(leader, ""))
		var plates: Array = battle.get("nameplates", [])
		if not plates.is_empty():
			u.display_name = String(plates[int(seen.get(id, 0)) % plates.size()])
		seen[id] = int(seen.get(id, 0)) + 1
		if id == NINJA:
			_set_palette(u, battle, NINJA_PALETTES[ninjas % NINJA_PALETTES.size()], rng)
			ninjas += 1
		if id == BattleCore.JARMILA:
			var defeats := int(state.flags.get(defeats_flag(id), 0))
			u.uses["base_name"] = u.display_name
			u.uses["defeats"] = defeats
			u.uses["revisions"] = defeats
			u.display_name = BattleCore.jarmila_name(u.display_name, defeats)
		if id != ACCOUNTS_RECEIVABLE and not battle.get("not_cabinet", false):  # cabinet_difficulty is about the cabinets
			_toughen(u)
		if battle.has("second_thoughts"):
			core.second_thoughts = float(battle["second_thoughts"])
		core.add_enemy(u)
	core.start()
	return core


## cabinet_difficulty (round v28): cabinet villains get +50% HP.
static func _toughen(u: BattleUnit) -> void:
	u.max_hp = roundi(u.max_hp * BattleRulings.CABINET_HP_MULT)
	u.hp = u.max_hp
	u.meter = float(u.hp)


static func _set_palette(u: BattleUnit, battle: Dictionary, palette: String, rng: RandomNumberGenerator) -> void:
	var brown: Dictionary = battle.get("mystery_brown", {})
	if not brown.is_empty() and rng.randf() < float(brown.get("chance", 0.0)):
		palette = "mystery_brown"
		u.max_hp = int(brown["max_hp"])
		u.hp = u.max_hp
		u.meter = float(u.hp)
		u.offense = int(brown["offense"])
		u.ticket_reward = int(brown["ticket_reward"])
	u.palette = palette
	u.display_name = String(battle["palettes"][palette]["name"])


## Writes the fight back into GameState. Returns {"tickets": n, "drops": [ids], "refund": SOVS}.
static func settle(machine_id: String, core: BattleCore, state) -> Dictionary:
	var result := {"tickets": 0, "drops": [], "refund": 0}
	settle_party(core, state)
	_settle_rewards(machine_id, core, state, result)
	return result


## Writes HP, Bravado and lasting statuses back to the party: a loss leaves everyone at LOSS_HP.
static func settle_party(core: BattleCore, state) -> void:
	var lasting_rolls := BattleRulings.FOOD_POISONING_BATTLES
	for b in core.party:
		for m in state.party:
			if m["id"] != b.id:
				continue
			match core.outcome:
				"lost":
					m["hp"] = LOSS_HP
				_:
					m["hp"] = b.settled_hp() if not b.is_down() else BattleRulings.DOWN_AFTER_WIN_HP
			m["bravado"] = b.bravado
			var before: Dictionary = m.get("lasting_statuses", {})
			var after := {}
			for id in BattleRulings.LASTING_STATUSES:
				if not b.has_status(id):
					continue
				if id == "food_poisoning":
					var left := int(before.get(id, 0))
					left = left - 1 if left > 0 else core._rng.randi_range(lasting_rolls.x, lasting_rolls.y)
					if left > 0:
						after[id] = left
				else:
					after[id] = -1
			m["lasting_statuses"] = after


static func _settle_rewards(machine_id: String, core: BattleCore, state, result: Dictionary) -> void:
	var cab := cabinet(machine_id)
	if core.outcome == "won":
		result["tickets"] = core.tickets()
		result["drops"] = core.roll_drops()
		ArcadeRules.add_tickets(state, int(result["tickets"]))
		for id: String in result["drops"]:
			state.add_item(id)
		state.flags[won_flag(machine_id)] = true
		result["refund"] = core.soggy_pile()
		state.sovs += int(result["refund"])
		for e in core.enemies:
			if e.id == BattleCore.JARMILA:
				state.flags[defeats_flag(e.id)] = int(state.flags.get(defeats_flag(e.id), 0)) + 1
		if cab.get("structure", "") == "ladder":
			state.flags[RUNG_FLAG] = (rung(state) + 1) % Array(cab["rungs"]).size()
	elif core.outcome == "lost" and cab.get("structure", "") == "ladder":
		state.flags[RUNG_FLAG] = 0
