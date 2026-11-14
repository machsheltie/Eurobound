extends GutTest
## SoundRegistry (Eurobound-pqe9): sound ids come from the data the game already has, files from
## res://assets/audio. An id is the file's name without its extension. Nothing here picks a sound.

const FIXTURE_DATA := "res://tests/fixtures/audio/data/"
const CLUB := "res://assets/audio/velvet_curtain_club/"

var reg: SoundRegistry


func before_each() -> void:
	reg = SoundRegistry.new()
	reg.data_root = FIXTURE_DATA


func test_sound_registry_resolves_an_id_to_the_audio_file_of_the_same_name() -> void:
	# Act / Assert
	assert_eq(reg.path_for("qr_code_scan_beep"), CLUB + "qr_code_scan_beep.ogg")


func test_sound_registry_resolves_a_file_no_data_names() -> void:
	# Act / Assert: icq_uh_oh is on disk and in no fixture row
	assert_eq(reg.path_for("icq_uh_oh"), "res://assets/audio/icq/icq_uh_oh.ogg")
	assert_true(reg.has_id("icq_uh_oh"))


func test_sound_registry_collects_ids_from_cue_keys_as_string_list_or_dictionary() -> void:
	# Act
	var ids := reg.declared_ids()
	# Assert
	for id in ["qr_code_scan_beep", "fixture_success_chime", "fixture_claw_sound", "fixture_clip_a", "fixture_clip_b"]:
		assert_has(ids, id)


func test_sound_registry_skips_prose_under_a_cue_key() -> void:
	# Act / Assert
	assert_false(reg.has_id("This is prose, not an id"))


func test_sound_registry_collects_file_names_as_ids() -> void:
	# Act / Assert
	assert_true(reg.has_id("fixture_press"))
	assert_true(reg.has_id("fixture_not_made_yet"))


func test_sound_registry_file_row_description_is_a_second_id_for_that_file() -> void:
	# Act / Assert: {"file": "vip_bathroom_nft_discovery.ogg", "description": "fixture_success_chime"}
	assert_eq(reg.path_for("fixture_success_chime"), CLUB + "vip_bathroom_nft_discovery.ogg")


func test_sound_registry_file_row_carries_volume_and_loop() -> void:
	# Act
	var chime := reg.entry("fixture_success_chime")
	var bed := reg.entry("fixture_not_made_yet")
	# Assert
	assert_almost_eq(float(chime["volume"]), 0.8, 0.001)
	assert_false(bool(chime["loop"]))
	assert_almost_eq(float(bed["volume"]), 0.6, 0.001)
	assert_true(bool(bed["loop"]))


func test_sound_registry_declared_id_without_a_file_has_no_path() -> void:
	# Act / Assert
	assert_eq(reg.path_for("fixture_not_made_yet"), "")
	assert_has(reg.missing_ids(), "fixture_not_made_yet")
	assert_does_not_have(reg.missing_ids(), "qr_code_scan_beep")


func test_sound_registry_unknown_id_is_not_declared_and_has_no_path() -> void:
	# Act / Assert
	assert_false(reg.has_id("no_such_sound"))
	assert_eq(reg.path_for("no_such_sound"), "")
	assert_eq(reg.entry("no_such_sound"), {"path": "", "volume": 1.0, "loop": false})


func test_sound_registry_missing_folders_give_an_empty_registry() -> void:
	# Arrange
	reg.data_root = "res://tests/fixtures/audio/nowhere/"
	reg.audio_root = "res://tests/fixtures/audio/nowhere/"
	# Act / Assert
	assert_eq(reg.declared_ids(), [])
	assert_eq(reg.path_for("qr_code_scan_beep"), "")


func test_sound_registry_game_data_resolves_the_vip_stall_cues() -> void:
	# Arrange: the real data (debaucheryville_interactions.json audio_cue / success_audio_cue)
	var real := SoundRegistry.new()
	# Act / Assert
	assert_eq(real.path_for("qr_code_scan_beep"), CLUB + "qr_code_scan_beep.ogg")
	assert_eq(real.path_for("triumphant_nft_discovery_chime"), CLUB + "vip_bathroom_nft_discovery.ogg")
	assert_almost_eq(float(real.entry("triumphant_nft_discovery_chime")["volume"]), 0.8, 0.001)


func test_sound_registry_game_data_declares_ids_that_have_no_file_yet() -> void:
	# Arrange
	var real := SoundRegistry.new()
	# Act / Assert: debaucheryville_environmental.json ambient_tracks.primary
	assert_true(real.has_id("warped_8bit_arcade_ambience"))
	assert_true(bool(real.entry("warped_8bit_arcade_ambience")["loop"]))
	assert_eq(real.path_for("warped_8bit_arcade_ambience"), "")
