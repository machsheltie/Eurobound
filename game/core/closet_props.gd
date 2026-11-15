class_name ClosetProps
extends RefCounted
## The Claw Machine Maintenance Closet Restroom's props: examine lines, use beats, CRT read-outs, the
## shame-timer announcer and the graffiti read-outs. Text is the Writers' Room final, approved by the
## author (Desk Eurobound-3ho-q4), verbatim from
## WritingRoom/tasks/20261112_1419_absinthe_arcade_completion_lines/final.md section 1 (L13-74).
## Pure data and logic; the room (absinthe_arcade_maintenance_closet_hd2d.gd) shows the lines.
## Alternates at final.md L31 and L52 do NOT ship.

const DDR_TOILET := "ddr_toilet"
const CRT_MIRROR := "crt_mirror"
const SOCK_CHUTE := "sock_chute"
const SPARKING_WIRING := "sparking_wiring"
const GRAFFITI_SMAAAASH := "graffiti_smaaaash"
const GRAFFITI_CHEAT_CODES := "graffiti_cheat_codes"
const GRAFFITI_HAIKU := "graffiti_tekken_haiku"
const GRAFFITI_BOOBS := "graffiti_pixel_boobs"
const GRAFFITI_JOYSTICK := "graffiti_joystick_lips"

const IDS := [DDR_TOILET, CRT_MIRROR, SOCK_CHUTE, SPARKING_WIRING, GRAFFITI_SMAAAASH,
	GRAFFITI_CHEAT_CODES, GRAFFITI_HAIKU, GRAFFITI_BOOBS, GRAFFITI_JOYSTICK]

## Speaker "" = plain microcopy (no title in the box).
const NO_SPEAKER := ""

const EXAMINE := {
	DDR_TOILET: "A DDR dance pad bolted over a toilet bowl. Sticky, but it still registers your weight as a PERFECT.",
	CRT_MIRROR: "The mirror is a dead arcade screen. INSERT COIN scrolls across your reflection on a loop, forever.",
	SOCK_CHUTE: "The paper-towel dispenser is a claw-machine prize chute. It only dispenses other men's socks. Used.",
	SPARKING_WIRING: "Exposed wiring snakes across the wall and spits a spark when you lean in. The fire code here is a rumor.",
	GRAFFITI_SMAAAASH: "Highlighter ink, under the blacklight. Whoever wrote it meant every word.",
	GRAFFITI_CHEAT_CODES: "A wall of cheat codes. Half are fake. Half of the fake ones are for games that don't exist. One is just a threat.",
	GRAFFITI_BOOBS: "Crude pixel-art boobs, rendered with the confidence of a man who had exactly four colors and one idea.",
	GRAFFITI_JOYSTICK: "A pixel joystick with lips, glowing faintly. It only shows itself to the already-humiliated. Of course.",
}

## DDR-arrow toilet, on use (final.md L18-20). The SFX direction has no on-screen text.
const DDR_USE: Array = [
	{"who": "Bradley", "line": "Bro, it's got combo scoring. I'm gonna get a full streak."},
	{"who": "Chadwick", "line": "Do the down arrow again. The sound it makes is insane."},
]
const SOCK_USE := "It thunk-clunks and drops a single sock, damp, with a foreign gym logo. There is no way to dry your hands. There never was."

## CRT read-outs, cycling on repeat inspection (final.md L27-29).
const CRT_READOUTS: Array = [
	"GAME OVER — YOUR DIGNITY HAS EXPIRED",
	"HI-SCORE TABLE — 1ST: YOU — 0 PTS — RANK: TOURIST",
	"PLEASE INSERT FACE",
]

## Shame timer: a line per 30 seconds overstayed, cycling (final.md L48-50).
const SHAME_INTERVAL_S := 30.0
const SHAME_LINES: Array = [
	"You've achieved nothing but shame, player one.",
	"Still here. New personal best. Your mother is so proud, player one.",
	"Achievement unlocked: Loiterer.",
]

## Tekken haiku (final.md L64-66, author-approved) and its read-out (L68).
const HAIKU: Array = [
	"She said \"PERFECT\" twice.",
	"when the combo was over",
	"she meant the combo",
]
const HAIKU_READOUT := "Highlighter ink. Underlined twice."

## Sparking-wiring zaps (author, Desk bcnr-q9: "Sparks, and a bro gets zapped (a joke line) if you walk
## too close; no game"). Lines are the Writers' Room final, author-approved as 4-line pools (Desk
## Eurobound-ms3r-q1), verbatim from WritingRoom/tasks/20261114_1826_claw_closet_sparking_wiring_zap_barks/
## final.md. The leader says one as a floating bark: no box, no reply, no flinch, no damage. A
## cooldown keeps it from firing every step, and no line or beat comes twice in a row.
const ZAP_RANGE_TILES := 1.2
const ZAP_COOLDOWN_S := 20.0
const ZAP_SHOW_S := 3.5
const ZAP_LINES := {
	"lord_pilsner": [
		{"line": "That's the local specialty, boys.", "beat": "order"},
		{"line": "I'll take two of those.", "beat": "order"},
		{"line": "Somebody's getting a raise for this.", "beat": "staff"},
		{"line": "Heh. This place treats a man right.", "beat": "staff"},
	],
	"chadwick": [
		{"line": "Dude, did that go in the video? Tell me yes.", "beat": "footage"},
		{"line": "Dude. That's the intro. That's my intro now.", "beat": "footage"},
		{"line": "Four hundred people are gonna love this.", "beat": "rating"},
		{"line": "This beats the dorm prank.", "beat": "rating"},
	],
	"bradley": [
		{"line": "Sore tomorrow means it worked.", "beat": "workout"},
		{"line": "Now that's a trainer. Didn't even ask questions.", "beat": "workout"},
		{"line": "Counts as chest day.", "beat": "workout"},
		{"line": "Somebody's spotting me. That's teamwork, bro.", "beat": "workout"},
	],
}

var _shame_elapsed := 0.0
var _shame_count := 0
var _zap_cool := 0.0
var _zap_last_line := ""
var _zap_last_beat := ""


## Picks `bro`'s zap line: never the last line, and never the last beat while another beat is left
## (Bradley's pool is one beat, so only the line rule applies to him). "" for a bro with no pool.
static func pick_zap(bro: String, last_line: String, last_beat: String, rng: RandomNumberGenerator) -> Dictionary:
	var pool: Array = ZAP_LINES.get(bro, [])
	var fresh := pool.filter(func(r): return r["line"] != last_line and r["beat"] != last_beat)
	if fresh.is_empty():
		fresh = pool.filter(func(r): return r["line"] != last_line)
	if fresh.is_empty():
		return {}
	return fresh[rng.randi_range(0, fresh.size() - 1)]


## Advances the zap cooldown; returns the leader's line when he is within range and it is ready,
## else "". `dist_tiles` < 0 means no leader.
func tick_zap(delta: float, bro: String, dist_tiles: float, rng: RandomNumberGenerator) -> String:
	_zap_cool = maxf(_zap_cool - delta, 0.0)
	if _zap_cool > 0.0 or dist_tiles < 0.0 or dist_tiles > ZAP_RANGE_TILES:
		return ""
	var row := pick_zap(bro, _zap_last_line, _zap_last_beat, rng)
	if row.is_empty():
		return ""
	_zap_last_line = String(row["line"])
	_zap_last_beat = String(row["beat"])
	_zap_cool = ZAP_COOLDOWN_S
	return _zap_last_line


## The poem as it is shown: its three lines in one box.
static func haiku_text() -> String:
	return "\n".join(HAIKU)


## The CRT's nth inspection, 0-based: the examine line first, then the read-outs in order, wrapping.
static func crt_text(inspection: int) -> String:
	if inspection <= 0:
		return String(EXAMINE[CRT_MIRROR])
	return String(CRT_READOUTS[(inspection - 1) % CRT_READOUTS.size()])


static func shame_line(index: int) -> String:
	return String(SHAME_LINES[index % SHAME_LINES.size()])


## The joystick-with-lips shows itself only while a bro is Embarrassed (FieldStatus gate).
static func available(state, id: String) -> bool:
	if id == GRAFFITI_JOYSTICK:
		return FieldStatus.has(state, FieldStatus.EMBARRASSED)
	return true


## Lines for one interaction. `visit` is how many times this prop was used before (0 = first).
## Each entry is {"who", "line"}. A prop whose gate is closed says nothing.
static func lines_for(state, id: String, visit: int) -> Array:
	if not available(state, id):
		return []
	match id:
		DDR_TOILET:
			if visit <= 0:
				return [{"who": NO_SPEAKER, "line": EXAMINE[id]}]
			return DDR_USE.duplicate()
		CRT_MIRROR:
			return [{"who": NO_SPEAKER, "line": crt_text(visit)}]
		SOCK_CHUTE:
			return [{"who": NO_SPEAKER, "line": EXAMINE[id] if visit <= 0 else SOCK_USE}]
		GRAFFITI_HAIKU:
			return [{"who": NO_SPEAKER, "line": haiku_text()}, {"who": NO_SPEAKER, "line": HAIKU_READOUT}]
		_:
			if EXAMINE.has(id):
				return [{"who": NO_SPEAKER, "line": EXAMINE[id]}]
	return []


## Advances the overstay timer; returns the announcer's line each time 30 seconds pass, else "".
func tick_shame(delta: float) -> String:
	_shame_elapsed += delta
	if _shame_elapsed < SHAME_INTERVAL_S:
		return ""
	_shame_elapsed -= SHAME_INTERVAL_S
	var line := shame_line(_shame_count)
	_shame_count += 1
	return line
