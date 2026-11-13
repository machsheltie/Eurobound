class_name NavigationRoll
extends RefCounted
## The Shamsterdam Navigation roll at Voetgangerstunnel intersections (Eurobound-eggq). Ruled values
## only: design/worlds/shamsterdam/voetgangerstunnel.md, Navigation Mechanics (N1-N5, Display) and
## docs/superpowers/specs/2026-11-12-shamsterdam-navigation-base-odds-proposal.md (approved
## Eurobound-76gz; clamp and Sober approved Eurobound-eb8). Exit tables and modifier points live in
## assets/data/navigation/voetgangerstunnel.json. No scene exists yet: the tunnel scene calls roll()
## at each intersection, display_text() for the map readout and leave_tunnel() on exit.
##  - N1 base = the followed sign's correct-exit row (40 Centraal / 50 Museum Plein).
##  - N3 base + every active modifier (additive points) -> clamp 10-90 -> roll.
##  - N2 wrong exits share 100 - correct in their listed proportions, largest remainder, ties to
##    the higher row.
##  - N4 each success this visit is +5; the count resets when the party leaves the tunnel.
##  - Sober (+20): lost with the party's first alcohol: true drink, back at the next rest.
##  - Display: the final chance shows only while the map item is equipped.
## Caller context (ctx): "map_equipped" (no equipment slots exist yet), "local_guide" (hired for
## this roll), "opa_cees" (the rental-insurance blessing; the permanent one is FLAG_OPA_CEES),
## "extra_points" (testing / future modifiers the author rules).
## Statuses the roll grants itself (Eurobound-1esc), lengths in assets/data/navigation/voetgangerstunnel.json
## "grants" (null = not ruled = inert):
##  - Tunnel Confusion (voetgangerstunnel.md:438-442): the visit's 3rd wrong turn (count from
##    voetgangerstunnel_items.json:261 and voetgangerstunnel_events.json:343-344) puts it on the whole
##    party for 2 hours of game clock; any successful navigation ends it. A wrong turn while it is
##    on does not refresh it (stacking is not ruled).
##  - Tunnel Vision (:183, :452-455): a success with no wrong turn this visit puts it on the whole
##    party for 1 hour of game clock. Its "+5% Speed underground" has no engine hook (Eurobound-cvkq).

const DATA_PATH := "res://assets/data/navigation/voetgangerstunnel.json"
const SIGN_CENTRAAL := "centraal_station"
const SIGN_MUSEUM_PLEIN := "museum_plein"
## Set by the party's first alcoholic drink since the last rest; cleared at rest.
const SOBER_LOST_KEY := "nav_sober_lost"
const VISIT_KEY := "nav_tunnel_visit_successes"
const WRONG_KEY := "nav_tunnel_visit_wrong_turns"
const TUNNEL_CONFUSION := "tunnel_confusion"
const TUNNEL_VISION := "tunnel_vision"
## Permanent rewards (quest/achievement), read as flags. Granting them is other work.
const FLAG_OPA_CEES := "opa_cees_blessing"
const FLAG_UNDERGROUND_NAVIGATOR := "underground_navigator"

var data: Dictionary
var state
var rng: RandomNumberGenerator


static func load_data(path: String = DATA_PATH) -> Dictionary:
	var f := FileAccess.open(path, FileAccess.READ)
	if f == null:
		return {}
	var parsed = JSON.parse_string(f.get_as_text())
	return parsed if parsed is Dictionary else {}


func _init(state_, rng_: RandomNumberGenerator = null, data_: Dictionary = {}) -> void:
	state = state_
	rng = rng_
	if rng == null:
		rng = RandomNumberGenerator.new()
		rng.randomize()
	data = data_ if not data_.is_empty() else load_data()


## Errors in the data; empty = valid. Each sign: exactly one correct exit, weights summing to 100.
static func validate(d: Dictionary) -> Array:
	var errs := []
	var signs: Dictionary = d.get("signs", {})
	if signs.is_empty():
		errs.append("no signs")
	for s in signs:
		var exits: Array = Dictionary(signs[s]).get("exits", [])
		var total := 0
		var n_correct := 0
		for e: Dictionary in exits:
			total += int(e.get("weight", 0))
			if bool(e.get("correct", false)):
				n_correct += 1
		if total != 100:
			errs.append("%s: weights sum to %d" % [s, total])
		if n_correct != 1:
			errs.append("%s: %d correct exits (needs 1)" % [s, n_correct])
	var c: Dictionary = d.get("clamp", {})
	if not c.has("min") or not c.has("max") or int(c["min"]) > int(c["max"]):
		errs.append("bad clamp")
	var g: Dictionary = d.get("grants", {})
	for path in [[TUNNEL_CONFUSION, "wrong_turns"], [TUNNEL_CONFUSION, "minutes"], [TUNNEL_VISION, "minutes"]]:
		var v: Variant = Dictionary(g.get(path[0], {})).get(path[1], null)
		if v != null and _positive_int(v) < 1:
			errs.append("grants.%s.%s: an int >= 1 or null" % path)
	return errs


## A whole number >= 1 from JSON, or 0 when `v` is null, not a number or not whole.
static func _positive_int(v: Variant) -> int:
	if not (v is int or v is float) or float(v) != floorf(float(v)) or float(v) < 1.0:
		return 0
	return int(v)


# --- Sober --------------------------------------------------------------------------------------

static func is_sober(st) -> bool:
	return not bool(st.flags.get(SOBER_LOST_KEY, false))


## Call wherever a bro consumes an item; only alcohol: true drinks end Sober.
static func note_item_used(st, item: Dictionary) -> void:
	if GameClock.is_drink(item) and "flags" in st:
		st.flags[SOBER_LOST_KEY] = true


## GameClock.rest calls this: Sober returns.
static func on_rest(st) -> void:
	if "flags" in st:
		st.flags.erase(SOBER_LOST_KEY)


# --- per-visit counter (N4) ---------------------------------------------------------------------

func successes_this_visit() -> int:
	return int(state.flags.get(VISIT_KEY, 0))


func wrong_turns_this_visit() -> int:
	return int(state.flags.get(WRONG_KEY, 0))


func leave_tunnel() -> void:
	state.flags.erase(VISIT_KEY)
	state.flags.erase(WRONG_KEY)


# --- statuses the roll grants (Eurobound-1esc) --------------------------------------------------

## A ruled value from "grants", or 0 when it is unruled (null) or missing.
func _grant(status_id: String, key: String) -> int:
	return _positive_int(Dictionary(Dictionary(data.get("grants", {})).get(status_id, {})).get(key, null))


## After a correct exit: ends Tunnel Confusion; grants Tunnel Vision when the visit had no wrong turn.
func _after_success(granted: Array, cured: Array) -> void:
	if FieldStatus.has(state, TUNNEL_CONFUSION):
		FieldStatus.remove(state, TUNNEL_CONFUSION)
		cured.append(TUNNEL_CONFUSION)
	var minutes := _grant(TUNNEL_VISION, "minutes")
	if wrong_turns_this_visit() == 0 and minutes > 0:
		FieldStatus.apply(state, FieldStatus.PARTY, TUNNEL_VISION, minutes, FieldStatus.UNIT_CLOCK)
		granted.append(TUNNEL_VISION)


## After a wrong exit: Tunnel Confusion once the visit's wrong turns reach the ruled count.
func _after_wrong_turn(granted: Array) -> void:
	var needed := _grant(TUNNEL_CONFUSION, "wrong_turns")
	var minutes := _grant(TUNNEL_CONFUSION, "minutes")
	if needed > 0 and minutes > 0 and wrong_turns_this_visit() >= needed 			and not FieldStatus.has(state, TUNNEL_CONFUSION):
		FieldStatus.apply(state, FieldStatus.PARTY, TUNNEL_CONFUSION, minutes, FieldStatus.UNIT_CLOCK)
		granted.append(TUNNEL_CONFUSION)


# --- odds ---------------------------------------------------------------------------------------

func _exits(sign_id: String) -> Array:
	return Array(Dictionary(Dictionary(data.get("signs", {})).get(sign_id, {})).get("exits", []))


## N1: the followed sign's correct-exit weight; -1 for an unknown sign.
func base_chance(sign_id: String) -> int:
	for e: Dictionary in _exits(sign_id):
		if bool(e.get("correct", false)):
			return int(e.get("weight", 0))
	return -1


## Every active modifier as [{"id", "points"}], in a fixed order.
func modifiers(ctx: Dictionary) -> Array:
	var m: Dictionary = data.get("modifiers", {})
	var out := []
	if is_sober(state):
		out.append({"id": "sober", "points": int(m.get("sober", 0))})
	if bool(ctx.get("map_equipped", false)):
		out.append({"id": "map_equipped", "points": int(m.get("map_equipped", 0))})
	if bool(ctx.get("local_guide", false)):
		out.append({"id": "local_guide", "points": int(m.get("local_guide", 0))})
	if bool(ctx.get("opa_cees", false)) or bool(state.flags.get(FLAG_OPA_CEES, false)):
		out.append({"id": "opa_cees_blessing", "points": int(m.get("opa_cees_blessing", 0))})
	if bool(state.flags.get(FLAG_UNDERGROUND_NAVIGATOR, false)):
		out.append({"id": "underground_navigator", "points": int(m.get("underground_navigator", 0))})
	var wins := successes_this_visit()
	if wins > 0:
		out.append({"id": "per_visit_success", "points": wins * int(m.get("per_visit_success", 0))})
	# A party-level penalty: counts once while any bro (or the party) has the status.
	var statuses: Dictionary = m.get("statuses", {})
	for sid in statuses:
		if FieldStatus.has(state, String(sid)):
			out.append({"id": String(sid), "points": int(statuses[sid])})
	if ctx.has("extra_points"):
		out.append({"id": "extra", "points": int(ctx["extra_points"])})
	return out


func modifier_sum(ctx: Dictionary) -> int:
	var total := 0
	for m in modifiers(ctx):
		total += int(m["points"])
	return total


func unclamped_chance(sign_id: String, ctx: Dictionary) -> int:
	return base_chance(sign_id) + modifier_sum(ctx)


## N3: base + modifiers, clamped to the ruled 10-90; -1 for an unknown sign.
func correct_chance(sign_id: String, ctx: Dictionary) -> int:
	if base_chance(sign_id) < 0:
		return -1
	var c: Dictionary = data.get("clamp", {})
	return clampi(unclamped_chance(sign_id, ctx), int(c.get("min", 0)), int(c.get("max", 100)))


## N2: shares `remaining` among `weights` in proportion, whole numbers by largest remainder,
## ties to the earlier (higher) row.
static func split(weights: Array, remaining: int) -> Array:
	var total := 0
	for w in weights:
		total += int(w)
	var out := []
	if total <= 0:
		for w in weights:
			out.append(0)
		return out
	var rems := []
	var given := 0
	for i in weights.size():
		var q := remaining * int(weights[i])
		out.append(q / total)
		given += q / total
		rems.append({"i": i, "r": q % total})
	rems.sort_custom(func(a, b): return a["r"] > b["r"] or (a["r"] == b["r"] and a["i"] < b["i"]))
	for k in remaining - given:
		out[rems[k % rems.size()]["i"]] += 1
	return out


## Every exit of the sign with its final chance, in table order: [{"id", "label", "chance", "correct"}].
func exit_odds(sign_id: String, ctx: Dictionary) -> Array:
	var exits := _exits(sign_id)
	if exits.is_empty():
		return []
	var correct := correct_chance(sign_id, ctx)
	var wrong_w := []
	for e: Dictionary in exits:
		if not bool(e.get("correct", false)):
			wrong_w.append(int(e.get("weight", 0)))
	var shares := split(wrong_w, 100 - correct)
	var out := []
	var k := 0
	for e: Dictionary in exits:
		var is_c := bool(e.get("correct", false))
		out.append({"id": String(e.get("id", "")), "label": String(e.get("label", "")),
				"chance": correct if is_c else int(shares[k]), "correct": is_c})
		if not is_c:
			k += 1
	return out


## Rolls where the party actually comes out. `draw` 0-99 forces the result (tests); -1 uses the rng.
## Returns {"exit", "label", "correct", "chance", "odds", "granted", "cured"}, or {} for an unknown
## sign. A correct exit adds one success to this visit's count (N4), a wrong one a wrong turn;
## "granted" and "cured" list the status ids the result put on or took off the party.
func roll(sign_id: String, ctx: Dictionary, draw: int = -1) -> Dictionary:
	var odds := exit_odds(sign_id, ctx)
	if odds.is_empty():
		return {}
	var chance := correct_chance(sign_id, ctx)  # before this roll's success counts
	var d := draw if draw >= 0 else rng.randi_range(0, 99)
	var picked: Dictionary = odds[odds.size() - 1]
	var acc := 0
	for e: Dictionary in odds:
		acc += int(e["chance"])
		if d < acc:
			picked = e
			break
	var granted := []
	var cured := []
	if bool(picked["correct"]):
		_after_success(granted, cured)  # reads this visit's wrong turns before anything changes
		state.flags[VISIT_KEY] = successes_this_visit() + 1
	else:
		state.flags[WRONG_KEY] = wrong_turns_this_visit() + 1
		_after_wrong_turn(granted)
	return {"exit": picked["id"], "label": picked["label"], "correct": picked["correct"],
			"chance": chance, "odds": odds, "granted": granted, "cured": cured}


# --- display ------------------------------------------------------------------------------------

## The final correct-exit chance, only while the map item is equipped; -1 otherwise.
func display_chance(sign_id: String, ctx: Dictionary) -> int:
	if not bool(ctx.get("map_equipped", false)):
		return -1
	return correct_chance(sign_id, ctx)


## The intersection readout: "75%" with the map, "" without.
func display_text(sign_id: String, ctx: Dictionary) -> String:
	var c := display_chance(sign_id, ctx)
	return "" if c < 0 else "%d%%" % c
