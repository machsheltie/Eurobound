class_name TaproomFights
extends RefCounted
## Where the two Taproom fights start (author, Eurobound Desk 2026-11-12):
##  - Mirror Chad: "In the maze, around section 3 or 4" -> section 3, first entry in a visit
##    (TaproomMaze.take_chad), until mirror_chad_defeated.
##  - Green Fairy Wisp: "When you first reach the bar after the maze" -> on arrival in the Taproom
##    from the maze exit, until she is defeated or survived.
## A loss follows the arcade loss rule (everyone at 1 HP, the bros stay where they were); a run
## leaves the flags unset. No dialogue beyond what TaproomBattle plays.


static func wisp_due(state) -> bool:
	return not bool(state.flags.get(TaproomBattle.FLAG_WISP_DEFEATED, false)) \
			and not bool(state.flags.get(TaproomBattle.FLAG_WISP_SURVIVED, false))


## Locks the player, runs the fight on `host`, then frees the player. Returns the outcome.
static func run(host: Node, player: Node, fight: String, state) -> String:
	if player != null:
		player.input_locked = true
	var outcome := ""
	if fight == TaproomBattle.MIRROR_CHAD:
		outcome = await TaproomBattle.start_mirror_chad(host, state)
	else:
		outcome = await TaproomBattle.start_wisp(host, state)
	if player != null and is_instance_valid(player):
		player.input_locked = false
	return outcome
