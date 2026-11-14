extends GutTest
## Audio (Eurobound-pqe9): one service plays a sound by id and one music track at a time, on Music
## and SFX buses, with a volume per bus kept in GameState.flags. Plumbing only: no test names a
## track the author has not made, the three files already in res://assets/audio stand in.

const AUDIO := preload("res://core/audio.gd")
const BEEP := "qr_code_scan_beep"
const CHIME := "triumphant_nft_discovery_chime"
const UH_OH := "icq_uh_oh"
const NO_FILE_YET := "warped_8bit_arcade_ambience"
const BEEP_PATH := "res://assets/audio/velvet_curtain_club/qr_code_scan_beep.ogg"

var st
var audio
var _saved_db := {}


func before_each() -> void:
	st = load("res://core/game_state.gd").new()
	st.flags = {}
	audio = AUDIO.new()
	audio.state = st
	add_child_autofree(audio)
	_saved_db = {}
	for bus: String in AUDIO.BUSES:
		var i := AudioServer.get_bus_index(bus)
		_saved_db[bus] = [AudioServer.get_bus_volume_db(i), AudioServer.is_bus_mute(i)]


func after_each() -> void:
	for bus: String in _saved_db:
		var i := AudioServer.get_bus_index(bus)
		AudioServer.set_bus_volume_db(i, _saved_db[bus][0])
		AudioServer.set_bus_mute(i, _saved_db[bus][1])
	st.free()


# ---------- buses ----------

func test_audio_buses_master_music_and_sfx_exist() -> void:
	# Act / Assert
	for bus: String in ["Master", "Music", "SFX"]:
		assert_true(AudioServer.get_bus_index(bus) >= 0, bus)


func test_audio_project_ships_a_bus_layout_with_music_and_sfx() -> void:
	# Act
	var text := FileAccess.get_file_as_string("res://default_bus_layout.tres")
	# Assert
	assert_string_contains(text, "&\"Music\"")
	assert_string_contains(text, "&\"SFX\"")


func test_audio_is_an_autoload() -> void:
	# Act / Assert
	assert_eq(String(ProjectSettings.get_setting("autoload/Audio", "")), "*res://core/audio.gd")


# ---------- sound effects ----------

func test_audio_play_sfx_plays_the_file_for_the_id_on_the_sfx_bus() -> void:
	# Act
	var ok: bool = audio.play_sfx(BEEP)
	# Assert
	assert_true(ok)
	var player: AudioStreamPlayer = audio.last_sfx_player
	assert_eq(player.bus, &"SFX")
	assert_eq(player.stream.resource_path, BEEP_PATH)


func test_audio_play_sfx_uses_the_volume_the_data_gives_the_file() -> void:
	# Act: debaucheryville_environmental.json gives vip_bathroom_nft_discovery.ogg volume 0.8
	audio.play_sfx(CHIME)
	# Assert
	assert_almost_eq(audio.last_sfx_player.volume_linear, 0.8, 0.001)


func test_audio_play_sfx_volume_argument_wins_over_the_data() -> void:
	# Act
	audio.play_sfx(CHIME, 0.5)
	# Assert
	assert_almost_eq(audio.last_sfx_player.volume_linear, 0.5, 0.001)


func test_audio_two_sounds_in_a_row_use_two_players() -> void:
	# Act
	audio.play_sfx(BEEP)
	var first: AudioStreamPlayer = audio.last_sfx_player
	audio.play_sfx(CHIME)
	# Assert: the beep is not cut off by the chime
	assert_ne(audio.last_sfx_player, first)
	assert_eq(first.stream.resource_path, BEEP_PATH)


func test_audio_missing_sound_returns_false_and_warns_once() -> void:
	# Act
	var first: bool = audio.play_sfx("no_such_sound")
	var second: bool = audio.play_sfx("no_such_sound")
	# Assert
	assert_false(first)
	assert_false(second)
	assert_eq(audio.warned_ids(), ["no_such_sound"])
	assert_eq(audio.warnings_sent, 1)


func test_audio_id_with_no_file_yet_returns_false_and_warns_once() -> void:
	# Act: declared in debaucheryville_environmental.json, no file in res://assets/audio
	var ok: bool = audio.play_sfx(NO_FILE_YET)
	audio.play_music(NO_FILE_YET)
	# Assert
	assert_false(ok)
	assert_eq(audio.warnings_sent, 1)


func test_audio_empty_id_is_ignored_without_a_warning() -> void:
	# Act / Assert
	assert_false(audio.play_sfx(""))
	assert_eq(audio.warnings_sent, 0)


func test_audio_has_sound_is_true_only_when_a_file_can_play() -> void:
	# Act / Assert
	assert_true(audio.has_sound(BEEP))
	assert_false(audio.has_sound(NO_FILE_YET))
	assert_false(audio.has_sound("no_such_sound"))
	assert_eq(audio.warnings_sent, 0)


# ---------- music ----------

func test_audio_play_music_plays_the_track_on_the_music_bus() -> void:
	# Act
	var ok: bool = audio.play_music(UH_OH, 0.0)
	# Assert
	assert_true(ok)
	assert_eq(audio.current_music(), UH_OH)
	var player: AudioStreamPlayer = audio.music_player()
	assert_eq(player.bus, &"Music")
	assert_true(player.playing)
	assert_almost_eq(player.volume_linear, 1.0, 0.001)


func test_audio_music_loops() -> void:
	# Act
	audio.play_music(UH_OH, 0.0)
	# Assert
	assert_true(audio.music_player().stream.loop)


func test_audio_looping_music_does_not_make_the_same_file_loop_as_a_sound() -> void:
	# Act
	audio.play_music(UH_OH, 0.0)
	audio.play_sfx(UH_OH)
	# Assert
	assert_false(audio.last_sfx_player.stream.loop)


func test_audio_play_music_crossfades_from_the_old_track_to_the_new() -> void:
	# Arrange
	audio.play_music(UH_OH, 0.0)
	var old: AudioStreamPlayer = audio.music_player()
	# Act
	audio.play_music(BEEP, 2.0)
	var new: AudioStreamPlayer = audio.music_player()
	audio.advance(1.0)
	# Assert: halfway, both are sounding
	assert_ne(new, old)
	assert_eq(audio.current_music(), BEEP)
	assert_true(old.playing)
	assert_almost_eq(old.volume_linear, 0.5, 0.01)
	assert_almost_eq(new.volume_linear, 0.5, 0.01)
	# Act: the fade ends
	audio.advance(1.0)
	# Assert
	assert_false(old.playing)
	assert_almost_eq(new.volume_linear, 1.0, 0.01)
	assert_true(new.playing)


func test_audio_play_music_with_the_track_already_playing_does_not_restart_it() -> void:
	# Arrange
	audio.play_music(UH_OH, 0.0)
	var player: AudioStreamPlayer = audio.music_player()
	# Act
	var ok: bool = audio.play_music(UH_OH, 2.0)
	# Assert
	assert_true(ok)
	assert_eq(audio.music_player(), player)
	assert_almost_eq(player.volume_linear, 1.0, 0.001)


func test_audio_stop_music_fades_out_then_stops() -> void:
	# Arrange
	audio.play_music(UH_OH, 0.0)
	var player: AudioStreamPlayer = audio.music_player()
	# Act
	audio.stop_music(2.0)
	audio.advance(1.0)
	# Assert
	assert_eq(audio.current_music(), "")
	assert_true(player.playing)
	assert_almost_eq(player.volume_linear, 0.5, 0.01)
	# Act
	audio.advance(1.0)
	# Assert
	assert_false(player.playing)


func test_audio_stop_music_with_no_fade_stops_at_once() -> void:
	# Arrange
	audio.play_music(UH_OH, 0.0)
	var player: AudioStreamPlayer = audio.music_player()
	# Act
	audio.stop_music(0.0)
	# Assert
	assert_false(player.playing)
	assert_eq(audio.current_music(), "")


func test_audio_missing_track_keeps_the_current_music_and_warns_once() -> void:
	# Arrange
	audio.play_music(UH_OH, 0.0)
	# Act
	var first: bool = audio.play_music("no_such_track")
	var second: bool = audio.play_music("no_such_track")
	# Assert
	assert_false(first)
	assert_false(second)
	assert_eq(audio.current_music(), UH_OH)
	assert_true(audio.music_player().playing)
	assert_eq(audio.warnings_sent, 1)


func test_audio_music_pitch_applies_to_the_playing_track_and_the_next() -> void:
	# Arrange
	audio.play_music(UH_OH, 0.0)
	# Act
	audio.set_music_pitch(0.96)
	# Assert
	assert_almost_eq(audio.music_player().pitch_scale, 0.96, 0.001)
	# Act
	audio.play_music(BEEP, 0.0)
	# Assert
	assert_almost_eq(audio.music_player().pitch_scale, 0.96, 0.001)


# ---------- volume ----------

func test_audio_volume_defaults_to_full_on_every_bus() -> void:
	# Act / Assert
	for bus: String in AUDIO.BUSES:
		assert_almost_eq(audio.get_volume(bus), 1.0, 0.001, bus)


func test_audio_set_volume_changes_the_bus_and_is_kept_in_the_game_state() -> void:
	# Act
	audio.set_volume("Music", 0.5)
	# Assert
	assert_almost_eq(audio.get_volume("Music"), 0.5, 0.001)
	assert_almost_eq(float(st.flags["settings.volume.music"]), 0.5, 0.001)
	assert_almost_eq(AudioServer.get_bus_volume_db(AudioServer.get_bus_index("Music")), linear_to_db(0.5), 0.01)
	assert_almost_eq(audio.get_volume("SFX"), 1.0, 0.001)


func test_audio_set_volume_clamps_to_zero_and_one() -> void:
	# Act
	audio.set_volume("SFX", 4.0)
	audio.set_volume("Music", -1.0)
	# Assert
	assert_almost_eq(audio.get_volume("SFX"), 1.0, 0.001)
	assert_almost_eq(audio.get_volume("Music"), 0.0, 0.001)


func test_audio_volume_zero_mutes_the_bus_and_raising_it_unmutes() -> void:
	# Arrange
	var i := AudioServer.get_bus_index("Music")
	# Act
	audio.set_volume("Music", 0.0)
	# Assert
	assert_true(AudioServer.is_bus_mute(i))
	# Act
	audio.set_volume("Music", 0.3)
	# Assert
	assert_false(AudioServer.is_bus_mute(i))


func test_audio_unknown_bus_is_refused() -> void:
	# Act / Assert
	assert_false(audio.set_volume("Narrator", 0.5))
	assert_false(st.flags.has("settings.volume.narrator"))
	assert_almost_eq(audio.get_volume("Narrator"), 1.0, 0.001)


func test_audio_volume_survives_a_save_and_load() -> void:
	# Arrange
	audio.set_volume("SFX", 0.25)
	var saved: Dictionary = JSON.parse_string(JSON.stringify(st.to_dict()))
	audio.set_volume("SFX", 1.0)
	# Act: a load replaces the flags; the service picks the saved volume up on its next pass
	st.from_dict(saved)
	audio.sync_volumes()
	# Assert
	assert_almost_eq(audio.get_volume("SFX"), 0.25, 0.001)
	assert_almost_eq(AudioServer.get_bus_volume_db(AudioServer.get_bus_index("SFX")), linear_to_db(0.25), 0.01)


func test_audio_broken_saved_volume_falls_back_to_full() -> void:
	# Arrange
	st.flags["settings.volume.music"] = "loud"
	# Act
	audio.sync_volumes()
	# Assert
	assert_almost_eq(audio.get_volume("Music"), 1.0, 0.001)
