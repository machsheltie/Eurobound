class_name StreetLoss
extends RefCounted
## Losing a street fight, Option A point 7 (author, Eurobound Desk Eurobound-skjd-q2, 2026-11-16:
## "lose = back to last save, lose some SOVS"; docs/superpowers/specs/2026-11-16-Eurobound-skjd-proposal.md
## section 3; design/mechanics/Battle/street_encounters.md). The bros go back to where the last save
## was made (a FREE Wi-Fi hotspot or the hostel bed, NEXT_WORK.md:892, :920) keeping XP and items:
## nothing is loaded over the state, only the location changes. Part of the SOVS on hand is lost
## (half, author-ruled, StreetEncounterRules.LOSS_SOVS_SHARE; the bros lose the floor of half).
## Who takes the SOVS and how the loss is shown on screen go to the Writers' Room (point 7).
##
## HP after the loss is whatever the fight settled to (ArcadeBattle.settle_party: LOSS_HP, as for
## every other loss in the game). That and a loss before any save exists are open author questions
## (Eurobound-iqgo); with no save the bros go back to the start of the screen they lost on.


## Applies the loss to `state` (party HP already settled) and prepares the next screen's spawn.
## `save_system` is the SaveSystem autoload (or a stand-in with last_save_location()).
## `fallback_scene` is used when there is no save. Returns {"scene", "spot", "sovs_lost"}.
static func apply(state, save_system, share: Variant, fallback_scene: String) -> Dictionary:
	var lost := StreetEncounterRules.sovs_lost(int(state.sovs), share)
	state.sovs = int(state.sovs) - lost
	var where: Dictionary = save_system.last_save_location() if save_system != null else {}
	var scene := String(where.get("scene", ""))
	var spot: Dictionary = {}
	if scene.is_empty():
		scene = fallback_scene
	else:
		var saved_spot: Variant = where.get("spot", {})
		spot = saved_spot.duplicate(true) if saved_spot is Dictionary else {}
	state.current_scene_path = scene
	SceneRouter.pending_spot = spot.duplicate(true)
	SceneRouter.pending_spawn = ""
	return {"scene": scene, "spot": spot, "sovs_lost": lost}


## Changes to the plan's screen. Does nothing for a plan with no screen.
static func travel(tree: SceneTree, plan: Dictionary) -> void:
	var scene := String(plan.get("scene", ""))
	if scene.is_empty() or tree == null:
		return
	tree.change_scene_to_file.call_deferred(scene)
