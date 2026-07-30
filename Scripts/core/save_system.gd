extends Node
## Persists GameState to disk as JSON. Corrupt saves are treated as absent —
## the player sees a disabled Continue button, never a crash.

var save_path := "user://saves/slot1.json"

func save_game(state) -> bool:
	DirAccess.make_dir_recursive_absolute("user://saves")
	var f := FileAccess.open(save_path, FileAccess.WRITE)
	if f == null:
		push_error("SaveSystem: cannot open %s for writing (%s)" % [save_path, FileAccess.get_open_error()])
		return false
	f.store_string(JSON.stringify(state.to_dict(), "  "))
	f.close()
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
	return parsed
