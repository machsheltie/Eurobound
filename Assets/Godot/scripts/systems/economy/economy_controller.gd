extends Node
class_name EconomyController
## Global economy + barter/rate glue for Shadow Exchange and shops.
## Make this an Autoload (Project Settings → AutoLoad) so you can call EconomyController.* anywhere.

signal gold_changed(new_gold: int)
signal item_granted(item_id: String, count: int)
signal rate_updated(source_id: String, rate: float)
signal premium_stock_unlocked()

@export var starting_gold: int = 100

var gold: int
var rates: Dictionary = {}          # e.g., {"shadow_exchange": 0.97}
var inventory: Dictionary = {}      # simple fallback if you don't have a dedicated InventoryController
var premium_unlocked: bool = false

func _ready() -> void:
	gold = starting_gold
	rates["shadow_exchange"] = 1.0

# --- Rates & Exchange ---

func apply_rate(rate: float, source_id: String = "shadow_exchange") -> void:
	# Called from RateBoard.rate_locked(rate)
	rates[source_id] = max(0.01, rate)
	emit_signal("rate_updated", source_id, rates[source_id])

func get_rate(source_id: String = "shadow_exchange") -> float:
	return float(rates.get(source_id, 1.0))

func convert_currency(amount: int, source_id: String = "shadow_exchange") -> int:
	# Converts foreign 'amount' into Gold using chosen source rate
	var r := get_rate(source_id)
	return int(round(amount * r))

func try_exchange(foreign_cost: int, source_id: String = "shadow_exchange") -> bool:
	# Deducts Gold based on current rate; returns true if successful
	var gold_cost := convert_currency(foreign_cost, source_id)
	if gold_cost <= gold:
		add_gold(-gold_cost)
		return true
	return false

# --- Gold & Inventory ---

func add_gold(delta: int) -> void:
	gold = max(0, gold + delta)
	emit_signal("gold_changed", gold)

func grant_reward(item_id: String, count: int = 1) -> void:
	inventory[item_id] = int(inventory.get(item_id, 0)) + count
	emit_signal("item_granted", item_id, count)

func has_item(item_id: String, count: int = 1) -> bool:
	return int(inventory.get(item_id, 0)) >= count

func take_item(item_id: String, count: int = 1) -> bool:
	if not has_item(item_id, count):
		return false
	inventory[item_id] = int(inventory.get(item_id, 0)) - count
	return true

# --- Shadow Exchange glue ---

func handle_barter_result(success: bool, reward: String) -> void:
	# Connect BarterCounter.barter_result → this
	if success and reward != "":
		grant_reward(reward, 1)

func verification_fee(cost_gold: int = 10) -> bool:
	# Called when a vendor "charges a verification fee"
	if gold >= cost_gold:
		add_gold(-cost_gold)
		return true
	return false

func unlock_premium_stock() -> void:
	# Call after the Debaucheryville boss dies
	if premium_unlocked:
		return
	premium_unlocked = true
	emit_signal("premium_stock_unlocked")

# --- Debug helpers (optional) ---

func debug_dump() -> void:
	print("--- Economy Dump ---")
	print("Gold:", gold)
	print("Rates:", rates)
	print("Inventory:", inventory)
	print("Premium:", premium_unlocked)
