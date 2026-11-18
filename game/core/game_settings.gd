class_name GameSettings
extends RefCounted
## The Settings screen's rows (Eurobound-c1gt, approved list in
## docs/superpowers/specs/2026-11-16-Eurobound-j0zo-proposal.md). Values live in GameState.flags
## under "settings.<name>", beside "settings.reduced_motion" and "settings.volume.<bus>", so they
## save and load with the game and the save format does not change.
##
## Built: reduced motion, prompt style. Not built, waiting on author numbers: volume sliders
## (step size, Ambience channel), chat speed and fast-scroll (no steps), text size, high contrast.

const KEY_REDUCED_MOTION := "settings.reduced_motion"
const KEY_PROMPT_STYLE := "settings.prompt_style"

const PROMPT_KEYBOARD := "keyboard"
const PROMPT_CONTROLLER := "controller"
const PROMPT_STYLES := [PROMPT_KEYBOARD, PROMPT_CONTROLLER]

## The rows, in screen order. Each is {"id", "label"}.
const ROWS := [
	{"id": "reduced_motion", "label": "Reduced motion"},
	{"id": "prompt_style", "label": "Button prompts"},
]

## Control labels per prompt style: the keys and buttons player_controller.gd and FieldMenu already take.
const CONTROLS := {
	PROMPT_KEYBOARD: ["Move  WASD / arrows", "Confirm  E / Space / Enter", "Back  Esc / Backspace / Q", "Menu  Esc"],
	PROMPT_CONTROLLER: ["Move  left stick", "Confirm  A", "Back  B", "Menu  Start"],
}


## Keyboard until the player picks controller: the game ships for desktop.
static func prompt_style(state) -> String:
	var raw = state.flags.get(KEY_PROMPT_STYLE, PROMPT_KEYBOARD) if state != null else PROMPT_KEYBOARD
	return String(raw) if PROMPT_STYLES.has(raw) else PROMPT_KEYBOARD


static func set_prompt_style(state, style: String) -> bool:
	if state == null or not PROMPT_STYLES.has(style):
		return false
	state.flags[KEY_PROMPT_STYLE] = style
	return true


static func toggle_prompt_style(state) -> void:
	set_prompt_style(state, PROMPT_CONTROLLER if prompt_style(state) == PROMPT_KEYBOARD else PROMPT_KEYBOARD)


static func reduced_motion(state) -> bool:
	return state != null and bool(state.flags.get(KEY_REDUCED_MOTION, false))


static func set_reduced_motion(state, on: bool) -> void:
	if state != null:
		state.flags[KEY_REDUCED_MOTION] = on


## Flips row `index` of ROWS.
static func toggle_row(state, index: int) -> void:
	match String(ROWS[clampi(index, 0, ROWS.size() - 1)]["id"]):
		"reduced_motion":
			set_reduced_motion(state, not reduced_motion(state))
		"prompt_style":
			toggle_prompt_style(state)


## The value shown beside row `index`.
static func row_value(state, index: int) -> String:
	match String(ROWS[clampi(index, 0, ROWS.size() - 1)]["id"]):
		"reduced_motion":
			return "On" if reduced_motion(state) else "Off"
		_:
			return "Controller" if prompt_style(state) == PROMPT_CONTROLLER else "Keyboard"
