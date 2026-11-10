class_name DdrJudge
extends RefCounted
## Judges the player's steps against a chart, like real DDR: the closer to the beat, the better.
## Timing windows are DDR's own (Perfect 33 ms, Great 92 ms, Good 142 ms either side).
## A song pays 0-30 tickets by score (ledger, 2026-11-09).

const WINDOWS := [["PERFECT", 0.033], ["GREAT", 0.092], ["GOOD", 0.142]]
## How much of a note's value each judgement earns toward the score.
const WEIGHT := {"PERFECT": 1.0, "GREAT": 0.7, "GOOD": 0.4, "MISS": 0.0}
const MAX_TICKETS := 30

var chart: DdrChart
var counts := {"PERFECT": 0, "GREAT": 0, "GOOD": 0, "MISS": 0}
var combo := 0
var _judged: Array[bool] = []


func _init(c: DdrChart) -> void:
	chart = c
	_judged.resize(c.notes.size())
	_judged.fill(false)


## The player stepped on `lane` at song time `t`. Returns the judgement, or "" if no note was close.
func hit(lane: int, t: float) -> String:
	var best := -1
	var best_dt := float(WINDOWS[-1][1])
	for i in chart.notes.size():
		if _judged[i] or int(chart.notes[i]["lane"]) != lane:
			continue
		var dt := absf(float(chart.notes[i]["time"]) - t)
		if dt <= best_dt:
			best_dt = dt
			best = i
	if best < 0:
		return ""
	_judged[best] = true
	for w in WINDOWS:
		if best_dt <= float(w[1]):
			counts[w[0]] += 1
			combo += 1
			return w[0]
	return ""


## Notes the song has passed without a step become misses. Returns how many just did.
func update(t: float) -> int:
	var missed := 0
	var late := float(WINDOWS[-1][1])
	for i in chart.notes.size():
		if not _judged[i] and float(chart.notes[i]["time"]) + late < t:
			_judged[i] = true
			counts["MISS"] += 1
			missed += 1
	if missed > 0:
		combo = 0
	return missed


func finished() -> bool:
	return not _judged.has(false)


## 0..1: the share of the song's value earned.
func score_ratio() -> float:
	if chart.notes.is_empty():
		return 0.0
	var earned := 0.0
	for k: String in counts.keys():
		earned += counts[k] * float(WEIGHT[k])
	return earned / chart.notes.size()


func tickets() -> int:
	return roundi(MAX_TICKETS * score_ratio())
