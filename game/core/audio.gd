extends Node
## Audio (Eurobound-pqe9): the one place the game plays sound. Autoload "Audio".
##
##   Audio.play_sfx("qr_code_scan_beep")      a sound by id, on the SFX bus
##   Audio.play_music("some_track_id")        one looping track on the Music bus, crossfaded in
##   Audio.stop_music()                       fades the track out
##   Audio.set_volume("Music", 0.5)           0.0 to 1.0 per bus; get_volume("Music") reads it
##
## Ids come from SoundRegistry: an id is an audio file's name without its extension, and the ids
## are the ones the game data already names. This node picks no sound and no track. Which sound
## exists and what plays where is the author's call.
##
## An id with no file warns once and returns false. Nothing here crashes on a missing file.
##
## Volumes are kept in GameState.flags under "settings.volume.<bus>", beside
## "settings.reduced_motion", so they save and load with the game. The Settings screen that would
## change them is Eurobound-j0zo.

const BUS_MASTER := "Master"
const BUS_MUSIC := "Music"
const BUS_SFX := "SFX"
const BUSES := [BUS_MASTER, BUS_MUSIC, BUS_SFX]
const VOLUME_KEY_PREFIX := "settings.volume."

## A technical default, not a ruled number: callers pass their own fade length when they have one.
const DEFAULT_FADE_S := 1.0
## How many sounds can overlap. The oldest is cut when all are busy.
const SFX_VOICES := 8

## The game state the volumes are kept in. Null means the GameState autoload.
var state = null
var registry := SoundRegistry.new()

## The player the last play_sfx() used, null before the first.
var last_sfx_player: AudioStreamPlayer = null
## How many missing-sound warnings have been sent (one per id).
var warnings_sent := 0

var _sfx: Array[AudioStreamPlayer] = []
var _next_sfx := 0
var _music: Array[AudioStreamPlayer] = []
var _active := 0
var _track := ""
var _music_pitch := 1.0
## One row per music player: {"from", "to", "t", "len", "stop"}; volumes are linear.
var _fades: Array = [{}, {}]
var _warned: Dictionary = {}
var _volumes: Dictionary = {}
var _streams: Dictionary = {}


func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS
	_ensure_buses()
	for i in SFX_VOICES:
		_sfx.append(_new_player(BUS_SFX))
	for i in 2:
		var player := _new_player(BUS_MUSIC)
		player.finished.connect(_on_music_finished.bind(i))
		_music.append(player)
	sync_volumes()


func _process(delta: float) -> void:
	advance(delta)
	sync_volumes()


# ---------- sound effects ----------

## Plays the sound `sound_id` once. `volume` (0.0 to 1.0) overrides the volume the data gives the
## file; leave it out to use the data's, or full volume when the data gives none.
## Returns false, after one warning per id, when there is no file for the id.
func play_sfx(sound_id: String, volume: float = -1.0) -> bool:
	var stream := _stream(sound_id)
	if stream == null or _sfx.is_empty():
		return false
	var player := _free_sfx_player()
	player.stream = stream
	player.volume_linear = clampf(volume, 0.0, 1.0) if volume >= 0.0 else float(registry.entry(sound_id)["volume"])
	player.play()
	last_sfx_player = player
	return true


## True when a file exists for `sound_id`. Never warns.
func has_sound(sound_id: String) -> bool:
	var path := registry.path_for(sound_id)
	return not path.is_empty() and ResourceLoader.exists(path)


# ---------- music ----------

## Plays `track_id` on a loop, fading the current track out and this one in over `fade_s` seconds
## (0 switches at once). The track that is already playing is left alone. Returns false, after one
## warning per id, when there is no file for the id; the current music then keeps playing.
func play_music(track_id: String, fade_s: float = DEFAULT_FADE_S) -> bool:
	if not track_id.is_empty() and track_id == _track:
		return true
	var stream := _stream(track_id)
	if stream == null or _music.is_empty():
		return false
	var looped: AudioStream = stream.duplicate()
	if "loop" in looped:
		looped.loop = true
	var level := float(registry.entry(track_id)["volume"])
	_fade(_active, 0.0, fade_s, true)
	_active = 1 - _active
	var player := _music[_active]
	player.stream = looped
	player.pitch_scale = _music_pitch
	player.volume_linear = 0.0 if fade_s > 0.0 else level
	player.play()
	_fades[_active] = {}
	if fade_s > 0.0:
		_fade(_active, level, fade_s, false)
	_track = track_id
	return true


## Fades the music out over `fade_s` seconds (0 stops at once).
func stop_music(fade_s: float = DEFAULT_FADE_S) -> void:
	_track = ""
	if not _music.is_empty():
		_fade(_active, 0.0, fade_s, true)


## The id of the track that is playing, "" when none is.
func current_music() -> String:
	return _track


## The player the current track is on (the other one holds a track that is fading out).
func music_player() -> AudioStreamPlayer:
	return _music[_active] if not _music.is_empty() else null


## Speed and pitch of the music, 1.0 is normal. Holds for the playing track and the ones after it.
func set_music_pitch(scale: float) -> void:
	_music_pitch = maxf(0.01, scale)
	for player in _music:
		player.pitch_scale = _music_pitch


## Moves the music fades on by `delta` seconds. _process() calls it; tests call it directly.
func advance(delta: float) -> void:
	for i in _music.size():
		var fade: Dictionary = _fades[i]
		if fade.is_empty():
			continue
		fade["t"] = float(fade["t"]) + delta
		var k := clampf(float(fade["t"]) / float(fade["len"]), 0.0, 1.0)
		_music[i].volume_linear = lerpf(float(fade["from"]), float(fade["to"]), k)
		if k >= 1.0:
			if bool(fade["stop"]):
				_music[i].stop()
			_fades[i] = {}


# ---------- volume ----------

## Sets a bus's volume, 0.0 (muted) to 1.0 (full), and keeps it in the game state so it is saved.
## Returns false for a bus that is not in BUSES.
func set_volume(bus: String, linear: float) -> bool:
	if not BUSES.has(bus):
		push_warning("Audio: no bus named '%s'" % bus)
		return false
	var value := clampf(linear, 0.0, 1.0)
	var st = _state()
	if st != null and "flags" in st:
		st.flags[volume_key(bus)] = value
	_apply_volume(bus, value)
	return true


## A bus's volume, 0.0 to 1.0. 1.0 for a bus that is not in BUSES.
func get_volume(bus: String) -> float:
	return float(_volumes.get(bus, 1.0))


## Reads the volumes from the game state and applies any that changed (after a load, say).
## _process() calls it every frame.
func sync_volumes() -> void:
	var st = _state()
	for bus: String in BUSES:
		var raw: Variant = st.flags.get(volume_key(bus)) if st != null and "flags" in st else null
		var value := clampf(float(raw), 0.0, 1.0) if (raw is float or raw is int) else 1.0
		if not _volumes.has(bus) or not is_equal_approx(float(_volumes[bus]), value):
			_apply_volume(bus, value)


static func volume_key(bus: String) -> String:
	return VOLUME_KEY_PREFIX + bus.to_lower()


## The ids already warned about, sorted.
func warned_ids() -> Array:
	var ids := _warned.keys()
	ids.sort()
	return ids


# ---------- internals ----------

func _state():
	if state != null:
		return state
	return get_node_or_null("/root/GameState") if is_inside_tree() else null


func _apply_volume(bus: String, value: float) -> void:
	_volumes[bus] = value
	var i := AudioServer.get_bus_index(bus)
	if i < 0:
		return
	AudioServer.set_bus_mute(i, value <= 0.0)
	if value > 0.0:
		AudioServer.set_bus_volume_db(i, linear_to_db(value))


## default_bus_layout.tres already has these; this covers a layout that failed to load.
func _ensure_buses() -> void:
	for bus: String in [BUS_MUSIC, BUS_SFX]:
		if AudioServer.get_bus_index(bus) >= 0:
			continue
		AudioServer.add_bus()
		var i := AudioServer.bus_count - 1
		AudioServer.set_bus_name(i, bus)
		AudioServer.set_bus_send(i, BUS_MASTER)


func _new_player(bus: String) -> AudioStreamPlayer:
	var player := AudioStreamPlayer.new()
	player.bus = bus
	add_child(player)
	return player


func _free_sfx_player() -> AudioStreamPlayer:
	for n in _sfx.size():
		var i := (_next_sfx + n) % _sfx.size()
		if not _sfx[i].playing:
			_next_sfx = (i + 1) % _sfx.size()
			return _sfx[i]
	var oldest := _sfx[_next_sfx]
	_next_sfx = (_next_sfx + 1) % _sfx.size()
	return oldest


## The stream for an id, or null after one warning per id.
func _stream(id: String) -> AudioStream:
	if id.is_empty():
		return null
	if _streams.has(id):
		return _streams[id]
	var path := registry.path_for(id)
	var stream: AudioStream = null
	if not path.is_empty() and ResourceLoader.exists(path):
		stream = load(path) as AudioStream
	if stream == null:
		_warn_once(id, path)
		return null
	_streams[id] = stream
	return stream


func _warn_once(id: String, path: String) -> void:
	if _warned.has(id):
		return
	_warned[id] = true
	warnings_sent += 1
	if not path.is_empty():
		push_warning("Audio: '%s' could not be loaded from %s" % [id, path])
	elif registry.has_id(id):
		push_warning("Audio: '%s' is named in the game data but has no file under %s yet" % [id, registry.audio_root])
	else:
		push_warning("Audio: no sound with the id '%s' (no data names it, no file under %s)" % [id, registry.audio_root])


func _fade(i: int, to: float, seconds: float, stop_after: bool) -> void:
	var player := _music[i]
	if not player.playing:
		_fades[i] = {}
		return
	if seconds <= 0.0:
		player.volume_linear = to
		if stop_after:
			player.stop()
		_fades[i] = {}
		return
	_fades[i] = {"from": player.volume_linear, "to": to, "t": 0.0, "len": seconds, "stop": stop_after}


## A stream that cannot loop by itself (no "loop" property) is started again when it ends.
func _on_music_finished(i: int) -> void:
	if i == _active and not _track.is_empty() and _music[i].stream != null:
		_music[i].play()
