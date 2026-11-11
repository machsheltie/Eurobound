extends GutTest
## ArcadeClaw: the Beanie claw's 1-in-3 grip and the rigged claw's PAYOUT light cycle (round v28).


class FakeState:
	var inventory := {}
	var flags := {}

	func add_item(id: String, count: int = 1) -> void:
		inventory[id] = int(inventory.get(id, 0)) + count


func _rng(seed_value: int) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = seed_value
	return r


func test_arcade_claw_light_blinks_on_the_seventh_play() -> void:
	# Arrange
	var state := FakeState.new()
	var pit := ArcadeClaw.layout(ArcadeClaw.RIGGED, state, _rng(1))
	var blinks := []
	# Act: fourteen plays that all miss.
	for i in 14:
		var on := ArcadeClaw.payout_blinking(state)
		blinks.append(on)
		ArcadeClaw.grab(ArcadeClaw.RIGGED, pit, 0.0, on, state, _rng(i))
	# Assert: plays 7 and 14 blink, and a blinking miss restarts the count.
	var at := []
	for i in blinks.size():
		if blinks[i]:
			at.append(i + 1)
	assert_eq(at, [7, 14])


func test_arcade_claw_rigged_grab_slips_unless_blinking() -> void:
	# Arrange
	var state := FakeState.new()
	var pit := ArcadeClaw.layout(ArcadeClaw.RIGGED, state, _rng(1))
	# Act
	var dark := ArcadeClaw.grab(ArcadeClaw.RIGGED, pit, ArcadeClaw.RELIC_SLOT, false, state, _rng(2))
	var lit := ArcadeClaw.grab(ArcadeClaw.RIGGED, pit, ArcadeClaw.RELIC_SLOT, true, state, _rng(3))
	# Assert
	assert_false(dark["held"])
	assert_true(lit["held"])
	assert_eq(int(state.inventory.get(ArcadeClaw.RELIC_ID, 0)), 1)
	assert_true(ArcadeClaw.relic_won(state))


func test_arcade_claw_blinking_grab_over_nothing_still_misses() -> void:
	# Arrange
	var state := FakeState.new()
	var pit := ArcadeClaw.layout(ArcadeClaw.RIGGED, state, _rng(1))
	# Act
	var r := ArcadeClaw.grab(ArcadeClaw.RIGGED, pit, 0.05, true, state, _rng(2))
	# Assert
	assert_false(r["over"])
	assert_false(r["held"])
	assert_eq(ArcadeClaw.plays_since_payout(state), 0)


func test_arcade_claw_relic_leaves_the_pit_once_won() -> void:
	# Arrange
	var state := FakeState.new()
	state.flags[ArcadeClaw.RELIC_FLAG] = true
	# Act
	var pit := ArcadeClaw.layout(ArcadeClaw.RIGGED, state, _rng(1))
	# Assert
	assert_false(pit.any(func(p: Dictionary) -> bool: return p["id"] == ArcadeClaw.RELIC_ID))


func test_arcade_claw_beanie_grip_holds_about_one_in_three() -> void:
	# Arrange
	var state := FakeState.new()
	var pit := [{"x": 0.5, "id": "plush_test"}]
	var held := 0
	# Act
	for i in 3000:
		if ArcadeClaw.grab(ArcadeClaw.BEANIE, pit, 0.5, false, state, _rng(i))["held"]:
			held += 1
	# Assert
	assert_almost_eq(held / 3000.0, 1.0 / 3.0, 0.03)
	assert_eq(int(state.inventory["plush_test"]), held)


func test_arcade_claw_beanie_over_nothing_is_wasted() -> void:
	# Arrange
	var state := FakeState.new()
	var pit := ArcadeClaw.layout(ArcadeClaw.BEANIE, state, _rng(1))
	# Act
	var r := ArcadeClaw.grab(ArcadeClaw.BEANIE, pit, 0.21, false, state, _rng(1))
	# Assert
	assert_false(r["over"])
	assert_false(r["held"])
