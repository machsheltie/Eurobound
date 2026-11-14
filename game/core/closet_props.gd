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

var _shame_elapsed := 0.0
var _shame_count := 0


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
