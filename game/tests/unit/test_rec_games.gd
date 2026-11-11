extends GutTest
## Skee-ball and foosball in the Absinthe Arcade hall (author ruling rec_games, round v25: real
## mini-games; costs and payouts delegated: skee-ball 2 tokens, 9 balls, 0-20 tickets by score;
## foosball 2 tokens against the house, 15 tickets for a win, 3 for a loss).


# --- Skee-ball ---

func test_skee_ball_power_picks_the_ring() -> void:
	# Arrange: dead-centre rolls, weakest to strongest
	var cases := {0.1: 0, 0.3: 10, 0.45: 20, 0.6: 30, 0.75: 40, 0.85: 50}

	for power: float in cases.keys():
		# Act
		var points := SkeeBall.pocket(0.0, power)

		# Assert
		assert_eq(points, cases[power], "power %s" % power)


func test_skee_ball_full_power_into_a_corner_is_the_hundred() -> void:
	assert_eq(SkeeBall.pocket(0.8, 0.95), 100)
	assert_eq(SkeeBall.pocket(-0.8, 0.95), 100)


func test_skee_ball_full_power_up_the_middle_drops_into_the_ten() -> void:
	assert_eq(SkeeBall.pocket(0.0, 0.95), 10)


func test_skee_ball_off_centre_clips_the_ring_down_one() -> void:
	assert_eq(SkeeBall.pocket(0.6, 0.85), 40)
	assert_eq(SkeeBall.pocket(0.6, 0.45), 10)


func test_skee_ball_off_the_side_rail_is_the_ten() -> void:
	assert_eq(SkeeBall.pocket(0.95, 0.85), 10)


func test_skee_ball_nine_balls_then_done() -> void:
	# Arrange
	var game := SkeeBall.new()

	# Act
	for i in SkeeBall.BALLS:
		assert_false(game.finished())
		game.roll(0.0, 0.85)

	# Assert
	assert_true(game.finished())
	assert_eq(game.score, 450)
	assert_eq(game.roll(0.0, 0.85), -1, "no tenth ball")
	assert_eq(game.score, 450)


func test_skee_ball_tickets_scale_with_score_and_cap_at_twenty() -> void:
	var game := SkeeBall.new()
	assert_eq(game.tickets(), 0)
	game.score = 225
	assert_eq(game.tickets(), 10)
	game.score = 450
	assert_eq(game.tickets(), 20)
	game.score = 900
	assert_eq(game.tickets(), 20)


# --- Foosball ---

func _foos() -> Foosball:
	var rng := RandomNumberGenerator.new()
	rng.seed = 7
	return Foosball.new(rng)


func test_foosball_ball_in_the_house_goal_scores_for_the_bros() -> void:
	# Arrange: the ball rolling into the house goal mouth, past everyone
	var game := _foos()
	game.ball = Vector2(Foosball.FIELD.x - 0.01, Foosball.FIELD.y * 0.5)
	game.velocity = Vector2(1.0, 0.0)

	# Act
	game.step(0.05)

	# Assert
	assert_eq(game.bros_goals, 1)
	assert_eq(game.house_goals, 0)
	assert_eq(game.ball, Foosball.FIELD * 0.5, "served again from the middle")


func test_foosball_ball_in_the_bros_goal_scores_for_the_house() -> void:
	var game := _foos()
	game.ball = Vector2(0.01, Foosball.FIELD.y * 0.5)
	game.velocity = Vector2(-1.0, 0.0)

	game.step(0.05)

	assert_eq(game.house_goals, 1)


func test_foosball_end_wall_outside_the_goal_bounces() -> void:
	var game := _foos()
	game.ball = Vector2(0.01, 0.05)
	game.velocity = Vector2(-1.0, 0.0)

	game.step(0.05)

	assert_eq(game.house_goals, 0)
	assert_gt(game.velocity.x, 0.0)


func test_foosball_side_wall_bounces() -> void:
	var game := _foos()
	game.ball = Vector2(0.5, 0.01)
	game.velocity = Vector2(0.0, -1.0)

	game.step(0.05)

	assert_gt(game.velocity.y, 0.0)


func test_foosball_a_bros_man_kicks_toward_the_house_goal() -> void:
	# Arrange: the ball arriving at one of the bros' strikers
	var game := _foos()
	var man: Vector2 = game.men("bros")[-1]
	game.ball = man + Vector2(Foosball.MAN_RADIUS + Foosball.BALL_RADIUS - 0.005, 0)
	game.velocity = Vector2(-0.5, 0.0)

	# Act
	game.step(0.001)

	# Assert
	assert_gt(game.velocity.x, 0.0)


func test_foosball_the_house_kicks_toward_the_bros_goal() -> void:
	var game := _foos()
	var man: Vector2 = game.men("house")[0]
	game.ball = man - Vector2(Foosball.MAN_RADIUS + Foosball.BALL_RADIUS - 0.005, 0)
	game.velocity = Vector2(0.5, 0.0)

	game.step(0.001)

	assert_lt(game.velocity.x, 0.0)


func test_foosball_the_bros_rods_move_with_the_stick_and_stay_on_the_table() -> void:
	var game := _foos()
	var before: float = game.men("bros")[0].y

	game.move_rods(1.0, 0.1)
	assert_gt(game.men("bros")[0].y, before)

	game.move_rods(1.0, 10.0)
	for m: Vector2 in game.men("bros"):
		assert_between(m.y, 0.0, Foosball.FIELD.y)


func test_foosball_first_to_five_and_the_payout() -> void:
	var game := _foos()
	assert_false(game.finished())
	game.bros_goals = Foosball.WIN_GOALS
	assert_true(game.finished())
	assert_true(game.bros_won())
	assert_eq(game.tickets(), 15)

	game.bros_goals = 2
	game.house_goals = Foosball.WIN_GOALS
	assert_false(game.bros_won())
	assert_eq(game.tickets(), 3)


func test_foosball_and_skee_ball_cost_two_tokens() -> void:
	assert_eq(ArcadeRules.play_cost("skee_ball"), 2)
	assert_eq(ArcadeRules.play_cost("foosball"), 2)
