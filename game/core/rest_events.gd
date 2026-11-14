class_name RestEvents
extends RefCounted
## What resting does to live field statuses (Eurobound-5kf4; spec
## docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md section 6). GameClock.rest
## calls run(). Order: each live status's on_rest events, then removals (ends_on_rest, rest cures).
## A status a rest ends hands a battle-only follow-up (Crash) to the next fight
## (FieldStatus.fire_waiting_then; Eurobound-2uji, author 64vo-q2). A row that is itself waiting for
## a fight is not running: its on_rest events do not run, and it ends here only when ends_on_rest
## says so.
## Null params do nothing. The PROPOSED pending flags are only set here and are not registered in
## world_data/quest_flags.json until the author rules them.

const EVENT_DEEP_CLEAN := "deep_clean"
const EVENT_MUNCHIES_TAX := "munchies_tax"


static func run(state) -> void:
	if not ("flags" in state):
		return
	var rows := _live_rows(state)
	for r in rows:
		if String(Dictionary(r["row"]).get("unit", "")) != FieldStatus.UNIT_WAITING:
			_run_events(state, String(r["id"]))
	var ended := []
	for r in rows:
		if _ends_on_rest(String(r["id"]), r["row"]):
			FieldStatus.remove(state, String(r["id"]), String(r["target"]))
			ended.append(r)
	for r in ended:
		FieldStatus.fire_waiting_then(state, String(r["target"]), r["row"], String(r["id"]))


static func _live_rows(state) -> Array:
	var out := []
	var all: Dictionary = FieldStatus._all(state)
	for t in all.keys():
		for id in Dictionary(all[t]).keys():
			if FieldStatus._live(state, all[t][id]):
				out.append({"target": t, "id": id, "row": all[t][id]})
	return out


static func _run_events(state, status_id: String) -> void:
	for ev in Array(StatusTable.entry(status_id).get("on_rest", [])):
		if not (ev is Dictionary):
			continue
		match String(ev.get("event", "")):
			EVENT_DEEP_CLEAN:
				# TODO(Eurobound-5kf4, open: strawberry_shortcake_speedcakes_item.md:150,:153): sorting the
				# inventory and which one item is thrown away are not ruled (never a key item). The
				# consumer of the flag does the work once ruled; here only the pending flag is set.
				_set_flag(state, ev)
			EVENT_MUNCHIES_TAX:
				# TODO(Eurobound-5kf4, open: mango_og_gushers_item.md:118): which food item or how many
				# SOVS the tax takes is not ruled. Only the pending flag is set; nothing is taken.
				_set_flag(state, ev)


static func _set_flag(state, ev: Dictionary) -> void:
	var flag: Variant = ev.get("flag", null)
	if flag is String and not String(flag).is_empty():
		state.flags[flag] = true


## ends_on_rest: the applier's value stored on the row wins, else the table default; null = stays.
## A "rest" cure kind also ends it.
static func _ends_on_rest(status_id: String, row: Dictionary) -> bool:
	var e := StatusTable.entry(status_id)
	for c in Array(e.get("cured_by", [])):
		if c is Dictionary and String(c.get("kind", "")) == "rest":
			return true
	if row.get("ends_on_rest", null) is bool:
		return bool(row["ends_on_rest"])
	return Dictionary(e.get("default_duration", {})).get("ends_on_rest", null) == true
