class_name MirrorShadowPuzzle
extends RefCounted
## Logic of the mirror corridor's shadow puzzle (design: design/worlds/debaucheryville/
## interactions/absinthe_arcade_interactions.json, object "mirror_shadow_puzzle": "Activate three
## shadow switches in the order shown by delayed afterimages"; author round v42 arc_mirror_puzzle = yes).
## Presentation lives in absinthe_arcade_mirror_corridor_hd2d.gd; this class only counts presses.
## `state` is GameState (flags, inventory, add_item).

const SWITCH_COUNT := 3
## The order the afterimages visit the switches, as switch indices 0..2: switch 3, then 1, then 2
## (author ruling, round v43 mirror_order = "312", 2026-11-12). The hint and the logic follow it.
const SOLUTION: Array[int] = [2, 0, 1]
const ITEM_ID := "item_broken_symbol_game_boy"
const SOLVED_FLAG := "mirror_shadow_secret_solved"
const FOUND_FLAG := "broken_game_boy_found"

## How many switches of the solution are lit so far.
var progress := 0


static func solved(state) -> bool:
	return bool(state.flags.get(SOLVED_FLAG, false))


## A switch was pressed. Returns "ignored" (already solved), "step" (right so far), "reset" (wrong
## order, start over) or "solved" (the reward is given, once).
func press(state, index: int) -> String:
	if solved(state):
		return "ignored"
	if index != SOLUTION[progress]:
		progress = 0
		return "reset"
	progress += 1
	if progress < SOLUTION.size():
		return "step"
	progress = 0
	state.flags[SOLVED_FLAG] = true
	state.flags[FOUND_FLAG] = true
	state.add_item(ITEM_ID, 1)
	return "solved"
