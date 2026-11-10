class_name DdrChart
extends RefCounted
## One DDR song's steps: notes are {"time": seconds from the song's start, "lane": 0-3}
## (0 left, 1 down, 2 up, 3 right, as on the pad), sorted by time.
## Chart files are JSON: {"title", "artist", "audio": "res://...", "notes": [[time, lane], ...]}.

var title := ""
var artist := ""
var audio_path := ""
var notes: Array[Dictionary] = []


static func load_file(path: String) -> DdrChart:
	var c := DdrChart.new()
	var data = JSON.parse_string(FileAccess.get_file_as_string(path))
	if not data is Dictionary:
		push_warning("DDR chart unreadable: " + path)
		return c
	c.title = String(data.get("title", ""))
	c.artist = String(data.get("artist", ""))
	c.audio_path = String(data.get("audio", ""))
	for n in data.get("notes", []):
		c.notes.append({"time": float(n[0]), "lane": int(n[1])})
	c.notes.sort_custom(func(a, b): return a["time"] < b["time"])
	return c


## A chart with one step per beat: `lanes[i]` lands on beat i, the first beat at `first_beat_s`.
static func from_steps(title_: String, bpm: float, first_beat_s: float, lanes: Array) -> DdrChart:
	var c := DdrChart.new()
	c.title = title_
	var beat := 60.0 / bpm
	for i in lanes.size():
		c.notes.append({"time": first_beat_s + i * beat, "lane": int(lanes[i])})
	return c


func length_s() -> float:
	return 0.0 if notes.is_empty() else float(notes[-1]["time"])
