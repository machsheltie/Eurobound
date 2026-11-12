extends GutTest
## FREE Wi-Fi hotspot (bead Eurobound-00i): interact -> ICQ window opens -> Tony420Hijack runs ->
## tony420_unlocked is set on the first run only.

const SCENE := preload("res://worlds/shared/icq/wifi_hotspot.tscn")


class FakeState:
	var flags := {}


class FakeStream:
	extends AudioStreamWAV


func _hotspot() -> WifiHotspot:
	var h: WifiHotspot = SCENE.instantiate()
	h.state = FakeState.new()
	h.dialogue = DialogueBox.new()
	h.dialogue.beat_scale = 0.01
	h.add_child(h.dialogue)
	add_child_autofree(h)
	return h


func _run(h: WifiHotspot) -> Array:
	var results := []
	h.hijack_finished.connect(func(who, first): results.append([who, first]))
	h.interact()
	var opened := h.icq.is_open()
	for i in 300:
		if not results.is_empty():
			break
		if h.dialogue.mode == "say":
			h.dialogue.press("interact")
		await wait_process_frames(1)
	return [opened, results]


func test_wifi_hotspot_interact_opens_icq_and_runs_first_hijack() -> void:
	# Arrange
	var h := _hotspot()
	assert_false(h.icq.is_open())
	# Act
	var out := await _run(h)
	# Assert
	assert_true(out[0], "ICQ window open while the hijack runs")
	assert_eq(out[1], [["tony420", true]])
	assert_true(h.state.flags.get("tony420_unlocked", false))
	assert_false(h.icq.is_open(), "window closes afterwards")
	assert_false(h.busy)


func test_wifi_hotspot_second_interact_is_not_the_first_hijack() -> void:
	# Arrange
	var h := _hotspot()
	await _run(h)
	# Act
	var out := await _run(h)
	# Assert
	assert_eq(out[1], [["tony420", false]], "unlock only on first run")
	assert_true(h.state.flags["tony420_unlocked"])


func test_wifi_hotspot_cue_without_stream_is_a_noop() -> void:
	# Arrange
	var h := _hotspot()
	# Act
	h.cue("icq_uh_oh")
	# Assert
	assert_false(h._player.playing)


func test_wifi_hotspot_cue_with_stream_plays_it() -> void:
	# Arrange
	var h := _hotspot()
	var s := FakeStream.new()
	h.cue_streams = {"icq_uh_oh": s}
	# Act
	h.cue("icq_uh_oh")
	# Assert
	assert_eq(h._player.stream, s)


func test_wifi_hotspot_is_an_interactable_and_defaults_to_tony420() -> void:
	# Arrange / Act
	var h := _hotspot()
	# Assert
	assert_true(h.is_in_group("interactable"))
	assert_eq(h.hijacker(), "tony420")
