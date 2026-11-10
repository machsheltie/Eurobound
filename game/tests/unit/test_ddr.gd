extends GutTest
## The Absinthe Arcade DDR dance-off (ledger 2026-11-09/10): four arrow lanes like real DDR,
## 2 tokens per song, 0-30 tickets by score, and a difficulty screen stuck on EXPERT.


func _chart() -> DdrChart:
	# 120 BPM, a note every beat across the four lanes, first beat at 1.0 s
	return DdrChart.from_steps("test", 120.0, 1.0, [0, 1, 2, 3, 0, 1, 2, 3])


func test_ddr_chart_places_steps_on_the_beat() -> void:
	# Act
	var c := _chart()

	# Assert
	assert_eq(c.notes.size(), 8)
	assert_almost_eq(float(c.notes[0]["time"]), 1.0, 0.0001)
	assert_almost_eq(float(c.notes[1]["time"]), 1.5, 0.0001)
	assert_eq(int(c.notes[3]["lane"]), 3)


func test_ddr_chart_loads_from_json() -> void:
	# Arrange
	var path := "user://test_ddr_chart.json"
	var f := FileAccess.open(path, FileAccess.WRITE)
	f.store_string(JSON.stringify({"title": "T", "artist": "A", "audio": "", "notes": [[2.0, 1], [1.0, 0]]}))
	f.close()

	# Act
	var c := DdrChart.load_file(path)

	# Assert: notes come back sorted by time
	assert_eq(c.title, "T")
	assert_eq(c.notes.size(), 2)
	assert_eq(int(c.notes[0]["lane"]), 0)
	DirAccess.remove_absolute(ProjectSettings.globalize_path(path))


func test_ddr_judge_on_time_is_perfect() -> void:
	# Arrange
	var j := DdrJudge.new(_chart())

	# Act / Assert
	assert_eq(j.hit(0, 1.01), "PERFECT")
	assert_eq(j.hit(1, 1.5 + 0.06), "GREAT")
	assert_eq(j.hit(2, 2.0 - 0.12), "GOOD")


func test_ddr_judge_wrong_lane_or_far_off_hits_nothing() -> void:
	# Arrange
	var j := DdrJudge.new(_chart())

	# Act / Assert
	assert_eq(j.hit(3, 1.0), "", "no lane-3 note near 1.0 s")
	assert_eq(j.hit(0, 1.4), "", "too far from the beat")


func test_ddr_judge_a_note_counts_once() -> void:
	# Arrange
	var j := DdrJudge.new(_chart())
	j.hit(0, 1.0)

	# Act
	var again := j.hit(0, 1.02)

	# Assert
	assert_eq(again, "")


func test_ddr_judge_unplayed_notes_become_misses() -> void:
	# Arrange
	var j := DdrJudge.new(_chart())

	# Act: the song ends untouched
	j.update(99.0)

	# Assert
	assert_eq(j.counts["MISS"], 8)
	assert_true(j.finished())
	assert_eq(j.tickets(), 0)


func test_ddr_judge_a_perfect_song_pays_30_tickets() -> void:
	# Arrange
	var c := _chart()
	var j := DdrJudge.new(c)

	# Act
	for n in c.notes:
		j.hit(int(n["lane"]), float(n["time"]))
	j.update(99.0)

	# Assert
	assert_eq(j.tickets(), DdrJudge.MAX_TICKETS)
	assert_eq(DdrJudge.MAX_TICKETS, 30)


func test_ddr_judge_half_the_song_pays_about_half() -> void:
	# Arrange
	var c := _chart()
	var j := DdrJudge.new(c)

	# Act: perfect on the first four, nothing after
	for i in 4:
		j.hit(int(c.notes[i]["lane"]), float(c.notes[i]["time"]))
	j.update(99.0)

	# Assert
	assert_eq(j.tickets(), 15)


func test_ddr_difficulty_is_stuck_on_expert() -> void:
	# Arrange
	var d := DdrDifficulty.new()

	# Act
	var moved_left := d.move(-1)
	var moved_right := d.move(1)

	# Assert
	assert_eq(d.selected(), "EXPERT")
	assert_false(moved_left)
	assert_false(moved_right)
	assert_eq(d.refusals, 2, "every try is counted, for the bros to complain about")


func test_ddr_costs_two_tokens_a_song() -> void:
	assert_eq(ArcadeRules.play_cost("ddr_dance_off"), 2)


func test_ddr_screen_plays_a_song_through_to_the_tickets() -> void:
	# Arrange
	var screen := DdrScreen.new()
	add_child_autofree(screen)
	screen.start(DdrChart.from_steps("test", 120.0, 1.0, [0, 1]))
	watch_signals(screen)

	# Act: try to change the difficulty, give up, pick Chadwick, hit the first step, miss the second
	screen.move_cursor(-1)
	assert_eq(screen.difficulty.selected(), "EXPERT")
	screen.confirm()
	screen.move_cursor(1)
	screen.confirm()
	assert_eq(screen.state, "play")
	assert_eq(screen.bro, "chadwick")
	screen.advance(2.0)  # 1 s lead-in, then to the first beat
	var j := screen.press_lane(0)
	screen.advance(99.0)
	assert_eq(screen.state, "results")
	screen.confirm()

	# Assert
	assert_eq(j, "PERFECT")
	assert_signal_emitted_with_parameters(screen, "finished", [15, "chadwick"])
