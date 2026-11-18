class_name NpcStanding
extends RefCounted
## Per-NPC grudge and fan flags (Eurobound-3385). Author ruling, Eurobound Desk f3tq-q6
## (2026-11-13; docs/superpowers/NEXT_WORK.md, "Drunk rules, part 2 of 3"): "Flags only: an NPC
## can hold a grudge or become a fan (no numbers)". This is option B in section 5 of
## docs/superpowers/proposals/2026-11-13-drunk-judgment-and-folklore-proposal.md.
##
## The flags are booleans in GameState.flags, so they save and load with every other flag:
##   grudge:<npc_id>           an NPC holds a grudge against the bros
##   fan:<crowd_or_npc_id>     a crowd or an NPC has become a fan
## Both are declared in quest_flags.json (flag_patterns). There is no numeric standing anywhere,
## and Regional Reputation is untouched. The two flags are independent: no ruling makes one clear
## the other, so an outcome that wants that writes both (apply_set_flags with true and false).
##
## Readers: dialogue conditions read them by id (GameState.has_flag(NpcStanding.grudge_flag(id)),
## or a dialogue-tree option's requires flag), and any code holding the state, the shop price path
## included, calls has_grudge / is_fan / standing. What a grudge or fan flag changes in a given
## NPC's lines or prices is content for that NPC's own doc; nothing here changes a line or a price.

const GRUDGE_PREFIX := "grudge:"
const FAN_PREFIX := "fan:"

## The fill the registry patterns accept (validate_data.py _declared_as: [a-z0-9_.]+).
static var _id_re := RegEx.create_from_string("^[a-z0-9_.]+$")


static func valid_id(id: String) -> bool:
	return _id_re.search(id) != null


static func grudge_flag(npc_id: String) -> String:
	return GRUDGE_PREFIX + npc_id


static func fan_flag(crowd_or_npc_id: String) -> String:
	return FAN_PREFIX + crowd_or_npc_id


static func has_grudge(state, npc_id: String) -> bool:
	return valid_id(npc_id) and bool(state.flags.get(GRUDGE_PREFIX + npc_id, false))


static func is_fan(state, crowd_or_npc_id: String) -> bool:
	return valid_id(crowd_or_npc_id) and bool(state.flags.get(FAN_PREFIX + crowd_or_npc_id, false))


## {"grudge": bool, "fan": bool} for one id: the one read a dialogue or shop caller needs.
static func standing(state, id: String) -> Dictionary:
	return {"grudge": has_grudge(state, id), "fan": is_fan(state, id)}


## False (and nothing written) for an id the registry pattern cannot hold.
static func set_grudge(state, npc_id: String) -> bool:
	if not valid_id(npc_id):
		return false
	state.flags[GRUDGE_PREFIX + npc_id] = true
	return true


static func set_fan(state, crowd_or_npc_id: String) -> bool:
	if not valid_id(crowd_or_npc_id):
		return false
	state.flags[FAN_PREFIX + crowd_or_npc_id] = true
	return true


## A cleared flag is removed, which reads the same as never set (the registry default, false).
static func clear_grudge(state, npc_id: String) -> void:
	state.flags.erase(GRUDGE_PREFIX + npc_id)


static func clear_fan(state, crowd_or_npc_id: String) -> void:
	state.flags.erase(FAN_PREFIX + crowd_or_npc_id)


## True when `flag_id` is a grudge or fan flag with a valid id.
static func is_standing_flag(flag_id: String) -> bool:
	for prefix: String in [GRUDGE_PREFIX, FAN_PREFIX]:
		if flag_id.begins_with(prefix):
			return valid_id(flag_id.substr(prefix.length()))
	return false


## Applies the grudge and fan entries of an event outcome's "set_flags" object (the ruled write
## shape, docs/superpowers/specs/2026-11-12-flag-write-shape-proposal.md): true sets, false clears.
## Other flag ids are left for their own writers; a non-boolean value or a bad id is skipped.
## Returns the flag ids applied.
static func apply_set_flags(state, set_flags: Dictionary) -> Array:
	var applied: Array = []
	for key: Variant in set_flags:
		var flag_id := String(key)
		var value: Variant = set_flags[key]
		if not is_standing_flag(flag_id) or not (value is bool):
			continue
		if value:
			state.flags[flag_id] = true
		else:
			state.flags.erase(flag_id)
		applied.append(flag_id)
	return applied
