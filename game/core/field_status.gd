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

const GREEN_FAIRY_CONFUSION := "green_fairy_confusion"
const EMBARRASSED := "embarrassed"
## Mirror maze Trap Mirror (the_absinthium_taproom.md 94-103): reversed controls for 30 s, like Confusion.
const TRAP_MIRROR := "trap_mirror"

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
	else:
		rows[status_id] = {"unit": UNIT_CLOCK, "until": GameClock.minutes(state) + int(amount)}
	_all(state)[target] = rows


static func _live(state, row: Dictionary) -> bool:
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
		if not row.is_empty() and _live(state, row):
			return true
	return false


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
			if _live(state, all[t][id]) and not out.has(id):
				out.append(id)
	return out


## Drops expired statuses and counts real-second ones down by `delta`.
static func tick(state, delta: float) -> void:
	var all := _all(state)
	for t in all.keys():
		var rows: Dictionary = all[t]
		for id in rows.keys():
			var row: Dictionary = rows[id]
			if String(row.get("unit", UNIT_CLOCK)) == UNIT_REAL:
				row["left"] = float(row.get("left", 0.0)) - delta
			if not _live(state, row):
				rows.erase(id)
		if rows.is_empty():
			all.erase(t)


## Green Fairy Confusion or the Trap Mirror: reversed controls.
static func controls_reversed(state) -> bool:
	return has(state, GREEN_FAIRY_CONFUSION) or has(state, TRAP_MIRROR)


## Battle statuses (id -> turns left) for a member's live field statuses (fs_into_battle).
## Both carried statuses last 2 turns in battle (v44), then are gone.
static func battle_statuses(state, member_id: String) -> Dictionary:
	var out := {}
	for id in list(state, member_id):
		if BATTLE_MAP.has(id):
			out[BATTLE_MAP[id]] = BATTLE_TURNS[id]
	return out


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
