extends GutTest
## ClawScreen: steer over the pit for up to ArcadeClaw.CONTROL_S seconds, drop (or the timer drops
## it), show the result, then report it. Rules live in ArcadeClaw (see test_arcade_claw.gd).


class FakeState:
	var inventory := {}
	var flags := {}

	func add_item(id: String, count: int = 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func _rng(seed_value: int) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	return r


## Kept out of the tree so _process (real input, real time) never runs; tests call advance().
func _screen(machine_id: String, state: FakeState, blinking: bool) -> ClawScreen:
	var c: ClawScreen = autofree(ClawScreen.new())
	c.setup(machine_id, state, _rng(3), blinking)
	return c


func test_claw_screen_setup_lays_out_the_pit() -> void:
	# Arrange
	var state := FakeState.new()
	# Act
	var c := _screen(ArcadeClaw.RIGGED, state, false)
	# Assert: the top prize sits alone in the rigged pit until it is won.
	assert_eq(c.machine_id, ArcadeClaw.RIGGED)
	assert_eq(c.pit, [{"x": ArcadeClaw.TOP_PRIZE_SLOT, "id": ArcadeClaw.TOP_PRIZE_ID}])
	assert_eq(c.state, "steer")
	assert_eq(c.time_left, ArcadeClaw.CONTROL_S)


func test_claw_screen_steer_stays_inside_the_pit() -> void:
	# Arrange
	var c := _screen(ArcadeClaw.BEANIE, FakeState.new(), false)
	# Act
	c.steer(-1.0, 10.0)
	var left := c.claw_x
	c.steer(1.0, 10.0)
	var right := c.claw_x
	# Assert
	assert_eq(left, 0.0)
	assert_eq(right, 1.0)


func test_claw_screen_steer_moves_at_claw_speed() -> void:
	# Arrange
	var c := _screen(ArcadeClaw.BEANIE, FakeState.new(), false)
	var start := c.claw_x
	# Act
	c.steer(1.0, 0.5)
	# Assert
	assert_almost_eq(c.claw_x, start + ClawScreen.CLAW_SPEED * 0.5, 0.0001)


func test_claw_screen_confirm_drops_and_the_claw_stops_steering() -> void:
	# Arrange
	var c := _screen(ArcadeClaw.BEANIE, FakeState.new(), false)
	# Act
	c.confirm()
	var x := c.claw_x
	c.steer(1.0, 1.0)
	# Assert
	assert_eq(c.state, "drop")
	assert_true(c.result.has("held"))
	assert_eq(c.claw_x, x, "no steering once the claw drops")


func test_claw_screen_timer_drops_the_claw_by_itself() -> void:
	# Arrange
	var c := _screen(ArcadeClaw.BEANIE, FakeState.new(), false)
	# Act
	c.advance(ArcadeClaw.CONTROL_S - 1.0)
	var still_steering := c.state
	c.advance(1.5)
	# Assert
	assert_eq(still_steering, "steer")
	assert_eq(c.state, "drop")
	assert_eq(c.time_left, 0.0)


func test_claw_screen_blinking_rigged_claw_over_the_top_prize_wins_it() -> void:
	# Arrange
	var state := FakeState.new()
	var c := _screen(ArcadeClaw.RIGGED, state, true)
	c.claw_x = ArcadeClaw.TOP_PRIZE_SLOT
	# Act
	c.confirm()
	# Assert
	assert_eq(c.result, {"over": true, "held": true, "id": ArcadeClaw.TOP_PRIZE_ID})
	assert_eq(int(state.inventory.get(ArcadeClaw.TOP_PRIZE_ID, 0)), 1)


func test_claw_screen_dark_rigged_claw_slips() -> void:
	# Arrange
	var state := FakeState.new()
	var c := _screen(ArcadeClaw.RIGGED, state, false)
	c.claw_x = ArcadeClaw.TOP_PRIZE_SLOT
	# Act
	c.confirm()
	# Assert
	assert_eq(c.result, {"over": true, "held": false, "id": ""})
	assert_false(state.inventory.has(ArcadeClaw.TOP_PRIZE_ID))


func test_claw_screen_shows_the_drop_then_reports_the_result() -> void:
	# Arrange
	var c := _screen(ArcadeClaw.RIGGED, FakeState.new(), true)
	c.claw_x = ArcadeClaw.TOP_PRIZE_SLOT
	c.confirm()
	watch_signals(c)
	# Act
	c.advance(ClawScreen.DROP_S * 0.5)
	var mid := c.state
	c.advance(ClawScreen.DROP_S)
	var shown := c.state
	c.confirm()
	# Assert
	assert_eq(mid, "drop")
	assert_eq(shown, "result")
	assert_eq(c.state, "done")
	assert_signal_emitted_with_parameters(c, "finished", [{"over": true, "held": true, "id": ArcadeClaw.TOP_PRIZE_ID}])
	assert_true(c.is_queued_for_deletion())


func test_claw_screen_item_name_reads_the_item_data() -> void:
	# Act / Assert
	assert_eq(ClawScreen.item_name("aa_junk_promise_ish_ring"), "PROMISE-ISH RING")
	assert_eq(ClawScreen.item_name("no_such_prize"), "NO SUCH PRIZE")
