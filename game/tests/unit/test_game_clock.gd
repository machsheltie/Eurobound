extends GutTest
## GameClock (round v34): starts 10:00, night 20:00-06:00, rest jumps to the next 10:00.

class FakeState:
	var flags := {}


func test_game_clock_new_game_starts_at_ten_in_the_day() -> void:
	# Arrange
	var s := FakeState.new()
	# Act / Assert
	assert_eq(GameClock.watch_text(s), "10:00")
	assert_false(GameClock.is_night(s))


func test_game_clock_night_is_twenty_to_six() -> void:
	# Arrange
	var s := FakeState.new()
	var checks := {}
	# Act
	for h in [5, 6, 19, 20, 23, 0]:
		GameClock.set_time(s, h * 60)
		checks[h] = GameClock.is_night(s)
	# Assert
	assert_eq(checks, {5: true, 6: false, 19: false, 20: true, 23: true, 0: true})


func test_game_clock_rest_jumps_to_the_next_morning() -> void:
	# Arrange: 01:30 on day 2, then 08:00 on day 3.
	var s := FakeState.new()
	GameClock.set_time(s, 2 * 1440 + 90)
	GameClock.rest(s)
	var after_late := GameClock.minutes(s)
	GameClock.set_time(s, 3 * 1440 + 480)
	# Act
	GameClock.rest(s)
	# Assert
	assert_eq(after_late, 2 * 1440 + 600)
	assert_eq(GameClock.minutes(s), 3 * 1440 + 600)


func test_game_clock_hours_wrap_past_midnight() -> void:
	# Act / Assert
	assert_true(GameClock.in_hours(1, 20, 2))
	assert_false(GameClock.in_hours(3, 20, 2))
	assert_true(GameClock.in_hours(21, 20, 2))


func test_game_clock_unpriced_actions_cost_nothing_until_ticks_are_ruled() -> void:
	# Arrange
	var s := FakeState.new()
	# Act
	GameClock.act(s, "cabinet")
	# Assert
	assert_eq(GameClock.minutes(s), 600)
