class_name FieldStatus
extends RefCounted
## Statuses that last OUTSIDE battle (author round v42, arc_systems = all). Kept in the saved
## GameState.flags under "field_status": {target: {status_id: {"unit", "until" | "left"}}}.
## target is a party member id ("lord_pilsner") or PARTY for the whole party.
## Two time units, because the game clock moves only when the bros act:
##  - UNIT_CLOCK: game-clock minutes (GameClock). Stores the expiry minute; expires lazily.
##  - UNIT_REAL: real seconds, for very short effects. Stores seconds left; call tick(state, delta)
##    from a node that runs while the bros walk (PlayerController does).
## Field effects defined by the docs, and only those:
##  - GREEN_FAIRY_CONFUSION reverses movement (the_absinthium_taproom.md 283-287, "Reversed controls").
##  - GREEN_FAIRY_CONFUSION also randomises dialogue choices (same lines; author round v43,
##    fs_confusion_dialogue = both): see choice_index().
##  - EMBARRASSED is a gate other content checks with has() (clawmachinemaintenanceclosetrestroom.md
##    102-117); it has no field effect of its own.

const KEY := "field_status"
const PARTY := "party"
const UNIT_CLOCK := "clock"
const UNIT_REAL := "real"
## UNIT_STEPS (Eurobound-d6yl; author eb8-q1 and 1m4-q1): 1 step = 1 metre walked by the party leader.
## A steps row has TWO independent counters: "left" (steps, ticks on the overworld) and, when the
## status has a battle effect, "turns" (battle turns, ticks in battle). It ends when either hits 0.
## A row without "turns" has no battle counter: no fight ends it and it is not carried into one.
const UNIT_STEPS := "steps"
## 40 steps = 1 battle turn (grist-genever numbers proposal R2, approved eb8-q1).
const STEPS_PER_BATTLE_TURN := 40
const CARRY_KEY := "field_step_carry"
## UNIT_CURED (Eurobound-t162): an until-cured row (Cottonmouth, default_duration.until_cured). It has
## no counter and never expires by time or steps. It ends only by a cure: a rest (RestEvents, via
## cured_by or ends_on_rest) or a drink consumable (cure_by_item). Carried into battle as -1 turns.
## Under stack_rule "extend" the row counts "stacks" (Eurobound-qiof; author, Eurobound Desk 64vo-q3:
## "one drink per Cottonmouth stack"): each curing item takes one stack off and the row ends at 0.
## A rest still ends the whole row. The stat penalty never reads the stack count.
const UNIT_CURED := "cured"
## UNIT_WAITING (Eurobound-2uji; author, Eurobound Desk 64vo-q2: "Battle only: Crash waits for the
## next fight and runs its turns there"): a battle-only status that fired outside a fight. The row
## holds "turns" (battle turns) and nothing else counts: steps, the game clock and real seconds
## never touch it. It is not running on the overworld, so has() and list() do not report it
## (waiting_turns() does). The next fight carries the turns in (battle_statuses) and the remainder
## is written back (write_back_battle); the row ends at 0. A rest ends it only when the table's
## default_duration.ends_on_rest is true (RestEvents).
const UNIT_WAITING := "waiting"

const GREEN_FAIRY_CONFUSION := "green_fairy_confusion"
const EMBARRASSED := "embarrassed"
## Mirror maze Trap Mirror (the_absinthium_taproom.md 94-103): reversed controls for 30 s, like Confusion.
const TRAP_MIRROR := "trap_mirror"

## Contact High and the Space Cake (Eurobound-2xah; approved spec
## docs/superpowers/specs/2026-11-13-contact-high-space-cake-proposal.md, Eurobound Desk vt7k-q2).
## Their lengths, stack rules and the timer's `then` live in status_effects.json. The numbers below
## have no field in the status shape yet (Eurobound-cvkq), so they are constants:
##  - SC5: when the Space Cake Timer lands, the bro gets +40 Bravado per cake (capped at max).
##  - SC6: 15 real seconds of reversed movement at landing, on the TRAP_MIRROR row (movement only;
##    dialogue choices are not shuffled).
##  - SC10: Space Cake Gamble never has more than 180 clock minutes left.
const CONTACT_HIGH := "contact_high"
const SPACE_CAKE_TIMER := "space_cake_timer"
const SPACE_CAKE_GAMBLE := "space_cake_gamble"
const SPACE_CAKE_LANDING_BRAVADO := 40
const SPACE_CAKE_WOBBLE_SECONDS := 15.0
## Status id -> the most clock minutes an "extend" row may have left.
const CLOCK_CAP_MINUTES := {"space_cake_gamble": 180}
## Landings waiting for their cue (rings, warp vignette, "OH." frame): see take_landings().
const LANDINGS_KEY := "field_status_landings"

## Round v43 rulings: fs_into_battle = yes (see battle_statuses), fs_confusion_length = random,
## fs_long_statuses = one_bro (Saw Yourself / Existentially Rested take a member id, no field
## effects), fs_reality_anchor = block (10% chance to block Confusion outright).
const SAW_YOURSELF := "saw_yourself"
const EXISTENTIALLY_RESTED := "existentially_rested"
const REALITY_ANCHOR_KEY := "reality_anchor"
const REALITY_ANCHOR_BLOCK_CHANCE := 0.10

## Round v44 rulings: p_emb_duration = 60min, p_emb_battle = 2turns, p_emb_sources = three,
## p_emb_resist = shorten, b_confusion_battle = 2turns, b_long_statuses_battle = field_only.
const EMBARRASSED_FIELD_MINUTES := 60
const EMBARRASSED_BATTLE_TURNS := 2
const CONFUSION_BATTLE_TURNS := 2
## Each point of Embarrassed resistance shortens it by this fraction. No party member has such a
## stat yet, so callers pass the points (default 0).
const EMBARRASSED_RESIST_STEP := 0.10
## The three causes of Embarrassed. Triggers live in other tasks (closet timer, QTEs, hostel).
const EMB_SOURCE_CLOSET_TIMER := "closet_shame_timer"
const EMB_SOURCE_QTE_FAIL := "qte_fail_npc"
const EMB_SOURCE_HOSTEL_WITNESS := "hostel_witness"
const EMBARRASSED_SOURCES := [EMB_SOURCE_CLOSET_TIMER, EMB_SOURCE_QTE_FAIL, EMB_SOURCE_HOSTEL_WITNESS]
## Turns a carried field status lasts in battle.
const BATTLE_TURNS := {
	"green_fairy_confusion": CONFUSION_BATTLE_TURNS,
	"embarrassed": EMBARRASSED_BATTLE_TURNS,
}

## Field status id -> battle status id (battle statuses live in BattleCore.NEGATIVE etc.).
## Saw Yourself and Existentially Rested have no battle definition, so they are not carried.
const BATTLE_MAP := {
	"green_fairy_confusion": "confused",
	"embarrassed": "embarrassed",
}

## Lengths the docs give. Ranges are {min, max}; the caller picks inside them.
## the_absinthium_taproom.md 283-287: Confusion 30 sec - 3 min, Saw Yourself 1 hour,
## Existentially Rested 2 hours.
const DOC_DURATIONS := {
	"green_fairy_confusion": {"unit": UNIT_REAL, "min": 30, "max": 180},
	"saw_yourself": {"unit": UNIT_CLOCK, "min": 60, "max": 60},
	"existentially_rested": {"unit": UNIT_CLOCK, "min": 120, "max": 120},
}


static func _all(state) -> Dictionary:
	if not state.flags.has(KEY):
		state.flags[KEY] = {}
	return state.flags[KEY]


## Applies (or refreshes) a status. `amount` is minutes for UNIT_CLOCK, seconds for UNIT_REAL.
## Non-positive amounts apply nothing.
static func apply(state, target: String, status_id: String, amount: float, unit: String = UNIT_CLOCK) -> void:
	if amount <= 0.0 or status_id == "":
		return
	var rows: Dictionary = _all(state).get(target, {})
	if unit == UNIT_REAL:
		rows[status_id] = {"unit": UNIT_REAL, "left": amount}
	elif unit == UNIT_STEPS:
		rows[status_id] = {"unit": UNIT_STEPS, "left": int(amount)}
	else:
		rows[status_id] = {"unit": UNIT_CLOCK, "until": GameClock.minutes(state) + int(amount)}
	_all(state)[target] = rows


static func _live(state, row: Dictionary) -> bool:
	if String(row.get("unit", UNIT_CLOCK)) == UNIT_CURED:
		return true
	if String(row.get("unit", UNIT_CLOCK)) == UNIT_WAITING:
		return int(row.get("turns", 0)) > 0
	if String(row.get("unit", UNIT_CLOCK)) == UNIT_STEPS:
		return int(row.get("left", 0)) > 0 and (not row.has("turns") or int(row["turns"]) != 0)
	if String(row.get("unit", UNIT_CLOCK)) == UNIT_REAL:
		return float(row.get("left", 0.0)) > 0.0
	return GameClock.minutes(state) < int(row.get("until", 0))


## True when the target has the status. target "" means anyone: the party or any member.
static func has(state, status_id: String, target: String = "") -> bool:
	var all := _all(state)
	for t in all.keys():
		if target != "" and t != target and t != PARTY:
			continue
		var row: Dictionary = Dictionary(all[t]).get(status_id, {})
		if not row.is_empty() and _running(state, row):
			return true
	return false


## Live and acting on the overworld: a waiting row is kept but is not running.
static func _running(state, row: Dictionary) -> bool:
	return String(row.get("unit", UNIT_CLOCK)) != UNIT_WAITING and _live(state, row)


static func remove(state, status_id: String, target: String = "") -> void:
	var all := _all(state)
	for t in all.keys():
		if target == "" or t == target:
			Dictionary(all[t]).erase(status_id)


## Live status ids on a target (and the whole-party ones); "" lists everything.
static func list(state, target: String = "") -> Array:
	var out := []
	var all := _all(state)
	for t in all.keys():
		if target != "" and t != target and t != PARTY:
			continue
		for id in Dictionary(all[t]).keys():
			if _running(state, all[t][id]) and not out.has(id):
				out.append(id)
	return out


## Drops expired statuses and counts real-second ones down by `delta`. An expired clock row fires
## its `then` (see settle).
static func tick(state, delta: float) -> void:
	var all := _all(state)
	var expired := []
	for t in all.keys():
		var rows: Dictionary = all[t]
		for id in rows.keys():
			var row: Dictionary = rows[id]
			if String(row.get("unit", UNIT_CLOCK)) == UNIT_REAL:
				row["left"] = float(row.get("left", 0.0)) - delta
			if not _live(state, row):
				rows.erase(id)
				if String(row.get("unit", UNIT_CLOCK)) == UNIT_CLOCK:
					expired.append({"target": t, "id": id, "row": row})
		if rows.is_empty():
			all.erase(t)
	for e in expired:
		_clock_expired(state, String(e["target"]), String(e["id"]), e["row"])


## Clock rows expire lazily, so something has to notice: GameClock.set_time calls this after every
## clock change (and tick() does the same while the bros walk). Each expired clock row goes and
## fires its `then`. The follow-up starts at the moment it is noticed. Touches nothing when there
## are no rows.
static func settle(state) -> void:
	if not ("flags" in state) or not state.flags.has(KEY):
		return
	var all: Dictionary = state.flags[KEY]
	var expired := []
	for t in all.keys():
		var rows: Dictionary = all[t]
		for id in rows.keys():
			var row: Dictionary = rows[id]
			if String(row.get("unit", UNIT_CLOCK)) == UNIT_CLOCK and not _live(state, row):
				rows.erase(id)
				expired.append({"target": t, "id": id, "row": row})
		if rows.is_empty():
			all.erase(t)
	for e in expired:
		_clock_expired(state, String(e["target"]), String(e["id"]), e["row"])


## An expired clock row: its `then` starts once per stack (SC10: a second cake joins the timer),
## then the Space Cake Timer's landing hook runs.
static func _clock_expired(state, target: String, status_id: String, row: Dictionary) -> void:
	var count := maxi(1, int(row.get("stacks", 1)))
	var fired := false
	for i in count:
		fired = _fire_then(state, target, row, status_id) or fired
	if fired and status_id == SPACE_CAKE_TIMER:
		_space_cake_landing(state, target, count)


## SC5/SC6: everything lands together. The Gamble itself came from the timer's `then`.
static func _space_cake_landing(state, target: String, cakes: int) -> void:
	if "party" in state:
		for member in state.party:
			if member is Dictionary and String(member.get("id", "")) == target and member.has("max_bravado"):
				member["bravado"] = mini(int(member["max_bravado"]),
						int(member.get("bravado", 0)) + SPACE_CAKE_LANDING_BRAVADO * cakes)
	var wobble: Dictionary = Dictionary(_all(state).get(target, {})).get(TRAP_MIRROR, {})
	if float(wobble.get("left", 0.0)) < SPACE_CAKE_WOBBLE_SECONDS:
		apply(state, target, TRAP_MIRROR, SPACE_CAKE_WOBBLE_SECONDS, UNIT_REAL)
	var queue: Array = state.flags.get(LANDINGS_KEY, [])
	queue.append({"target": target, "status": SPACE_CAKE_TIMER, "count": cakes})
	state.flags[LANDINGS_KEY] = queue


## Landings since the last call, oldest first: [{"target", "status", "count"}]. The scene that plays
## the onset cue takes them; no cue asset exists yet.
static func take_landings(state) -> Array:
	var queue: Array = state.flags.get(LANDINGS_KEY, [])
	state.flags.erase(LANDINGS_KEY)
	return queue


## Green Fairy Confusion or the Trap Mirror: reversed controls.
static func controls_reversed(state) -> bool:
	return has(state, GREEN_FAIRY_CONFUSION) or has(state, TRAP_MIRROR)


## Applies a status counted in steps with an optional battle counter (battle_turns < 0 = none).
## Non-positive steps apply nothing.
static func apply_steps(state, target: String, status_id: String, steps: int, battle_turns: int = -1) -> void:
	if steps <= 0 or status_id == "":
		return
	apply(state, target, status_id, steps, UNIT_STEPS)
	if battle_turns > 0:
		_all(state)[target][status_id]["turns"] = battle_turns


## The status's ruled game-clock length (default_duration.clock_minutes, Eurobound-zcdf; author
## zcdf-q1), or 0 when it is null, missing or not a whole number >= 1.
static func table_minutes(status_id: String) -> int:
	var d: Dictionary = Dictionary(StatusTable.entry(status_id).get("default_duration", {}))
	var v: Variant = d.get("clock_minutes", null)
	if not (v is int or v is float) or float(v) != floorf(float(v)) or float(v) < 1.0:
		return 0
	return int(v)


## Applies a status with the durations in status_effects.json. Null (not tuned yet) numbers apply
## nothing: with no field_steps and no clock_minutes the call is inert and returns false.
## field_steps wins when both are set (no status has both; combining them is not ruled). A
## clock_minutes row is a UNIT_CLOCK row: it counts down on GameClock and has no battle counter.
## `count` is how many stacks arrive. An until-cured status under stack_rule "extend" counts them;
## a battle-only status waits for the next fight with its default battle_turns once per stack under
## "extend" (64vo-q3), once otherwise. Nothing else reads it.
static func apply_from_table(state, target: String, status_id: String, count: int = 1) -> bool:
	var d: Dictionary = Dictionary(StatusTable.entry(status_id).get("default_duration", {}))
	if d.get("until_cured", false) == true:
		apply_until_cured(state, target, status_id, count)
		return true
	if StatusTable.battle_only(status_id):
		# 64vo-q2: it waits for the next fight. Null battle_turns (not tuned yet) = nothing starts.
		var waits: Variant = d.get("battle_turns", null)
		if not (waits is int or waits is float) or int(waits) < 1:
			return false
		return apply_waiting(state, target, status_id, int(waits) * StatusTable.then_length_mult(status_id, count))
	var steps: Variant = d.get("field_steps", null)
	if not (steps is int or steps is float) or int(steps) <= 0:
		var minutes := table_minutes(status_id)
		if minutes <= 0:
			return false
		return _apply_clock_from_table(state, target, status_id, minutes)
	var turns: Variant = d.get("battle_turns", null)
	apply_steps(state, target, status_id, int(steps), int(turns) if (turns is int or turns is float) else -1)
	return true


## A clock row from the table, honouring the entry's stack_rule on the target's own live row:
##  - then.stacks true: the running row keeps its expiry and counts one more stack (a second Space
##    Cake joins the timer); a new row starts at 1 stack.
##  - "none": a live row is left alone (returns false).
##  - "extend": the minutes are added to what is left, up to CLOCK_CAP_MINUTES when one is ruled.
##  - "refresh" or not ruled (null): the row restarts at its full length.
static func _apply_clock_from_table(state, target: String, status_id: String, minutes: int) -> bool:
	var e := StatusTable.entry(status_id)
	var then: Variant = e.get("then", null)
	var stacks: bool = then is Dictionary and Dictionary(then).get("stacks", false) == true
	var own: Dictionary = Dictionary(_all(state).get(target, {})).get(status_id, {})
	var live := not own.is_empty() and String(own.get("unit", UNIT_CLOCK)) == UNIT_CLOCK and _live(state, own)
	var rule: Variant = e.get("stack_rule", null)
	if live and stacks:
		own["stacks"] = int(own.get("stacks", 1)) + 1
		return true
	if live and rule is String and rule == "none":
		return false
	var now := GameClock.minutes(state)
	if live and rule is String and rule == "extend":
		var until := int(own["until"]) + minutes
		if CLOCK_CAP_MINUTES.has(status_id):
			until = mini(until, now + int(CLOCK_CAP_MINUTES[status_id]))
		own["until"] = until
		return true
	apply(state, target, status_id, minutes, UNIT_CLOCK)
	if stacks:
		_all(state)[target][status_id]["stacks"] = 1
	return true


## Holds `turns` battle turns of a battle-only status for the next fight. On a row already
## waiting, the entry's stack_rule decides, as it does for clock rows: "extend" adds the turns,
## "none" leaves it alone (returns false), "refresh" or not ruled restarts it at `turns`.
static func apply_waiting(state, target: String, status_id: String, turns: int) -> bool:
	if status_id == "" or turns <= 0:
		return false
	var rows: Dictionary = _all(state).get(target, {})
	var own: Dictionary = rows.get(status_id, {})
	var live := not own.is_empty() and String(own.get("unit", UNIT_CLOCK)) == UNIT_WAITING and _live(state, own)
	var rule: Variant = StatusTable.entry(status_id).get("stack_rule", null)
	if live and rule is String and rule == "none":
		return false
	if live and rule is String and rule == "extend":
		own["turns"] = int(own["turns"]) + turns
		return true
	rows[status_id] = {"unit": UNIT_WAITING, "turns": turns}
	_all(state)[target] = rows
	return true


## Battle turns the target's OWN waiting row holds for the next fight; 0 when it has none.
static func waiting_turns(state, target: String, status_id: String) -> int:
	var row: Dictionary = Dictionary(_all(state).get(target, {})).get(status_id, {})
	if row.is_empty() or String(row.get("unit", UNIT_CLOCK)) != UNIT_WAITING:
		return 0
	return maxi(int(row.get("turns", 0)), 0)


## Applies an until-cured row. Re-applying keeps the existing row (and its ends_on_rest). Under
## stack_rule "extend" the row counts stacks: a new row starts at `stacks`, a live one gains them.
static func apply_until_cured(state, target: String, status_id: String, stacks: int = 1) -> void:
	if status_id == "":
		return
	var extend := StatusTable.stacks_extend(status_id)
	var rows: Dictionary = _all(state).get(target, {})
	if not rows.has(status_id) or String(Dictionary(rows[status_id]).get("unit", "")) != UNIT_CURED:
		rows[status_id] = {"unit": UNIT_CURED}
		if extend:
			rows[status_id]["stacks"] = maxi(stacks, 1)
	elif extend:
		rows[status_id]["stacks"] = maxi(int(rows[status_id].get("stacks", 1)), 1) + maxi(stacks, 1)
	_all(state)[target] = rows


## Stacks on the target's OWN until-cured row: 0 when it has none, else at least 1.
static func stack_count(state, target: String, status_id: String) -> int:
	var row: Dictionary = Dictionary(_all(state).get(target, {})).get(status_id, {})
	if row.is_empty() or String(row.get("unit", UNIT_CLOCK)) != UNIT_CURED:
		return 0
	return maxi(int(row.get("stacks", 1)), 1)


## Stack counts (battle status id -> stacks) of a member's until-cured rows that go into battle.
## The fight reads them at BattleCore.start(); battle_statuses() carries the -1.
static func battle_stacks(state, member_id: String) -> Dictionary:
	var out := {}
	for entry in _rows_for(state, member_id):
		var r: Dictionary = entry["row"]
		if String(r.get("unit", UNIT_CLOCK)) == UNIT_CURED and StatusTable.in_battle(String(entry["id"])):
			var bid := String(BATTLE_MAP.get(entry["id"], entry["id"]))
			out[bid] = maxi(int(out.get(bid, 0)), maxi(int(r.get("stacks", 1)), 1))
	return out


## Ends every live row the item cures (StatusTable.cured_by_item: item_id or drink subtype),
## on `target` and the whole party. `target` "" = every target. Cures rows of every unit.
## An until-cured row with more than one stack loses one stack instead and stays (64vo-q3).
## Returns the status ids removed.
static func cure_by_item(state, target: String, item_id: String, item: Dictionary) -> Array:
	var removed := []
	var hits := []
	for entry in (_rows_for(state, target) if target != "" else _rows_for_all(state)):
		var id := String(entry["id"])
		if _live(state, entry["row"]) and StatusTable.cured_by_item(id, item_id, item):
			hits.append(entry)
	for entry in hits:
		var hit_row: Dictionary = entry["row"]
		if String(hit_row.get("unit", UNIT_CLOCK)) == UNIT_CURED and int(hit_row.get("stacks", 1)) > 1:
			hit_row["stacks"] = int(hit_row["stacks"]) - 1
			continue
		Dictionary(_all(state)[entry["target"]]).erase(entry["id"])
		if not removed.has(entry["id"]):
			removed.append(entry["id"])
	return removed


static func _rows_for_all(state) -> Array:
	var out := []
	var all := _all(state)
	for t in all.keys():
		for id in all[t].keys():
			out.append({"target": t, "id": id, "row": all[t][id]})
	return out


static func turns_to_steps(turns: int) -> int:
	return turns * STEPS_PER_BATTLE_TURN


static func steps_to_turns(steps: int) -> int:
	return steps / STEPS_PER_BATTLE_TURN


## Counts `n` steps off every steps row; expired rows go. Overworld only: battle never calls it.
## A row hidden by a "timer": "pause" suppress rule does not count down (author, Eurobound Desk
## 64vo-q6: "Pause: the timer stops while hidden and picks up again when it returns"). Who is
## hidden is settled before anything ticks.
static func add_steps(state, n: int) -> void:
	if n <= 0:
		return
	var all := _all(state)
	var paused := {}
	for t in all.keys():
		var live := {}
		for id in list(state, String(t)):
			live[id] = true
		paused[t] = Dictionary(all[t]).keys().filter(func(s) -> bool: return StatusTable.timer_paused(String(s), live))
	var expired := []
	for t in all.keys():
		var rows: Dictionary = all[t]
		for id in rows.keys():
			var row: Dictionary = rows[id]
			if String(row.get("unit", UNIT_CLOCK)) == UNIT_STEPS and not Array(paused[t]).has(id):
				row["left"] = int(row.get("left", 0)) - n
				if not _live(state, row):
					rows.erase(id)
					expired.append({"target": t, "id": id, "row": row})
		if rows.is_empty():
			all.erase(t)
	for e in expired:
		_fire_then(state, String(e["target"]), e["row"], String(e["id"]))


## An expired row's `then` status starts from the status table's defaults. The row's own `then`
## (Intoxicant.apply_field) wins; without one, the status's table entry is read (Eurobound-2xah).
## Null defaults are inert: nothing starts (Eurobound-umy). Returns true when something started.
## The follow-up arrives with the row's then.stacks_count stacks (Intoxicant.apply_field), doubled
## when the ended status has a live "modify_then" / "double_stacks" rule (64vo-q4).
static func _fire_then(state, target: String, row: Dictionary, status_id: String = "") -> bool:
	var t: Variant = row.get("then", null)
	if not (t is Dictionary) and status_id != "":
		t = StatusTable.entry(status_id).get("then", null)
	if t is Dictionary and Dictionary(t).get("status", null) is String and not String(t["status"]).is_empty():
		var live := {}
		for id in list(state, target):
			live[id] = true
		var count := maxi(int(Dictionary(t).get("stacks_count", 1)), 1)
		count *= StatusTable.then_stack_mult(status_id, String(t["status"]), live)
		return apply_from_table(state, target, String(t["status"]), count)
	return false


## A row a rest just ended: its `then` starts only when it is a battle-only status, which then
## waits for the next fight (64vo-q2; the Crash "Fires when Sugar Rush Hour ends"). No ruling has a
## field follow-up start at a rest, so those stay as they were. Returns true when one was held.
static func fire_waiting_then(state, target: String, row: Dictionary, status_id: String) -> bool:
	var t: Variant = row.get("then", null)
	if not (t is Dictionary):
		t = StatusTable.entry(status_id).get("then", null)
	if t is Dictionary and Dictionary(t).get("status", null) is String and StatusTable.battle_only(String(t["status"])):
		return _fire_then(state, target, row, status_id)
	return false


## Adds metres walked by the party leader; whole metres become steps (the fraction carries).
## Returns the steps counted.
static func add_metres(state, metres: float) -> int:
	if metres <= 0.0:
		return 0
	var total := float(state.flags.get(CARRY_KEY, 0.0)) + metres
	var whole := int(floor(total))
	state.flags[CARRY_KEY] = total - whole
	add_steps(state, whole)
	return whole


## Battle statuses (id -> turns left) for a member's live field statuses (fs_into_battle).
## Both carried statuses last 2 turns in battle (v44), then are gone.
static func battle_statuses(state, member_id: String) -> Dictionary:
	var out := {}
	for id in list(state, member_id):
		if BATTLE_MAP.has(id):
			out[BATTLE_MAP[id]] = BATTLE_TURNS[id]
	# Steps rows carry their real remaining battle turns, never -1. No "turns" = no battle counter.
	for row in _rows_for(state, member_id):
		var r: Dictionary = row["row"]
		if String(r.get("unit", UNIT_CLOCK)) == UNIT_CURED and StatusTable.in_battle(String(row["id"])):
			out[String(BATTLE_MAP.get(row["id"], row["id"]))] = -1
			continue
		if String(r.get("unit", UNIT_CLOCK)) == UNIT_WAITING and _live(state, r):
			# 64vo-q2: the waiting status runs its turns in this fight.
			out[String(BATTLE_MAP.get(row["id"], row["id"]))] = int(r["turns"])
			continue
		if String(r.get("unit", UNIT_CLOCK)) == UNIT_STEPS and r.has("turns") and _live(state, r):
			out[String(BATTLE_MAP.get(row["id"], row["id"]))] = int(r["turns"])
	return out


## Rows ({"target", "id", "row"}) that apply to a member: its own and the whole party's.
static func _rows_for(state, member_id: String) -> Array:
	var out := []
	var all := _all(state)
	for t in all.keys():
		if t != member_id and t != PARTY:
			continue
		for id in all[t].keys():
			out.append({"target": t, "id": id, "row": all[t][id]})
	return out


## After a fight: writes a bro's remaining battle turns back to his steps rows (the remainder, not
## the carried-in value). A carried status that is gone from the unit has run out its turns and
## ends. A -1 (until cured) leaves the row alone. A whole-party row only ever shrinks, so the bro
## with the fewest turns left sets it. Rows with no battle counter are untouched. A waiting row
## (battle-only status) is treated the same way: its remainder stays for the fight after.
## `stacks` (battle status id -> stacks, BattleUnit.status_stacks) sets a bro's own until-cured row
## to what he left the fight with; a whole-party row only shrinks. An until-cured status that started
## in the fight and has field scope gets its row here: the end of a fight is not a cure.
static func write_back_battle(state, member_id: String, battle_statuses: Dictionary, stacks: Dictionary = {}) -> void:
	var all := _all(state)
	var cured_rows := {}
	var ended := []
	for entry in _rows_for(state, member_id):
		var r: Dictionary = entry["row"]
		if String(r.get("unit", UNIT_CLOCK)) == UNIT_CURED:
			var cid := String(BATTLE_MAP.get(entry["id"], entry["id"]))
			cured_rows[cid] = true
			# Carried in as -1; a drink in the fight that cured it removed it from the unit.
			if StatusTable.in_battle(String(entry["id"])) and not battle_statuses.has(cid):
				Dictionary(all[entry["target"]]).erase(entry["id"])
			elif r.has("stacks") and int(stacks.get(cid, 0)) >= 1:
				if String(entry["target"]) == member_id:
					r["stacks"] = int(stacks[cid])
				else:
					r["stacks"] = mini(int(r["stacks"]), int(stacks[cid]))
			continue
		var waiting := String(r.get("unit", UNIT_CLOCK)) == UNIT_WAITING
		if not waiting and (String(r.get("unit", UNIT_CLOCK)) != UNIT_STEPS or not r.has("turns")):
			continue
		var bid := String(BATTLE_MAP.get(entry["id"], entry["id"]))
		var left := int(battle_statuses.get(bid, 0))
		if left < 0:
			continue
		r["turns"] = mini(int(r["turns"]), left)
		if int(r["turns"]) <= 0:
			Dictionary(all[entry["target"]]).erase(entry["id"])
			ended.append(entry)
	# Follow-ups start after every row has its remainder, so a status that starts waiting here
	# (2uji) is not cut down by this same fight's numbers.
	for entry in ended:
		_fire_then(state, String(entry["target"]), entry["row"], String(entry["id"]))
	for bid in battle_statuses.keys():
		var sid := String(bid)
		if int(battle_statuses[bid]) < 0 and not cured_rows.has(sid) and StatusTable.until_cured(sid) \
				and Array(StatusTable.entry(sid).get("scope", [])).has("field"):
			apply_until_cured(state, member_id, sid, maxi(int(stacks.get(sid, 1)), 1))


## Applies Embarrassed for 60 game-minutes, shortened 10% per resistance point.
## Returns false for an unknown source or when resistance leaves no time.
static func apply_embarrassed(state, member_id: String, source: String, resistance: float = 0.0) -> bool:
	if not EMBARRASSED_SOURCES.has(source):
		return false
	var minutes := int(round(EMBARRASSED_FIELD_MINUTES * (1.0 - EMBARRASSED_RESIST_STEP * maxf(resistance, 0.0))))
	if minutes <= 0:
		return false
	apply(state, member_id, EMBARRASSED, minutes, UNIT_CLOCK)
	return true


## Whole-party Reality Anchor is not ruled; the flag is per member.
static func grant_reality_anchor(state, member_id: String) -> void:
	var d: Dictionary = state.flags.get(REALITY_ANCHOR_KEY, {})
	d[member_id] = true
	state.flags[REALITY_ANCHOR_KEY] = d


static func has_reality_anchor(state, member_id: String) -> bool:
	return bool(Dictionary(state.flags.get(REALITY_ANCHOR_KEY, {})).get(member_id, false))


## A random whole-second length inside the doc range for `status_id`.
static func random_amount(status_id: String, rng: RandomNumberGenerator) -> float:
	var d: Dictionary = DOC_DURATIONS[status_id]
	return float(rng.randi_range(int(d["min"]), int(d["max"])))


## Applies Green Fairy Confusion to one bro for a random 30 s - 3 min. A bro with Reality
## Anchor blocks it outright 10% of the time. Returns true when it was applied.
static func apply_confusion(state, member_id: String, rng: RandomNumberGenerator = null) -> bool:
	if rng == null:
		rng = RandomNumberGenerator.new()
		rng.randomize()
	if has_reality_anchor(state, member_id) and rng.randf() < REALITY_ANCHOR_BLOCK_CHANCE:
		return false
	apply(state, member_id, GREEN_FAIRY_CONFUSION, random_amount(GREEN_FAIRY_CONFUSION, rng), UNIT_REAL)
	return true


static func apply_saw_yourself(state, member_id: String) -> void:
	apply(state, member_id, SAW_YOURSELF, DOC_DURATIONS[SAW_YOURSELF]["min"], UNIT_CLOCK)


static func apply_existentially_rested(state, member_id: String) -> void:
	apply(state, member_id, EXISTENTIALLY_RESTED, DOC_DURATIONS[EXISTENTIALLY_RESTED]["min"], UNIT_CLOCK)


## Confusion randomises dialogue: the index actually taken for a choice of `count` options.
static func choice_index(state, picked: int, count: int, rng: RandomNumberGenerator = null) -> int:
	if state == null or count <= 1 or not has(state, GREEN_FAIRY_CONFUSION):
		return picked
	if rng == null:
		rng = RandomNumberGenerator.new()
		rng.randomize()
	return rng.randi_range(0, count - 1)
