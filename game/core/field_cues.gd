extends Node
## FieldCues (Eurobound-k3qa): the one place the screen layer hears about the Space Cake cues the
## engine already produces (Eurobound-2xah). Autoload "FieldCues". Approved spec:
## docs/superpowers/specs/2026-11-13-contact-high-space-cake-proposal.md (SC4, SC5c, SC7, T6).
##
## This node only hands facts over. It draws nothing, plays nothing and holds no text: what each
## cue looks, reads and sounds like waits on the author (Eurobound Desk Eurobound-k3qa-q1). A HUD or
## scene connects to the signals below and builds the visible part behind them.

## SC5c: a Space Cake Timer landed on `target` (a party member id) with `cakes` cakes in it. One
## emission per landing, oldest first. Landings stay queued in the saved state until something is
## connected here, so a cue is never dropped because no screen was listening.
signal space_cake_landed(target: String, cakes: int)

## T6: a Navigation roll was replaced by a teleport. `exit_id` and `label` are the exit the bros
## come up at; `lost_minutes` is already on the game clock (T5). Sent by report_roll().
signal tunnel_teleported(exit_id: String, label: String, lost_minutes: int)

## SC4: the Space Cake Timer readout changed. `readout` is timer_readout(): one entry per bro with a
## live timer, [] when none is running.
signal space_cake_timer_changed(readout: Array)

## SC7: Space Cake Gamble started or stopped being live on any bro (the music bed's cue).
signal space_cake_gamble_changed(live: bool)

## The game state to read. Null means the GameState autoload.
var state = null

var _last_readout: Array = []
var _last_gamble := false


func _process(_delta: float) -> void:
	pump()


func _state():
	if state != null:
		return state
	return get_node_or_null("/root/GameState") if is_inside_tree() else null


## One pass: hands over queued landings (only while something listens), then reports the timer
## readout and the Gamble when either changed since the last pass.
func pump() -> void:
	var st = _state()
	if st == null or not ("flags" in st):
		return
	if not space_cake_landed.get_connections().is_empty() and st.flags.has(FieldStatus.LANDINGS_KEY):
		for landing: Dictionary in FieldStatus.take_landings(st):
			space_cake_landed.emit(String(landing.get("target", "")), int(landing.get("count", 1)))
	var readout := timer_readout(st)
	if readout != _last_readout:
		_last_readout = readout
		space_cake_timer_changed.emit(readout)
	var live := gamble_live(st)
	if live != _last_gamble:
		_last_gamble = live
		space_cake_gamble_changed.emit(live)


## The tunnel scene passes every NavigationRoll.roll() result here. Emits tunnel_teleported and
## returns true when the roll teleported; otherwise does nothing.
func report_roll(result: Dictionary) -> bool:
	if not bool(result.get("teleported", false)):
		return false
	tunnel_teleported.emit(String(result.get("exit", "")), String(result.get("label", "")),
			int(result.get("lost_minutes", 0)))
	return true


## SC4: [{"target", "minutes_left", "cakes"}] for each bro with a live Space Cake Timer, in party
## order. Reads only; never changes the state.
static func timer_readout(st) -> Array:
	var out := []
	if st == null or not ("flags" in st) or not st.flags.has(FieldStatus.KEY):
		return out
	var all: Dictionary = st.flags[FieldStatus.KEY]
	var now := GameClock.minutes(st)
	var targets := []
	if "party" in st:
		for member in st.party:
			if member is Dictionary and all.has(String(member.get("id", ""))):
				targets.append(String(member["id"]))
	for t in all.keys():
		if not targets.has(t):
			targets.append(t)
	for t: String in targets:
		var row: Dictionary = Dictionary(all[t]).get(FieldStatus.SPACE_CAKE_TIMER, {})
		var left := int(row.get("until", 0)) - now
		if row.is_empty() or left <= 0:
			continue
		out.append({"target": t, "minutes_left": left, "cakes": maxi(1, int(row.get("stacks", 1)))})
	return out


## SC7: true while any bro has Space Cake Gamble. Reads only.
static func gamble_live(st) -> bool:
	if st == null or not ("flags" in st) or not st.flags.has(FieldStatus.KEY):
		return false
	return FieldStatus.has(st, FieldStatus.SPACE_CAKE_GAMBLE)
