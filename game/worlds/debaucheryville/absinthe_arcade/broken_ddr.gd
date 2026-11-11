class_name BrokenDdr
extends RefCounted
## The north wing's hacked DDR (design: broken_ddr_restroom_unlock; round v34 nw_broken_ddr =
## follow_design): tokens go in one at a time, and the third unlocks the MAINTENANCE door for good.

const TOKENS := 3
const FED_FLAG := "aa_broken_ddr_tokens_fed"
const UNLOCK_FLAG := "arcade_maintenance_restroom_unlocked"


static func fed(state) -> int:
	return int(state.flags.get(FED_FLAG, 0))


static func unlocked(state) -> bool:
	return bool(state.flags.get(UNLOCK_FLAG, false))


## Feeds one token. Returns "fed", "unlocked" (that was the third), "broke" (no token) or "done"
## (already unlocked; nothing taken).
static func feed(state) -> String:
	if unlocked(state):
		return "done"
	if ArcadeRules.tokens(state) < 1:
		return "broke"
	ArcadeRules._take(state, ArcadeRules.TOKEN_ID, 1)
	state.flags[FED_FLAG] = fed(state) + 1
	if fed(state) >= TOKENS:
		state.flags[UNLOCK_FLAG] = true
		return "unlocked"
	return "fed"
