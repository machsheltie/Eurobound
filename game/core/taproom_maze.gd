class_name TaproomMaze
extends RefCounted
## The Absinthium Taproom mirror maze (design/worlds/debaucheryville/the_absinthium_taproom.md
## 63-68, 94-103, 140-150; author round v41-42, v44). Pure logic: which mirror is in which niche per
## section (data: assets/data/taproom_maze/sections.json) and what using one does. The rooms
## (absinthe_arcade_taproom_maze_*_hd2d) only dress and route.
## Run state lives in GameState.flags[RUN_KEY] = {"section": int, "confused": bool, "layout": {}}.
## Author round v45: the layout in sections.json is used as-is until the bros use ANY Truth Mirror
## for the first time (FLAG_TRUTH_USED). After that every NEW entry through the curtain (start_run)
## shuffles each section's mirror types across its niches (same composition) and stores the result
## in the run state as "layout" ({"<section id>": {niche: type}}), so a portal hop, a section change
## or a save mid-visit keeps it. The maze is walked on every visit, solved or not (v44 + v45).

const DATA_PATH := "res://assets/data/taproom_maze/sections.json"
const RUN_KEY := "taproom_maze_run"
const FLAG_COMPLETED := "maze_completed"
const FLAG_TRUTH_USED := "maze_truth_used"
const BREWERY_ID := "absinthium_taproom"
const CHAD_SECTION := 3
const BROS := ["lord_pilsner", "chadwick", "bradley"]

const TRUE_M := "true"
const PORTAL := "portal"
const TRAP := "trap"
const CONFUSION := "confusion"
const TRUTH := "truth"
const TYPES := [TRUE_M, PORTAL, TRAP, CONFUSION, TRUTH]

var data: Dictionary
var state
var rng: RandomNumberGenerator
var section := 1
var confused := false
var chad_done := false  ## Mirror Chad already started this visit (v45: section 3, once per visit)
var layout := {}  ## this visit's shuffled niches; empty = the data's fixed layout
var reveal_left := 0.0


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
	var run: Dictionary = state.flags.get(RUN_KEY, {})
	section = clampi(int(run.get("section", 1)), 1, section_count())
	confused = bool(run.get("confused", false))
	chad_done = bool(run.get("chad_done", false))
	var saved = run.get("layout", {})
	layout = saved.duplicate(true) if saved is Dictionary else {}


## Errors against the design doc 140-146; empty = valid.
static func validate(d: Dictionary) -> Array:
	var errs := []
	var secs: Array = d.get("sections", [])
	if secs.size() != 5:
		errs.append("needs 5 sections, has %d" % secs.size())
	for s: Dictionary in secs:
		var counts := {}
		var niches: Dictionary = s.get("niches", {})
		for t in niches.values():
			counts[t] = int(counts.get(t, 0)) + 1
			if not TYPES.has(t):
				errs.append("section %s: unknown mirror type %s" % [s.get("id"), t])
		var exit_is_true := String(s.get("exit", "")) != ""
		var n_true := int(counts.get(TRUE_M, 0)) + (1 if exit_is_true else 0)
		var n_trap := int(counts.get(TRAP, 0)) + int(counts.get(CONFUSION, 0))
		var total := niches.size() + (1 if exit_is_true else 0)
		if exit_is_true:
			total -= 1  # the archway is not a mirror
		if total < 4 or total > 6:
			errs.append("section %s: %d mirrors (needs 4-6)" % [s.get("id"), total])
		if n_true != 1:
			errs.append("section %s: %d True exits (needs 1)" % [s.get("id"), n_true])
		if int(counts.get(PORTAL, 0)) < 2 or int(counts.get(PORTAL, 0)) > 3:
			errs.append("section %s: %d Portal (needs 2-3)" % [s.get("id"), int(counts.get(PORTAL, 0))])
		if n_trap < 1 or n_trap > 2:
			errs.append("section %s: %d Trap/Confusion (needs 1-2)" % [s.get("id"), n_trap])
		if int(counts.get(TRUTH, 0)) != 1:
			errs.append("section %s: %d Truth (needs 1)" % [s.get("id"), int(counts.get(TRUTH, 0))])
	return errs


func section_count() -> int:
	return Array(data.get("sections", [])).size()


func section_data(n: int = -1) -> Dictionary:
	return Array(data.get("sections", []))[(section if n < 0 else n) - 1]


func plate_of(n: int = -1) -> String:
	return String(section_data(n).get("plate", "m1"))


## The niche -> mirror type map in effect for section n (this visit's shuffle, else the data).
func niches_of(n: int = -1) -> Dictionary:
	var sec := section_data(n)
	var key := str(int(sec.get("id", section if n < 0 else n)))
	if layout.has(key):
		return layout[key]
	return sec.get("niches", {})


func mirror_at(niche_id: String) -> String:
	return String(niches_of().get(niche_id, ""))


func _save_run() -> void:
	state.flags[RUN_KEY] = {"section": section, "confused": confused, "layout": layout, "chad_done": chad_done}


## Permutes each section's mirror types across its niches (Fisher-Yates on the seeded rng), keeping
## composition. Re-rolls if the result equals the fixed base everywhere.
func shuffled_layout() -> Dictionary:
	for _attempt in 20:
		var out := {}
		var changed := false
		for sec: Dictionary in data.get("sections", []):
			var base: Dictionary = sec.get("niches", {})
			var ids: Array = base.keys()
			var types: Array = base.values()
			for i in range(types.size() - 1, 0, -1):
				var j := rng.randi_range(0, i)
				var tmp = types[i]
				types[i] = types[j]
				types[j] = tmp
			var m := {}
			for i in ids.size():
				m[ids[i]] = types[i]
				if types[i] != base[ids[i]]:
					changed = true
			out[str(int(sec.get("id", 0)))] = m
		if changed:
			return out
	return {}


## Entering from the curtain: a fresh run at section 1. Fixed layout until a Truth Mirror has been
## used, a fresh shuffle for this visit afterwards.
func start_run() -> void:
	section = 1
	confused = false
	chad_done = false
	reveal_left = 0.0
	layout = shuffled_layout() if bool(state.flags.get(FLAG_TRUTH_USED, false)) else {}
	_save_run()


## Author v45 (fight_mirror_chad: "In the maze, around section 3 or 4"; section 3 is the pick):
## Mirror Chad starts the first time in a visit the bros are in section 3, until he is defeated.
func chad_due() -> bool:
	return section == CHAD_SECTION and not chad_done \
			and not bool(state.flags.get(TaproomBattle.FLAG_MIRROR_CHAD_DEFEATED, false))


## True once per visit when Mirror Chad is due; marks him started so a loss does not re-trigger him
## in the same visit (the next start_run clears it). The layout and section stay as they were.
func take_chad() -> bool:
	if not chad_due():
		return false
	chad_done = true
	_save_run()
	return true


func revealed() -> bool:
	return reveal_left > 0.0


func tick(delta: float) -> void:
	if reveal_left > 0.0:
		reveal_left = maxf(reveal_left - delta, 0.0)


func _go(n: int) -> void:
	section = n
	reveal_left = 0.0
	_save_run()


## Uses the mirror in a niche. Returns {"type", "action", "section"}; action is "none", "section"
## (re-dress / change plate for `section`) or "status".
func use_niche(niche_id: String) -> Dictionary:
	var t := mirror_at(niche_id)
	var out := {"type": t, "action": "none", "section": section}
	match t:
		TRUE_M:
			_go(section + 1)
			out["action"] = "section"
		PORTAL:
			var others := []
			for i in range(1, section_count() + 1):
				if i != section:
					others.append(i)
			_go(others[rng.randi_range(0, others.size() - 1)])
			out["action"] = "section"
		TRAP:
			FieldStatus.apply(state, FieldStatus.PARTY, FieldStatus.TRAP_MIRROR,
					float(data.get("trap_seconds", 30.0)), FieldStatus.UNIT_REAL)
			out["action"] = "status"
		CONFUSION:
			for id in BROS:
				if FieldStatus.apply_confusion(state, id, rng):
					confused = true
			_save_run()
			out["action"] = "status"
		TRUTH:
			reveal_left = float(data.get("truth_reveal_seconds", 10.0))
			state.flags[FLAG_TRUTH_USED] = true
			out["action"] = "status"
	out["section"] = section
	return out


## Leaving by the True exit of the last section (the open archway). Placeholder per round v44:
## Reality Anchor goes to the whole party (b_reality_anchor = party) when no Confusion was applied.
func use_exit() -> Dictionary:
	# Rewards once only: finishing again (the maze is walked every visit) awards nothing new.
	if bool(state.flags.get(FLAG_COMPLETED, false)):
		state.flags.erase(RUN_KEY)
		return {"type": TRUE_M, "action": "exit", "anchored": false, "repeat": true}
	state.flags[FLAG_COMPLETED] = true
	BreweryPassport.award_opener(state, BREWERY_ID)
	var anchored := not confused
	if anchored:
		for id in BROS:
			FieldStatus.grant_reality_anchor(state, id)
	state.flags.erase(RUN_KEY)
	return {"type": TRUE_M, "action": "exit", "anchored": anchored}
