extends GutTest
## ICQ message queue on top of the FREE Wi-Fi hotspot (author round v42): conditions, first-time
## rules, the later-connection popup, and the bros locked while the window is up.

const SCENE := preload("res://worlds/shared/icq/wifi_hotspot.tscn")


class FakeState:
	var flags := {}


class FakePlayer:
	extends Node
	var input_locked := false


func _queue() -> IcqQueue:
	var q := IcqQueue.new()
	q.messages = [
		{"id": "a", "sender": "T", "lines": ["one"], "hotspots": ["h1"], "once": true,
			"requires_flags": ["f"], "blocks_flags": []},
		{"id": "b", "sender": "U", "lines": ["two"], "hotspots": [], "once": false,
			"requires_flags": [], "blocks_flags": ["stop"]},
	]
	return q


func _hotspot() -> WifiHotspot:
	var h: WifiHotspot = SCENE.instantiate()
	h.state = FakeState.new()
	h.dialogue = DialogueBox.new()
	h.dialogue.beat_scale = 0.01
	h.add_child(h.dialogue)
	add_child_autofree(h)
	return h


## Runs one connection to the end, pressing through every line; returns "speaker|text" per line.
func _run(h: WifiHotspot) -> Array:
	var said := []
	h.interact()
	for i in 300:
		if h.dialogue.mode == "say":
			said.append(h.dialogue.speaker + "|" + h.dialogue.text)
			h.dialogue.press("interact")
		if not h.busy:
			break
		await wait_process_frames(1)
	return said


func test_icq_queue_filters_by_hotspot_and_required_flag() -> void:
	# Arrange
	var s := FakeState.new()
	var q := _queue()
	# Act / Assert
	assert_eq(q.next_for(s, "h1")["id"], "b", "a needs its flag")
	s.flags["f"] = true
	assert_eq(q.next_for(s, "h1")["id"], "a")
	assert_eq(q.next_for(s, "h2")["id"], "b", "a is tied to h1")


func test_icq_queue_once_messages_fire_a_single_time() -> void:
	# Arrange
	var s := FakeState.new()
	s.flags["f"] = true
	var q := _queue()
	# Act
	var first := q.take(s, "h1")
	var second := q.take(s, "h1")
	# Assert
	assert_eq(first["id"], "a")
	assert_eq(second["id"], "b")
	assert_true(s.flags.has("icq_seen_a"))


func test_icq_queue_blocking_flag_empties_the_queue() -> void:
	# Arrange
	var s := FakeState.new()
	s.flags["stop"] = true
	# Act / Assert
	assert_true(_queue().next_for(s, "h2").is_empty())


func test_icq_queue_shipped_messages_cite_a_source_line() -> void:
	# Arrange / Act
	var q := IcqQueue.from_file()
	# Assert
	assert_gt(q.messages.size(), 0)
	for m: Dictionary in q.messages:
		assert_true(String(m.get("source", "")).contains(".md:"), "%s cites path:line" % m.get("id"))
		assert_false(m["lines"].is_empty())


func test_icq_queue_shipped_messages_wait_for_the_tony420_hijack() -> void:
	# Arrange
	var s := FakeState.new()
	# Act / Assert
	assert_true(IcqQueue.from_file().next_for(s, "any").is_empty(), "nothing before the first hijack")


func test_icq_queue_first_connection_hijacks_and_second_shows_the_queued_message() -> void:
	# Arrange
	var h := _hotspot()
	# Act
	var first := await _run(h)
	var second := await _run(h)
	# Assert
	assert_true(h.state.flags["tony420_unlocked"])
	assert_eq(first[0], "TONY420|yo")
	assert_eq(second.size(), 1)
	assert_true(second[0].begins_with("Tony420|50 mooncum"))
	assert_true(h.state.flags["icq_seen_icq_tony420_xanax_pitch"])


func test_icq_queue_locks_the_bros_while_the_window_is_up() -> void:
	# Arrange
	var h := _hotspot()
	var p := FakePlayer.new()
	add_child_autofree(p)
	h.player = p
	var locked_when_opened := []
	h.icq.visibility_changed.connect(func() -> void: locked_when_opened.append(p.input_locked))
	# Act
	await _run(h)
	# Assert
	assert_true(locked_when_opened.has(true), "locked while the window is up")
	assert_false(p.input_locked, "released afterwards")


func test_icq_queue_hamstradamus_is_queued_verbatim_and_gated() -> void:
	# Arrange
	var q := IcqQueue.from_file()
	var ham := {}
	for m: Dictionary in q.messages:
		if m.get("sender") == "Hamstradamus":
			ham = m
	var locked := FakeState.new()
	var open := FakeState.new()
	open.flags["tony420_unlocked"] = true
	open.flags["icq_seen_icq_tony420_xanax_pitch"] = true
	open.flags["icq_seen_icq_cryptobro69_kebab_monkey"] = true
	# Act / Assert
	assert_false(ham.is_empty(), "Hamstradamus is in the queue")
	assert_eq(ham["lines"], ["REPENT BEFORE THE CLOCK TICKS 00:00 OR YOUR NOKIA SHALL BECOME A TOASTER."])
	assert_eq(ham["source"], "design/worlds/shared/interactables/wifihotspots.md:11")
	assert_true(q.next_for(locked, "any").is_empty(), "gated on the first hijack")
	assert_eq(q.next_for(open, "any").get("sender"), "Hamstradamus")
