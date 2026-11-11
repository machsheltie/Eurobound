class_name ArcadeMicrocopy
extends RefCounted
## The Absinthe Arcade's approved microcopy (Writers' Room, approved as final 2026-11-11):
## Jakub "Tokens" Dvořák's ambient mutters and the bros' DDR EXPERT lines. The lines live in
## absinthe_arcade_microcopy.json, verbatim.

const DATA := "res://assets/data/locations/debaucheryville/absinthe_arcade_microcopy.json"

static var _data: Dictionary = {}


static func data() -> Dictionary:
	if _data.is_empty():
		var parsed = JSON.parse_string(FileAccess.get_file_as_string(DATA))
		_data = parsed if parsed is Dictionary else {}
	return _data


## Every mutter Jakub has for one job ("ticket_machine", "token_machine", "restrooms",
## "claw_machines", "shift"); with `late` (after 01:00) his drunk lines join the pool.
static func mutter_pool(job: String, late: bool = false) -> Array:
	var ta: Dictionary = data()["token_attendant"]
	var pool: Array = Array(ta["mutters"].get(job, [])).duplicate()
	if late:
		pool.append_array(ta["late_night_after_0100"])
	return pool


## One mutter, never the line he just said when there's another to pick.
static func mutter(job: String, late: bool, rng: RandomNumberGenerator, last: String = "") -> String:
	var pool := mutter_pool(job, late)
	if pool.size() > 1:
		pool.erase(last)
	return "" if pool.is_empty() else String(pool[rng.randi_range(0, pool.size() - 1)])


## A bro's line when EASY bounces back to EXPERT ("difficulty_bounce") or after a failed EXPERT
## song ("failed_expert_song").
static func ddr_line(moment: String, bro_id: String, rng: RandomNumberGenerator) -> String:
	var lines: Array = data()["ddr_expert"].get(moment, {}).get(bro_id, [])
	return "" if lines.is_empty() else String(lines[rng.randi_range(0, lines.size() - 1)])
