class_name SoundRegistry
extends RefCounted
## Sound ids for the Audio service (Eurobound-pqe9). It makes up no ids: it reads the ones the game
## data already names and matches them to the files under res://assets/audio.
##
## The rule: an id is an audio file's name without its extension ("qr_code_scan_beep" is
## qr_code_scan_beep.ogg, in any folder under audio_root).
##
## Ids are collected from every JSON file under data_root:
## - a value under one of ID_KEYS ("audio_cue": "qr_code_scan_beep"), as a string, a list of
##   strings or a dictionary of strings;
## - any string that ends in an audio extension ("ddr_up_arrow_press.wav");
## - a row with a "file" (or "audio_file") key also gives that file its "volume" and "loop", and
##   its "description", when that is one id-shaped word, becomes a second id for the same file
##   ({"file": "vip_bathroom_nft_discovery.ogg", "description": "triumphant_nft_discovery_chime"}).
## Text with spaces is prose and is skipped. An id the data names with no file on disk is
## "declared": has_id() is true, path_for() is "".

const ID_KEYS := ["audio_cue", "success_audio_cue", "sound", "audio_clip", "audio_clips",
		"triggers_audio", "sound_trigger", "sync_with_audio", "audio"]
const FILE_KEYS := ["file", "audio_file"]
const EXTENSIONS := ["ogg", "wav", "mp3"]

var data_root := "res://assets/data/"
var audio_root := "res://assets/audio/"

var _built := false
var _files: Dictionary = {}     # id -> res:// path of a file on disk
var _declared: Dictionary = {}  # id -> true, every id the data or the disk names
var _alias: Dictionary = {}     # id -> the id (file name) it stands for
var _rows: Dictionary = {}      # file id -> {"volume": float, "loop": bool}
var _id_shape := RegEx.create_from_string("^[A-Za-z0-9_]+$")


## Reads the data and the audio folder again. Lookups call it on first use.
func build() -> void:
	_built = true
	_files = {}
	_declared = {}
	_alias = {}
	_rows = {}
	_scan_audio(audio_root)
	for id: String in _files:
		_declared[id] = true
	for path: String in _json_files(data_root):
		var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(path))
		if parsed != null:
			_walk(parsed, false)


## True when the data or the audio folder names `id`, whether or not a file exists for it.
func has_id(id: String) -> bool:
	_ensure()
	return _declared.has(id)


## The res:// path of the file for `id`, or "" when there is none.
func path_for(id: String) -> String:
	_ensure()
	return String(_files.get(_file_id(id), ""))


## {"path", "volume", "loop"} for `id`. Volume is 1.0 and loop false unless the data says otherwise.
func entry(id: String) -> Dictionary:
	_ensure()
	var row: Dictionary = _rows.get(_file_id(id), {})
	return {
		"path": path_for(id),
		"volume": float(row.get("volume", 1.0)),
		"loop": bool(row.get("loop", false)),
	}


## Every known id, sorted.
func declared_ids() -> Array:
	_ensure()
	var ids := _declared.keys()
	ids.sort()
	return ids


## The declared ids that have no file yet, sorted.
func missing_ids() -> Array:
	return declared_ids().filter(func(id: String) -> bool: return path_for(id).is_empty())


func _ensure() -> void:
	if not _built:
		build()


func _file_id(id: String) -> String:
	if _files.has(id) or not _alias.has(id):
		return id
	return String(_alias[id])


func _is_id(text: String) -> bool:
	return _id_shape.search(text) != null


func _is_audio_file(text: String) -> bool:
	return EXTENSIONS.has(text.get_extension().to_lower()) and _is_id(text.get_file().get_basename())


func _declare(text: String) -> void:
	if _is_audio_file(text):
		_declared[text.get_file().get_basename()] = true
	elif _is_id(text):
		_declared[text] = true


## `under_id_key`: the node sits under one of ID_KEYS, so its plain strings are ids.
func _walk(node: Variant, under_id_key: bool) -> void:
	if node is String:
		if under_id_key or _is_audio_file(node):
			_declare(node)
	elif node is Array:
		for item in node:
			_walk(item, under_id_key)
	elif node is Dictionary:
		_read_file_row(node)
		for key in node:
			_walk(node[key], under_id_key or ID_KEYS.has(String(key)))


func _read_file_row(row: Dictionary) -> void:
	for key: String in FILE_KEYS:
		var file: Variant = row.get(key)
		if not (file is String) or not _is_audio_file(file):
			continue
		var id := String(file).get_file().get_basename()
		_declared[id] = true
		var known: Dictionary = _rows.get(id, {})
		if (row.get("volume") is float or row.get("volume") is int) and not known.has("volume"):
			known["volume"] = clampf(float(row["volume"]), 0.0, 1.0)
		if row.get("loop") is bool and not known.has("loop"):
			known["loop"] = row["loop"]
		_rows[id] = known
		var other: Variant = row.get("description")
		if other is String and _is_id(other) and other != id and not _alias.has(other):
			_alias[other] = id
			_declared[other] = true


func _scan_audio(dir_path: String) -> void:
	var dir := DirAccess.open(dir_path)
	if dir == null:
		return
	for sub in dir.get_directories():
		_scan_audio(dir_path.path_join(sub))
	for file in dir.get_files():
		# An exported game lists "name.ogg.import" in place of "name.ogg".
		var name := file.trim_suffix(".import")
		if not EXTENSIONS.has(name.get_extension().to_lower()):
			continue
		var id := name.get_basename()
		var path := dir_path.path_join(name)
		if _files.has(id) and _files[id] != path:
			push_warning("SoundRegistry: two audio files share the id '%s': %s and %s (the first is used)" % [id, _files[id], path])
			continue
		_files[id] = path


func _json_files(dir_path: String) -> Array:
	var out := []
	var dir := DirAccess.open(dir_path)
	if dir == null:
		return out
	for file in dir.get_files():
		if file.get_extension().to_lower() == "json":
			out.append(dir_path.path_join(file))
	for sub in dir.get_directories():
		out.append_array(_json_files(dir_path.path_join(sub)))
	return out
