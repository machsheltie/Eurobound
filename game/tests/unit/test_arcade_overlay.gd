extends GutTest
## ArcadeOverlay: the TOKENS HERE how-many picker and the INSUFFICIENT CREDITS flash. It only shows
## things and reports the player's choice; the hall decides what happens.


func _overlay() -> ArcadeOverlay:
	# Kept out of the tree so _process only runs when a test calls it.
	var o: ArcadeOverlay = autofree(ArcadeOverlay.new())
	return o


func test_arcade_overlay_open_picker_starts_at_one() -> void:
	# Arrange
	var o := _overlay()
	# Act
	o.open_picker(7)
	# Assert
	assert_true(o.is_picking())
	assert_eq(o.count, 1)
	assert_eq(o.max_count, 7)


func test_arcade_overlay_count_stays_between_one_and_the_most() -> void:
	# Arrange
	var o := _overlay()
	o.open_picker(3)
	# Act
	o.change_count(-1)
	var floor_count := o.count
	o.change_count(10)
	var ceiling_count := o.count
	# Assert
	assert_eq(floor_count, 1)
	assert_eq(ceiling_count, 3)


func test_arcade_overlay_count_does_not_move_when_closed() -> void:
	# Arrange
	var o := _overlay()
	# Act
	o.change_count(5)
	# Assert
	assert_eq(o.count, 0)


func test_arcade_overlay_confirm_reports_the_count_and_closes() -> void:
	# Arrange
	var o := _overlay()
	o.open_picker(5)
	o.change_count(2)
	watch_signals(o)
	# Act
	o.confirm()
	# Assert
	assert_signal_emitted_with_parameters(o, "tokens_chosen", [3])
	assert_signal_not_emitted(o, "picker_closed")
	assert_false(o.is_picking())


func test_arcade_overlay_cancel_closes_without_buying() -> void:
	# Arrange
	var o := _overlay()
	o.open_picker(5)
	watch_signals(o)
	# Act
	o.cancel()
	# Assert
	assert_signal_emitted(o, "picker_closed")
	assert_signal_not_emitted(o, "tokens_chosen")
	assert_false(o.is_picking())


func test_arcade_overlay_confirm_and_cancel_do_nothing_when_closed() -> void:
	# Arrange
	var o := _overlay()
	watch_signals(o)
	# Act
	o.confirm()
	o.cancel()
	# Assert
	assert_signal_not_emitted(o, "tokens_chosen")
	assert_signal_not_emitted(o, "picker_closed")


func test_arcade_overlay_flash_shows_the_text_then_finishes() -> void:
	# Arrange
	var o := _overlay()
	watch_signals(o)
	# Act
	o.flash("INSUFFICIENT CREDITS")
	var shown := o.is_flashing()
	var text := o.flash_text()
	o._process(ArcadeOverlay.FLASH_SECONDS * 0.5)
	var midway := o.is_flashing()
	o._process(ArcadeOverlay.FLASH_SECONDS)
	# Assert
	assert_true(shown)
	assert_eq(text, "INSUFFICIENT CREDITS")
	assert_true(midway)
	assert_false(o.is_flashing())
	assert_signal_emit_count(o, "flash_finished", 1)


func test_arcade_overlay_idle_frames_emit_nothing() -> void:
	# Arrange
	var o := _overlay()
	watch_signals(o)
	# Act
	o._process(5.0)
	# Assert
	assert_signal_not_emitted(o, "flash_finished")


func test_arcade_overlay_sovs_text_reads_1_sov_and_n_sovs() -> void:
	# Act / Assert
	assert_eq(ArcadeOverlay.sovs_text(1), "1 SOV")
	assert_eq(ArcadeOverlay.sovs_text(3), "3 SOVS")
	assert_eq(ArcadeOverlay.sovs_text(0), "0 SOVS")
