class_name KavarnaChair
extends RefCounted
## Tony420's rented terminal at the Cyberspace Kavarna (cyberspacekavarna.md "The Hourly Chair";
## Kavarna option C, author 2026-11-11; NEXT_WORK.md "Tony420 / FREE Wi-Fi hijack"). Before the
## Shamsterdam Döner Debate a different silent hourly patron sits there every night; after it, the
## goon holding the tablet takes the seat. The goon is never shown before the Debate.

## Set by the Döner Debate's Shamsterdam confrontation (the goon-and-tablet reveal) when it's built.
const DONER_DEBATE_DONE := "great_doner_debate.shamsterdam.complete"


## "hourly_patron" before the Döner Debate, "goon_tablet" after.
static func occupant(state) -> String:
	return "goon_tablet" if bool(state.flags.get(DONER_DEBATE_DONE, false)) else "hourly_patron"


## Tonight's patron from a roster: a different one each night (the roster is the scene's art).
static func patron_for_night(state, roster: Array) -> String:
	if roster.is_empty():
		return ""
	return String(roster[GameClock.day(state) % roster.size()])
