class_name DdrDifficulty
extends RefCounted
## The difficulty select: it lists every level and is permanently stuck on EXPERT, to the bros'
## frustration (author ruling ef_ddr_build, 2026-11-10). Every try to move it is counted so the
## screen can let the bros complain (their lines are the author's to write).

const LEVELS := ["BEGINNER", "BASIC", "DIFFICULT", "EXPERT"]
const STUCK_ON := "EXPERT"

var refusals := 0


func selected() -> String:
	return STUCK_ON


## Tries to move the cursor. It never moves.
func move(_delta: int) -> bool:
	refusals += 1
	return false
