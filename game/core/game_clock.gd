class_name GameClock
extends RefCounted
## The game clock (round v34, author 2026-11-11):
##  - clock_advance = action: time moves only when the bros act (TICK_MINUTES per action).
##  - clock_day_night = binary: night is 20:00-06:00; a screen picks day or night when it loads.
##  - clock_watch = watch_menu: the time shows on Pilsner's watch in the menu, no HUD clock.
##  - clock_closing = bounce_rest: venues throw the bros out at closing; the next rest is morning,
##    which jumps to 10:00.
##  - clock_start = morning: a new game starts at 10:00.
##  - clock_ticks2 = minutes (round v35): a screen change 10, a fight or minigame (cabinet battle,
##    DDR song, claw, skee-ball, foosball) 20, buying or drinking a drink 10, talking free.
## Time is kept in the saved flags as minutes since day 0, 00:00.

const LIVE := true
const KEY := "clock.minutes"
const START_HOUR := 10
const NIGHT_FROM := 20
const NIGHT_UNTIL := 6
const DAY := 1440
## Round v37 drink_tag = alcohol: every alcoholic drink and beer (signature beers, shots, absinthe...)
## is a drink; food, drugs and vapes are not. Items carry "alcohol": true.
static func is_drink(item: Dictionary) -> bool:
	return bool(item.get("alcohol", false))


## Minutes each action costs (round v35).
const TICK_MINUTES := {"screen": 10, "fight": 20, "minigame": 20, "drink": 10, "talk": 0}


static func minutes(state) -> int:
	return int(state.flags.get(KEY, START_HOUR * 60))


static func hour(state) -> int:
	return (minutes(state) % DAY) / 60


static func day(state) -> int:
	return minutes(state) / DAY


## Every clock change settles the clock-counted field statuses: an expired row fires its `then`
## (the Space Cake Timer lands, Eurobound-2xah).
static func set_time(state, total_minutes: int) -> void:
	state.flags[KEY] = total_minutes
	FieldStatus.settle(state)


## An action the bros take ("cabinet", "walk_screen", ...). Unknown or unpriced actions cost nothing.
static func act(state, action: String) -> void:
	set_time(state, minutes(state) + int(TICK_MINUTES.get(action, 0)))


static func is_night(state) -> bool:
	return in_hours(hour(state), NIGHT_FROM, NIGHT_UNTIL)


## True when `h` is in [from, until), wrapping past midnight.
static func in_hours(h: int, from: int, until: int) -> bool:
	return h >= from or h < until if from > until else h >= from and h < until


## Rest: the next morning at 10:00.
static func rest(state) -> void:
	RestEvents.run(state)
	NavigationRoll.on_rest(state)  # Sober returns at rest (Eurobound-eb8)
	var next := day(state) * DAY + START_HOUR * 60
	if next <= minutes(state):
		next += DAY
	set_time(state, next)


## A venue that closes at `closing_hour` and opens at `opening_hour` is shut now.
static func closed(state, opening_hour: int, closing_hour: int) -> bool:
	return not in_hours(hour(state), opening_hour, closing_hour)


## Pilsner's watch face, e.g. "01:07".
static func watch_text(state) -> String:
	var m := minutes(state) % DAY
	return "%02d:%02d" % [m / 60, m % 60]


## Night for a screen loading now (while LIVE; otherwise the screen keeps its own default).
static func night_for_screen(state, fallback: bool) -> bool:
	return is_night(state) if LIVE else fallback


## Cara's group is in the Arcade 20:00-02:00 (round v32), always while the clock isn't live.
static func group_present(state) -> bool:
	return not LIVE or in_hours(hour(state), 20, 2)


## Jakub drinks his way into the late lines after 01:00 (Writers' Room microcopy).
static func late(state) -> bool:
	return LIVE and in_hours(hour(state), 1, NIGHT_UNTIL)
