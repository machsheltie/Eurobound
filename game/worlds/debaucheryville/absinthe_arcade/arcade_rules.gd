class_name ArcadeRules
extends RefCounted
## Absinthe Arcade money: tokens and tickets, kept in GameState's inventory.
##  - 1 token = 1 SOV; Frogger costs 2 tokens, Street Fighter 3, Kebab Kombat 4, DDR 2 per song
##    (author rulings 2026-11-09); skee-ball and foosball 2 each (round v25, delegated); the rigged claw 5 (the Beanie claw is a placeholder).
##  - The TOKENS HERE machine sells any number of tokens; they sit in the inventory and cabinets
##    spend them (author ruling ef_tokens = machine_any, 2026-11-10).
##  - Arcade fights pay tickets, not SOVS (ruling 2026-11-09), redeemed at the Prize Redemption
##    counter for key items priced in tickets.
## `state` is GameState (or anything with gold, inventory and add_item).

const TOKEN_ID := "item_absinthe_arcade_token"
const TICKET_ID := "arcade_tickets"
const SOVS_PER_TOKEN := 1
const PLAY_COST := {
	"cabinet_frogger": 2,
	"cabinet_street_fighter": 3,
	"cabinet_kebab_kombat": 4,
	"ddr_dance_off": 2,
	"skee_ball": 2,    # round v25: rec-game numbers delegated to Claude
	"foosball": 2,
	"beanie_baby_claw": 5,               # PLACEHOLDER: unruled (round v29 beanie_price, 2 proposed)
	"rigged_absinthe_claw_machine": 5,   # ruled 2026-11-02 ("claw 5")
}


static func play_cost(machine_id: String) -> int:
	return int(PLAY_COST.get(machine_id, 0))


static func tokens(state) -> int:
	return int(state.inventory.get(TOKEN_ID, 0))


static func tickets(state) -> int:
	return int(state.inventory.get(TICKET_ID, 0))


## The most tokens the wallet can pay for.
static func max_buyable(state) -> int:
	return maxi(int(state.gold), 0) / SOVS_PER_TOKEN


static func buy_tokens(state, count: int) -> bool:
	if count <= 0 or count > max_buyable(state):
		return false
	state.gold -= count * SOVS_PER_TOKEN
	state.add_item(TOKEN_ID, count)
	return true


static func can_play(state, machine_id: String) -> bool:
	var cost := play_cost(machine_id)
	return cost > 0 and tokens(state) >= cost


## Spends a play's tokens. False (and nothing spent) when the bros are short.
static func pay_for_play(state, machine_id: String) -> bool:
	if not can_play(state, machine_id):
		return false
	_take(state, TOKEN_ID, play_cost(machine_id))
	return true


static func add_tickets(state, count: int) -> void:
	if count > 0:
		state.add_item(TICKET_ID, count)


static func _take(state, id: String, count: int) -> void:
	var left := int(state.inventory.get(id, 0)) - count
	if left > 0:
		state.inventory[id] = left
	else:
		state.inventory.erase(id)
