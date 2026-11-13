class_name VanekTaproom
extends RefCounted
## Dr. Miloš Vaněk's rules at The Cracked Bottle bar in The Absinthium Taproom.
## Spec: design/worlds/debaucheryville/the_absinthium_taproom.md (opener check :34-37, stamp
## conditions :207-211, stamp speech :213-214, Absinthe Lager :216-238) and
## design/items/brewery_tour/beer_absinthium_taproom_item.md.
## Order of play: keychain gate, then opener check, then the Lager sale (12 SOVS, keychain
## discount), then the stamp (all four conditions). State is GameState (flags + inventory).

const BREWERY_ID := "absinthium_taproom"
const LAGER_ID := "beer_absinthium_taproom"
const LAGER_PRICE := 12
const FLAG_LAGER_BOUGHT := "vanek_lager_bought"
const FLAG_SURVEY_CONSENTED := "vanek_survey_consented"
const FLAG_GREETED := "vanek_greeted"

const GATE_NO_KEYCHAIN := "no_keychain"
const GATE_NO_OPENER := "no_opener"
const GATE_OK := "ok"

const SALE_BOUGHT := "bought"
const SALE_CANNOT_AFFORD := "cannot_afford"
const SALE_REFUSED := "refused"  ## failed the gate

const SPEAKER := "Dr. Vaněk"

## Verbatim from the location doc (:36-37, :213-214, :235-238).
const LINE_NO_KEYCHAIN := "No Publandia key, no brewery tour access. The Continental Trail has protocols. Return when properly credentialed."
const LINE_BOTH_OPENERS := "The cracked glass. You've navigated the mirrors. Either way, you've committed. The Absinthe Lager awaits. Prepare for... introspection."
const LINES_SERVING := [
	"The Absinthe Lager. My signature creation. The green fairy is IN the beer. Metaphorically. And slightly literally.",
	"You may experience mild disorientation. This is intentional. If you DON'T feel disoriented, tell me immediately — I need to adjust the formula.",
	"30% confusion chance. 100% authenticity. Those are better odds than reality offers.",
]
const LINE_STAMP_SPEECH := "Congratulations. You've seen yourself. Not everyone does — some people navigate the mirrors without ever looking INTO them. You looked. The stamp is proof. The memory is punishment. Or reward. The distinction is philosophical."

## TODO (author / Writers' Room): gaps the docs do not fill. Empty = nothing is said, nothing invented.
## Keychain held, no Absinthium opener: the old line is struck (:35); the Writers' Room writes it (v44).
const TODO_LINE_KEYCHAIN_NO_OPENER := ""
## The player cannot pay for the Lager.
const TODO_LINE_CANNOT_AFFORD := ""
## "Vaněk's Survey" (:243, :298): questions and rewards are undefined; only consent is recorded.
const TODO_SURVEY_QUESTIONS: Array = []
const TODO_SURVEY_REWARDS: Array = []
## Callback lines once stamped / on return visits: not written.
const TODO_LINES_CALLBACK: Array = []
## Opener when the maze was finished before the tour started: not auto-granted (undecided).
const TODO_OPENER_BACKFILL_ENABLED := false
## His hours (20:00-04:00, :16) are not enforced yet.
const TODO_HOURS_ENFORCED := false


static func has_keychain(state) -> bool:
	return int(state.inventory.get(BreweryPassport.KEYCHAIN, 0)) > 0


## Keychain gate first, then the opener check.
static func gate(state) -> String:
	if not has_keychain(state):
		return GATE_NO_KEYCHAIN
	if not BreweryPassport.has_opener(state, BREWERY_ID):
		return GATE_NO_OPENER
	return GATE_OK


## 12 SOVS less the keychain discount.
static func lager_price(state) -> int:
	return BreweryPassport.discounted_bar_price(state, LAGER_PRICE)


static func buy_lager(state) -> String:
	if gate(state) != GATE_OK:
		return SALE_REFUSED
	if not state.spend_sovs(lager_price(state)):
		return SALE_CANNOT_AFFORD
	state.add_item(LAGER_ID, 1)
	state.flags[FLAG_LAGER_BOUGHT] = true
	return SALE_BOUGHT


## The four unlock conditions (:208-211), each true or false.
static func stamp_conditions(state) -> Dictionary:
	return {
		"maze": bool(state.flags.get(TaproomMaze.FLAG_COMPLETED, false)),
		"wisp": bool(state.flags.get(TaproomBattle.FLAG_WISP_DEFEATED, false)) \
				or bool(state.flags.get(TaproomBattle.FLAG_WISP_SURVIVED, false)),
		"lager": bool(state.flags.get(FLAG_LAGER_BOUGHT, false)),
		"keychain": has_keychain(state),
	}


static func stamp_ready(state) -> bool:
	return gate(state) == GATE_OK and not stamp_conditions(state).values().has(false)


## Awards the Absinthium Seal when every condition holds. False if unmet or already stamped.
static func try_stamp(state) -> bool:
	if not stamp_ready(state):
		return false
	return BreweryPassport.award_stamp(state, BREWERY_ID)
