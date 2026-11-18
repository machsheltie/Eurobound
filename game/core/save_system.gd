extends Node
## Persists GameState to disk as JSON. Corrupt saves AND saves from an incompatible
## schema version are treated as absent — the player sees a disabled Continue button,
## never a crash. Author ruling, 2026-08-06: an incompatible save is rejected
## cleanly, never migrated. See GameState.SAVE_VERSION.

## Three save slots the player picks from (author, NEXT_WORK.md:892). Slot n is
## <save_dir>/slot<n>.json. Before slots the game's one save was user://saves/slot1.json, which is
## slot 1's file: an existing save simply is slot 1, nothing is moved or rewritten.
const SLOT_COUNT := 3

## Where the slot files live (tests point it elsewhere).
var save_dir := "user://saves"
## The file save_game()/load_game() use: the slot last saved to or loaded (slot 1 at start).
var save_path := "user://saves/slot1.json"
## The slot picker while one is up (save_with_picker), else null.
var picker: SaveSlotPicker

## Emitted after save_now() has written the file. `reason` is the trigger's own word for itself.
signal saved(reason: String)


func slot_path(slot: int) -> String:
	return "%s/slot%d.json" % [save_dir, slot]


static func valid_slot(slot: int) -> bool:
	return slot >= 1 and slot <= SLOT_COUNT


## True when the slot holds a save that loads (a corrupt or incompatible file counts as empty).
func has_slot(slot: int) -> bool:
	return valid_slot(slot) and not _read_file(slot_path(slot)).is_empty()


func has_any_save() -> bool:
	for slot in range(1, SLOT_COUNT + 1):
		if has_slot(slot):
			return true
	return false


## What the picker shows for a slot, read from the save itself: {} when the slot is empty, else
## {"slot", "scene" (the screen's file), "time" (Lord Pilsner's watch, "HH:MM"), "sovs"}.
## The save stores no play time.
func slot_info(slot: int) -> Dictionary:
	if not valid_slot(slot):
		return {}
	var data := _read_file(slot_path(slot))
	if data.is_empty():
		return {}
	var flags: Variant = data.get("flags", {})
	var holder := {"flags": flags if flags is Dictionary else {}}
	return {
		"slot": slot,
		"scene": String(data.get("current_scene_path", "")),
		"time": GameClock.watch_text(holder),
		"sovs": int(data.get("sovs", data.get("gold", 0))),
	}


## Saves to one slot through save_now(): the location is captured the same way.
func save_to_slot(state, slot: int, reason: String = "") -> bool:
	if not valid_slot(slot):
		return false
	save_path = slot_path(slot)
	return save_now(reason, state)


func load_slot(state, slot: int) -> bool:
	if not has_slot(slot):
		return false
	save_path = slot_path(slot)
	return load_game(state)


## THE call for a save point (a FREE Wi-Fi hotspot, a bed): shows the slot picker, then saves to
## the slot the player picks (author, Eurobound Desk Eurobound-x2ws-q3: "A slot picker every time
## you save (hotspot or bed) and in Load"). Await it. False when the player cancels or the write
## fails. `state` defaults to the GameState autoload.
func save_with_picker(reason: String, state = null) -> bool:
	if picker != null:
		return false
	picker = SaveSlotPicker.new()
	picker.setup(self, "save")
	add_child(picker)
	var slot: int = await picker.pick()
	picker = null
	if slot <= 0:
		return false
	return save_to_slot(state, slot, reason)

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
	DirAccess.make_dir_recursive_absolute(save_dir)
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
	state.from_dict(data, get_node_or_null("/root/DataRepo"))
	return true

func has_save() -> bool:
	return not _read_save().is_empty()

## Where the last save was made (the slot last saved to or loaded): {"scene", "spot"}, or {} when
## that slot holds no save that loads. Reads the location only; the state is not touched (a street
## loss goes back there keeping XP and items, StreetLoss).
func last_save_location() -> Dictionary:
	var data := _read_save()
	if data.is_empty():
		return {}
	var spot: Variant = data.get("player_spot", {})
	return {
		"scene": String(data.get("current_scene_path", "")),
		"spot": spot.duplicate(true) if spot is Dictionary else {},
	}

func _read_save() -> Dictionary:
	return _read_file(save_path)

func _read_file(path: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		return {}
	var text := FileAccess.get_file_as_string(path)
	var parsed: Variant = JSON.parse_string(text)
	if parsed == null or not (parsed is Dictionary):
		push_error("SaveSystem: save file is corrupt: " + path)
		return {}
	var found_version := int(parsed.get("save_version", 0))
	if found_version != GameState.SAVE_VERSION:
		push_error("SaveSystem: save file '%s' is version %d, expected %d — incompatible save rejected (no migration, per author ruling)" % [path, found_version, GameState.SAVE_VERSION])
		return {}
	return parsed
