extends GutTest
## StreetEncounterRules: the pure checks behind street encounters, Option A
## (docs/superpowers/specs/2026-11-16-Eurobound-skjd-proposal.md section 3; Eurobound-iqgo).
## Every number the author has not ruled is null in the rules, so these tests pass fixture values.

const NORTH := Vector3(0, 0, -1)
const SOUTH := Vector3(0, 0, 1)
const EAST := Vector3(1, 0, 0)


# --- first strike by facing (point 3) ----------------------------------------------------------

func test_street_rules_bros_touching_an_enemy_from_behind_strike_first() -> void:
	# The enemy faces north; the bros come up behind it (south of it), facing north.
	var side := StreetEncounterRules.first_strike(Vector3(0, 0, 1), NORTH, Vector3.ZERO, NORTH)
	assert_eq(side, StreetEncounterRules.PARTY)


func test_street_rules_an_enemy_touching_the_bros_from_behind_strikes_first() -> void:
	# The bros face north; the enemy comes up behind them (south of them), facing north.
	var side := StreetEncounterRules.first_strike(Vector3(0, 0, -1), NORTH, Vector3.ZERO, NORTH)
	assert_eq(side, StreetEncounterRules.ENEMY)


func test_street_rules_face_to_face_contact_has_no_first_strike() -> void:
	var side := StreetEncounterRules.first_strike(Vector3(0, 0, 1), NORTH, Vector3.ZERO, SOUTH)
	assert_eq(side, StreetEncounterRules.NONE)


func test_street_rules_back_to_back_contact_has_no_first_strike() -> void:
	var side := StreetEncounterRules.first_strike(Vector3(0, 0, 1), SOUTH, Vector3.ZERO, NORTH)
	assert_eq(side, StreetEncounterRules.NONE)


func test_street_rules_side_on_contact_has_no_first_strike() -> void:
	var side := StreetEncounterRules.first_strike(Vector3(1, 0, 0), NORTH, Vector3.ZERO, NORTH)
	assert_eq(side, StreetEncounterRules.NONE)


func test_street_rules_height_is_ignored_by_the_facing_test() -> void:
	var side := StreetEncounterRules.first_strike(Vector3(0, 3, 1), NORTH, Vector3.ZERO, NORTH)
	assert_eq(side, StreetEncounterRules.PARTY)


func test_street_rules_first_strike_rounds_are_unruled() -> void:
	assert_null(StreetEncounterRules.FIRST_STRIKE_ROUNDS, "the size of the first strike waits on the author")


# --- auto-win (point 4): off until the XP curve is ruled ---------------------------------------

func test_street_rules_auto_win_is_off_while_the_gap_is_unruled() -> void:
	assert_null(StreetEncounterRules.AUTO_WIN_LEVEL_GAP)
	assert_eq(StreetEncounterRules.AUTO_WIN_PARTY_LEVEL, "")
	assert_false(StreetEncounterRules.auto_win(99, 1))


func test_street_rules_auto_win_with_a_fixture_gap_and_measure() -> void:
	assert_true(StreetEncounterRules.auto_win(5, 2, 3, "leader"))
	assert_false(StreetEncounterRules.auto_win(4, 2, 3, "leader"))


func test_street_rules_auto_win_needs_the_enemy_level() -> void:
	assert_false(StreetEncounterRules.auto_win(9, null, 1, "leader"))


func test_street_rules_auto_win_needs_a_party_level_measure() -> void:
	assert_false(StreetEncounterRules.auto_win(9, 1, 1, ""))


func test_street_rules_party_level_by_measure() -> void:
	var party := [{"level": 4}, {"level": 1}, {"level": 7}]
	assert_eq(StreetEncounterRules.party_level(party, "leader"), 4)
	assert_eq(StreetEncounterRules.party_level(party, "lowest"), 1)
	assert_eq(StreetEncounterRules.party_level(party, "average"), 4.0)
	assert_null(StreetEncounterRules.party_level(party, ""))
	assert_null(StreetEncounterRules.party_level([], "leader"))


# --- the SOVS lost on a loss (point 7) ---------------------------------------------------------

func test_street_rules_loss_share_is_half() -> void:
	# Author, Eurobound Desk Eurobound-iqgo-q3: "Half, as EarthBound does".
	assert_eq(StreetEncounterRules.LOSS_SOVS_SHARE, 0.5)
	assert_eq(StreetEncounterRules.sovs_lost(80), 40)


func test_street_rules_half_loss_on_odd_amounts_keeps_the_rounded_up_half() -> void:
	# Implementation detail of "half" (EarthBound way): the bros keep the rounded-up half.
	assert_eq(StreetEncounterRules.sovs_lost(1), 0)
	assert_eq(StreetEncounterRules.sovs_lost(7), 3)
	assert_eq(StreetEncounterRules.sovs_lost(81), 40)
	assert_eq(81 - StreetEncounterRules.sovs_lost(81), 41)
	assert_eq(StreetEncounterRules.sovs_lost(0), 0)


func test_street_rules_loss_share_null_loses_nothing() -> void:
	assert_eq(StreetEncounterRules.sovs_lost(80, null), 0)


func test_street_rules_loss_share_with_a_fixture_share() -> void:
	assert_eq(StreetEncounterRules.sovs_lost(80, 0.25), 20)


func test_street_rules_loss_share_never_takes_more_than_is_on_hand() -> void:
	assert_eq(StreetEncounterRules.sovs_lost(10, 2.0), 10)
	assert_eq(StreetEncounterRules.sovs_lost(0, 0.5), 0)
	assert_eq(StreetEncounterRules.sovs_lost(10, -1.0), 0)


# --- grace (point 5) ---------------------------------------------------------------------------

func test_street_rules_grace_counts_in_steps_but_its_number_is_unruled() -> void:
	# Author, Eurobound Desk Eurobound-iqgo-q2: "Count it in steps (walking distance)".
	assert_eq(StreetEncounterRules.GRACE_UNIT, StreetEncounterRules.UNIT_STEPS)
	assert_null(StreetEncounterRules.GRACE_LENGTH)
