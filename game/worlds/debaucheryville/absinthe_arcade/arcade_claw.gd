class_name ArcadeClaw
extends RefCounted
## The Absinthe Arcade's two claw machines (author rulings round v26: both claws work; round v28,
## 2026-11-11: ef5_claw_controls, ef5_payout_light_timing, ef5_beanie_odds approved).
##  - Controls (both claws): up to CONTROL_S seconds to steer the claw left/right over the prize pit,
##    press to drop (it drops by itself when time runs out). It grabs whatever is directly under it;
##    over nothing, the play is wasted.
##  - Beanie Baby Claw: a grab over a plush holds 1 time in 3. Prizes can repeat.
##  - Rigged claw: every grab slips unless the PAYOUT light is blinking. The machine counts every
##    play (saved); once PAYOUT_EVERY - 1 plays have gone by since the last blinking play, the light
##    blinks in the hall before the bros pay. That play's grab holds if the claw is over the top
##    prize. The count restarts after any blinking play, hit or miss.
##  - The rigged claw's top prize is Sea-Monkeys (author 2026-11-11: "replace the beer pong saint
##    relic with Sea-Monkey"). Until it is won the pit holds only Sea-Monkeys; after, the junk-shelf
##    prizes (whether those also need the light: ef6_junk_claw_rule, open).
## Prize names: Writers' Room, approved by the author 2026-11-11 (desk, "Approve Gemini's
## favourites"); registered in key_items.json.
## `state` is GameState (inventory, flags, add_item).

const BEANIE := "beanie_baby_claw"
const RIGGED := "rigged_absinthe_claw_machine"
const CONTROL_S := 10.0
const BEANIE_HOLD := 1.0 / 3.0
const PAYOUT_EVERY := 7
const PLAYS_FLAG := "rigged_claw_plays_since_payout"
## Sea-Monkeys has no item entry yet (the NFT doc is ad's); the id is the one the claw grants.
const TOP_PRIZE_ID := "sea_monkeys"
const TOP_PRIZE_FLAG := "sea_monkeys_obtained"
const BEANIE_PRIZES: Array[String] = [
	"aa_claw_pre_emptive_perry", "aa_claw_pets_con_sock_hound", "aa_claw_snorty_bouncer_badger",
	"aa_claw_mugshot_mandy", "aa_claw_minty_rare_mint_bunny"]
const JUNK_PRIZES: Array[String] = [
	"aa_junk_terminal_velocity_terry", "aa_junk_forty_eight_hour_tramp_stamp", "aa_junk_noise_violation"]

## Pit layout, as fractions of the pit width: slot centres and the half-width a grab must land in.
const BEANIE_SLOTS := [0.12, 0.3, 0.5, 0.7, 0.88]
const RIGGED_JUNK_SLOTS := [0.15, 0.4, 0.62, 0.86]
const TOP_PRIZE_SLOT := 0.62
const SLOT_HALF := 0.06


static func is_claw(machine_id: String) -> bool:
	return machine_id == BEANIE or machine_id == RIGGED


static func plays_since_payout(state) -> int:
	return int(state.flags.get(PLAYS_FLAG, 0))


## Whether the rigged claw's PAYOUT light is blinking for the next play.
static func payout_blinking(state) -> bool:
	return plays_since_payout(state) >= PAYOUT_EVERY - 1


static func top_prize_won(state) -> bool:
	return bool(state.flags.get(TOP_PRIZE_FLAG, false))


## The pit for one play: [{"x": centre, "id": item id or ""}]. An empty id is a stand-in prize.
static func layout(machine_id: String, state, rng: RandomNumberGenerator) -> Array:
	var pit := []
	if machine_id == BEANIE:
		for x: float in BEANIE_SLOTS:
			pit.append({"x": x, "id": _pick(BEANIE_PRIZES, rng)})
	elif not top_prize_won(state):
		pit.append({"x": TOP_PRIZE_SLOT, "id": TOP_PRIZE_ID})
	else:
		for x: float in RIGGED_JUNK_SLOTS:
			pit.append({"x": x, "id": _pick(JUNK_PRIZES, rng)})
	return pit


static func _pick(pool: Array, rng: RandomNumberGenerator) -> String:
	return "" if pool.is_empty() else String(pool[rng.randi_range(0, pool.size() - 1)])


## The prize under the claw at `x`, or {} over nothing.
static func under(pit: Array, x: float) -> Dictionary:
	for p: Dictionary in pit:
		if absf(float(p["x"]) - x) <= SLOT_HALF:
			return p
	return {}


## Settles one drop. `blinking` is the light as it was when the bros paid. Returns
## {"over": bool (the claw was over a prize), "held": bool, "id": item id or ""} and, on a hold
## with a real prize, puts it in the inventory. The rigged claw's play count moves on.
static func grab(machine_id: String, pit: Array, x: float, blinking: bool, state, rng: RandomNumberGenerator) -> Dictionary:
	var prize := under(pit, x)
	var result := {"over": not prize.is_empty(), "held": false, "id": ""}
	if machine_id == BEANIE:
		result["held"] = not prize.is_empty() and rng.randf() < BEANIE_HOLD
	else:
		result["held"] = not prize.is_empty() and blinking
		state.flags[PLAYS_FLAG] = 0 if blinking else plays_since_payout(state) + 1
	if result["held"]:
		result["id"] = String(prize["id"])
		if not String(result["id"]).is_empty():
			state.add_item(result["id"])
			if result["id"] == TOP_PRIZE_ID:
				state.flags[TOP_PRIZE_FLAG] = true
	return result
