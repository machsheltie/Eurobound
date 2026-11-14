extends GutTest
## Eurobound-cwkh: the DDR screen and the north wing play sound through the Audio autoload and make no
## AudioStreamPlayer of their own. (The Wi-Fi hotspot's checks are in test_wifi_hotspot.gd.)

const DDR := "res://worlds/debaucheryville/absinthe_arcade/ddr/ddr_screen.gd"
const NORTH_WING := "res://worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.gd"


func after_each() -> void:
	Audio.stop_music(0.0)


func test_ddr_and_north_wing_scripts_make_no_audio_stream_player() -> void:
	for path: String in [DDR, NORTH_WING]:
		assert_false(FileAccess.get_file_as_string(path).contains("AudioStreamPlayer"), path)


func test_ddr_screen_with_no_song_file_keeps_the_timer_and_starts_no_music() -> void:
	# Arrange
	var screen := DdrScreen.new()
	add_child_autofree(screen)
	screen.start(DdrChart.from_steps("test", 120.0, 1.0, [0]))
	# Act
	screen.confirm()
	screen.confirm()
	screen.advance(0.5)
	# Assert
	assert_eq(screen.state, "play")
	assert_eq(Audio.current_music(), "")
	assert_almost_eq(screen.song_time(), -0.5, 0.001)


func test_ddr_screen_plays_a_song_with_a_file_on_the_audio_autoload() -> void:
	# Arrange: any track that has a file
	var track := "icq_uh_oh"
	assert_true(Audio.has_sound(track))
	var screen := DdrScreen.new()
	add_child_autofree(screen)
	var chart := DdrChart.from_steps("test", 120.0, 1.0, [0])
	chart.audio_path = "res://assets/audio/icq/%s.ogg" % track
	screen.start(chart)
	# Act
	screen.confirm()
	screen.confirm()
	# Assert
	assert_eq(Audio.current_music(), track)
	assert_true(Audio.music_player().playing)
