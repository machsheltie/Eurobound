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
## "marloes_blessing" (see below), "extra_points" (testing / future modifiers the author rules).
## Rewards the roll tracks itself:
##  - Underground Navigator (Eurobound-gpfc; author 2026-11-13: "After 5 successful navigations
##    (Buffs Earned, :459)"): every correct exit adds one to a lifetime count that leave_tunnel()
##    does not reset; when it reaches "grants.underground_navigator.successes" the roll sets
##    FLAG_UNDERGROUND_NAVIGATOR (permanent +5). The roll that earns it does not get the +5 itself.
##  - Marloes's Blessing (Eurobound-6dx6; author 2026-11-13: "Yes: +20 on the roll for the rest of
##    that tunnel visit"; voetgangerstunnel.md Buffs Earned: buy the map AND follow her advice).
##    Marloes's shop and the "followed her advice" check are not built: whatever builds them calls
##    grant_marloes_blessing() (lasts until leave_tunnel()) or passes ctx "marloes_blessing".
## Statuses the roll grants itself (Eurobound-1esc). The trigger count is in
## assets/data/navigation/voetgangerstunnel.json "grants"; the lengths are the statuses'
## default_duration.clock_minutes in status_effects.json (Eurobound-zcdf), read through
## FieldStatus.table_minutes (null = not ruled = inert):
##  - Tunnel Confusion (voetgangerstunnel.md:438-442): the visit's 3rd wrong turn (count from
##    voetgangerstunnel_items.json:261 and voetgangerstunnel_events.json:343-344) puts it on the whole
##    party for 2 hours of game clock; any successful navigation ends it. A wrong turn while it is
##    on does not refresh it (stacking is not ruled).
##  - Tunnel Vision (:183, :452-455): a success with no wrong turn this visit puts it on the whole
##    party for 1 hour of game clock. Its "+5% Speed underground" has no engine hook (Eurobound-cvkq).
## Eurobound-2xah (docs/superpowers/specs/2026-11-13-contact-high-space-cake-proposal.md, approved
## Eurobound Desk vt7k-q2), numbers in the json "teleport" block and "grants.contact_high":
##  - Space Cake Gamble teleport (T1-T5): see roll().
##  - Coffeeshop Quarter exit (CH2): 30% chance of Contact High on the whole party.

const DATA_PATH := "res://assets/data/navigation/voetgangerstunnel.json"
const SIGN_CENTRAAL := "centraal_station"
const SIGN_MUSEUM_PLEIN := "museum_plein"
## Set by the party's first alcoholic drink since the last rest; cleared at rest.
const SOBER_LOST_KEY := "nav_sober_lost"
const VISIT_KEY := "nav_tunnel_visit_successes"
const WRONG_KEY := "nav_tunnel_visit_wrong_turns"
## Correct exits ever; never reset. Feeds Underground Navigator.
const LIFETIME_KEY := "nav_tunnel_lifetime_successes"
## Marloes's Blessing for the current tunnel visit; cleared on leaving.
const MARLOES_KEY := "nav_marloes_blessing"
const TUNNEL_CONFUSION := "tunnel_confusion"
const TUNNEL_VISION := "tunnel_vision"
## Permanent rewards, read as flags. Opa Cees's is granted by a quest (other work); the roll sets
## Underground Navigator itself.
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
	for path in [[TUNNEL_CONFUSION, "wrong_turns"]]:
		var v: Variant = Dictionary(g.get(path[0], {})).get(path[1], null)
		if v != null and _positive_int(v) < 1:
			errs.append("grants.%s.%s: an int >= 1 or null" % path)
	var un: Variant = g.get(FLAG_UNDERGROUND_NAVIGATOR, null)
	if un is Dictionary:
		var n: Variant = Dictionary(un).get("successes", null)
		if n != null and _positive_int(n) < 1:
			errs.append("grants.underground_navigator.successes: an int >= 1 or null")
	var ch: Variant = g.get(FieldStatus.CONTACT_HIGH, null)
	if ch is Dictionary:
		var pct := _positive_int(Dictionary(ch).get("chance", null))
		if pct < 1 or pct > 100 or String(Dictionary(ch).get("exit", "")).is_empty():
			errs.append("grants.contact_high: needs an exit id and a chance 1-100")
	var tp: Variant = d.get("teleport", null)
	if tp is Dictionary:
		var t: Dictionary = tp
		if String(t.get("status", "")).is_empty():
			errs.append("teleport.status: a status id")
		if not _whole_in(t.get("chance_on_wrong", null), 0, 100):
			errs.append("teleport.chance_on_wrong: a whole number 0-100")
		if not _whole_in(t.get("lost_minutes", null), 0, GameClock.DAY):
			errs.append("teleport.lost_minutes: a whole number >= 0")
	return errs


static func _whole_in(v: Variant, lo: int, hi: int) -> bool:
	return (v is int or v is float) and float(v) == floorf(float(v)) and float(v) >= lo and float(v) <= hi


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


func lifetime_successes() -> int:
	return int(state.flags.get(LIFETIME_KEY, 0))


func has_marloes_blessing() -> bool:
	return bool(state.flags.get(MARLOES_KEY, false))


## Marloes's Blessing for the rest of this tunnel visit. The caller decides the trigger (bought
## the map AND followed her advice); nothing in the engine detects it yet.
func grant_marloes_blessing() -> void:
	state.flags[MARLOES_KEY] = true


func leave_tunnel() -> void:
	state.flags.erase(VISIT_KEY)
	state.flags.erase(WRONG_KEY)
	state.flags.erase(MARLOES_KEY)


# --- statuses the roll grants (Eurobound-1esc) --------------------------------------------------

## A ruled value from "grants", or 0 when it is unruled (null) or missing.
func _grant(status_id: String, key: String) -> int:
	return _positive_int(Dictionary(Dictionary(data.get("grants", {})).get(status_id, {})).get(key, null))


## After a correct exit: ends Tunnel Confusion; grants Tunnel Vision when the visit had no wrong turn.
func _after_success(granted: Array, cured: Array) -> void:
	if FieldStatus.has(state, TUNNEL_CONFUSION):
		FieldStatus.remove(state, TUNNEL_CONFUSION)
		cured.append(TUNNEL_CONFUSION)
	var minutes := FieldStatus.table_minutes(TUNNEL_VISION)
	if wrong_turns_this_visit() == 0 and minutes > 0:
		FieldStatus.apply(state, FieldStatus.PARTY, TUNNEL_VISION, minutes, FieldStatus.UNIT_CLOCK)
		granted.append(TUNNEL_VISION)


## Counts a correct exit toward Underground Navigator; true on the success that earns the flag.
func _count_lifetime_success() -> bool:
	state.flags[LIFETIME_KEY] = lifetime_successes() + 1
	var needed := _grant(FLAG_UNDERGROUND_NAVIGATOR, "successes")
	if needed <= 0 or lifetime_successes() < needed or bool(state.flags.get(FLAG_UNDERGROUND_NAVIGATOR, false)):
		return false
	state.flags[FLAG_UNDERGROUND_NAVIGATOR] = true
	return true


## After a wrong exit: Tunnel Confusion once the visit's wrong turns reach the ruled count.
func _after_wrong_turn(granted: Array) -> void:
	var needed := _grant(TUNNEL_CONFUSION, "wrong_turns")
	var minutes := FieldStatus.table_minutes(TUNNEL_CONFUSION)
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
	if has_marloes_blessing() or bool(ctx.get("marloes_blessing", false)):
		out.append({"id": "marloes_blessing", "points": int(m.get("marloes_blessing", 0))})
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
## "granted" and "cured" list the status ids the result put on or took off the party;
## "underground_navigator_earned" is true on the one roll that sets FLAG_UNDERGROUND_NAVIGATOR.
## `draws` forces the later rolls the same way (tests): "teleport" 0-99, "destination" (an index
## into teleport_destinations), "contact_high" 0-99.
## Teleport (T1-T5): a correct roll is never touched. On a wrong roll, while any bro has the
## teleport status, a second roll replaces the wrong exit with a uniform pick from
## teleport_destinations(); "teleported" is true and "lost_minutes" went onto the game clock. A
## teleport is a wrong turn like any other, and the exit's own consequences apply.
func roll(sign_id: String, ctx: Dictionary, draw: int = -1, draws: Dictionary = {}) -> Dictionary:
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
	var teleported := false
	var lost := 0
	var earned := false
	if bool(picked["correct"]):
		_after_success(granted, cured)  # reads this visit's wrong turns before anything changes
		state.flags[VISIT_KEY] = successes_this_visit() + 1
		earned = _count_lifetime_success()
	else:
		var dest := _teleport(sign_id, draws)
		if not dest.is_empty():
			picked = dest
			teleported = true
			lost = _teleport_value("lost_minutes")
			if lost > 0:  # T5: the half hour is gone before the bros come up
				GameClock.set_time(state, GameClock.minutes(state) + lost)
		state.flags[WRONG_KEY] = wrong_turns_this_visit() + 1
		_after_wrong_turn(granted)
	_exit_grants(String(picked["id"]), draws, granted)
	return {"exit": picked["id"], "label": picked["label"], "correct": picked["correct"],
			"chance": chance, "odds": odds, "granted": granted, "cured": cured,
			"teleported": teleported, "lost_minutes": lost, "underground_navigator_earned": earned}


# --- teleport (Eurobound-2xah; contact-high-space-cake proposal T1-T5) --------------------------

## A whole number >= 0 from the "teleport" block, or 0 when it is missing or not a whole number.
func _teleport_value(key: String) -> int:
	var v: Variant = Dictionary(data.get("teleport", {})).get(key, null)
	if not (v is int or v is float) or float(v) != floorf(float(v)) or float(v) < 0.0:
		return 0
	return int(v)


## T3: every tunnel exit except the followed sign's correct one, in table order, each once:
## [{"id", "label", "correct": false}].
func teleport_destinations(sign_id: String) -> Array:
	var out := []
	var seen := {}
	var signs: Dictionary = data.get("signs", {})
	for e: Dictionary in _exits(sign_id):
		if bool(e.get("correct", false)):
			seen[String(e.get("id", ""))] = true
	for s in signs:
		for e: Dictionary in _exits(String(s)):
			var id := String(e.get("id", ""))
			if seen.has(id):
				continue
			seen[id] = true
			out.append({"id": id, "label": String(e.get("label", "")), "correct": false})
	return out


## T1/T2: the destination a wrong roll is replaced by, or {} when no teleport happens.
func _teleport(sign_id: String, draws: Dictionary) -> Dictionary:
	var status := String(Dictionary(data.get("teleport", {})).get("status", ""))
	var chance := _teleport_value("chance_on_wrong")
	if status.is_empty() or chance <= 0 or not FieldStatus.has(state, status):
		return {}
	var t: int = int(draws["teleport"]) if draws.has("teleport") else rng.randi_range(0, 99)
	if t >= chance:
		return {}
	var dests := teleport_destinations(sign_id)
	if dests.is_empty():
		return {}
	var i: int = int(draws["destination"]) if draws.has("destination") else rng.randi_range(0, dests.size() - 1)
	return dests[clampi(i, 0, dests.size() - 1)]


## CH2: coming up at the Coffeeshop Quarter exit, by a roll or a teleport, is a 30% chance of
## Contact High on the whole party (length and refresh rule from the status table).
func _exit_grants(exit_id: String, draws: Dictionary, granted: Array) -> void:
	var g: Dictionary = Dictionary(data.get("grants", {})).get(FieldStatus.CONTACT_HIGH, {})
	var chance := _positive_int(g.get("chance", null))
	if chance <= 0 or String(g.get("exit", "")) != exit_id:
		return
	var c: int = int(draws["contact_high"]) if draws.has("contact_high") else rng.randi_range(0, 99)
	if c < chance and FieldStatus.apply_from_table(state, FieldStatus.PARTY, FieldStatus.CONTACT_HIGH):
		granted.append(FieldStatus.CONTACT_HIGH)


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
