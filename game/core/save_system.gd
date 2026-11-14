extends Node
## Persists GameState to disk as JSON. Corrupt saves AND saves from an incompatible
## schema version are treated as absent — the player sees a disabled Continue button,
## never a crash. Author ruling, 2026-08-06: an incompatible save is rejected
## cleanly, never migrated. See GameState.SAVE_VERSION.

var save_path := "user://saves/slot1.json"

## Emitted after save_now() has written the file. `reason` is the trigger's own word for itself.
signal saved(reason: String)

## THE entry point for anything that saves the game (a FREE Wi-Fi hotspot, a bed, autosave):
## notes where the bros are standing, then writes the save. `reason` names the trigger
## ("hotspot", ...). `state` defaults to the GameState autoload; tests pass their own.
## WHEN the game saves is the author's call (NEXT_WORK.md:700); this only does the saving.
func save_now(reason: String = "", state = null) -> bool:
	var tree := get_tree() if is_inside_tree() else null
	if state == null and tree != null:
		state = tree.root.get_node_or_null("GameState")
	if state == null:
		push_error("SaveSystem: save_now('%s') has no game state to save" % reason)
		return false
	if tree != null and tree.current_scene != null:
		capture_location(state, tree.current_scene, tree.current_scene.scene_file_path)
	if not save_game(state):
		return false
	saved.emit(reason)
	return true

## Records the screen and the leader's spot on `state`. `world` is the screen's root (the node
## SceneRouter.spawn_player put the player under). With no world, no scene file or no player,
## what the state already holds is kept.
func capture_location(state, world: Node, scene_path: String) -> void:
	if world == null or not world.is_inside_tree():
		return
	if not scene_path.is_empty():
		state.current_scene_path = scene_path
	for n in world.get_tree().get_nodes_in_group("player"):
		if n is PlayerController and world.is_ancestor_of(n):
			var player := n as PlayerController
			state.player_spot = {
				"x": float(player.position.x),
				"y": float(player.position.y),
				"z": float(player.position.z),
				"facing": String(player.sprite.facing),
			}
			return

## Call after load_game() and before changing to state.current_scene_path: the screen then
## spawns the leader where the save was made.
func prepare_resume(state) -> void:
	var spot: Variant = state.get("player_spot")
	SceneRouter.pending_spot = spot.duplicate(true) if spot is Dictionary else {}
	SceneRouter.pending_spawn = ""

## Writes to a temp file first and swaps it in, so a crash mid-write never leaves a half-written
## save where the last good one was.
func save_game(state) -> bool:
	DirAccess.make_dir_recursive_absolute("user://saves")
	var tmp_path := save_path + ".tmp"
	var f := FileAccess.open(tmp_path, FileAccess.WRITE)
	if f == null:
		push_error("SaveSystem: cannot open %s for writing (%s)" % [tmp_path, FileAccess.get_open_error()])
		return false
	f.store_string(JSON.stringify(state.to_dict(), "  "))
	var write_error := f.get_error()
	f.close()
	if write_error != OK:
		push_error("SaveSystem: writing %s failed (%s)" % [tmp_path, write_error])
		DirAccess.remove_absolute(tmp_path)
		return false
	var err := DirAccess.rename_absolute(tmp_path, save_path)
	if err != OK:
		push_error("SaveSystem: cannot move %s to %s (%s)" % [tmp_path, save_path, err])
		DirAccess.remove_absolute(tmp_path)
		return false
	return true

func load_game(state) -> bool:
	var data := _read_save()
	if data.is_empty():
		return false
	state.from_dict(data)
	return true

func has_save() -> bool:
	return not _read_save().is_empty()

func _read_save() -> Dictionary:
	if not FileAccess.file_exists(save_path):
		return {}
	var text := FileAccess.get_file_as_string(save_path)
	var parsed: Variant = JSON.parse_string(text)
	if parsed == null or not (parsed is Dictionary):
		push_error("SaveSystem: save file is corrupt: " + save_path)
		return {}
	var found_version := int(parsed.get("save_version", 0))
	if found_version != GameState.SAVE_VERSION:
		push_error("SaveSystem: save file '%s' is version %d, expected %d — incompatible save rejected (no migration, per author ruling)" % [save_path, found_version, GameState.SAVE_VERSION])
		return {}
	return parsed
