class_name ShopCatalog
extends RefCounted
## SOVS shops (economy Phase 1, Eurobound-it49): the Shops.json schema, its rows, and buying.
## Buying goes through GameState's one SOVS purchase path (purchase_sovs, Phase 0): select, pay,
## done (design/economy/economy_system.md §1.4, §8.4). No fee, no pending state, no wobble.
##
## Shops.json schema (res://assets/data/world_data/Shops.json):
##   {
##     "schema_version": "1.0",
##     "shops": {
##       "<shop_id, snake_case>": {
##         "display_name": "<shop name>",              required, non-empty
##         "currency": "SOVS",                         required; SOVS is the only shop currency
##                                                     (back-alley coin vendors are Phase 4)
##         "location_id": "<location id>",             optional
##         "cannot_afford_notice": "<line>",           optional; SovsShop has a plain fallback
##         "stock": [                                  required, may be empty
##           {"item_id": "<id in consumables, key_items or equipment>",
##            "price": <whole SOVS, at least 1> | null, null = pending author ruling, not sold
##            "count": <whole number, at least 1>}     optional, default 1: copies per purchase
##         ],
##         "_pending": {"<note key>": "<what waits on the author>"}   optional, ignored at run time
##       }
##     }
##   }
## Prices are whole SOVS and never below 1 SOV (currency.md, the 1-SOV floor). Row names come
## from item data, never from the shop. No stock or price is set here: shops, their stock and
## their prices come from the author.

const SHOPS_PATH := "res://assets/data/world_data/Shops.json"
const ITEM_FILES := {"consumables": "res://assets/data/items/consumables.json",
	"key_items": "res://assets/data/items/key_items.json", "equipment": "res://assets/data/items/equipment.json"}
const CURRENCY := "SOVS"
const SHOP_KEYS := ["display_name", "currency", "location_id", "cannot_afford_notice", "stock", "_pending"]
const ROW_KEYS := ["item_id", "price", "count"]

static var _snake := RegEx.create_from_string("^[a-z][a-z0-9_]*$")


static func load_doc(path: String = SHOPS_PATH) -> Dictionary:
	if not FileAccess.file_exists(path):
		push_error("ShopCatalog: missing data file: " + path)
		return {}
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(path))
	if not (parsed is Dictionary):
		push_error("ShopCatalog: invalid JSON in " + path)
		return {}
	return parsed


## Every item a shop may stock, by id, merged across the item files.
static func item_tables(files: Dictionary = ITEM_FILES) -> Dictionary:
	var out := {}
	for key: String in files:
		var path: String = files[key]
		if not FileAccess.file_exists(path):
			continue
		var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(path))
		if parsed is Dictionary and parsed.get(key) is Dictionary:
			out.merge(parsed[key])
	return out


## Schema problems in a whole Shops.json document, one message each. Empty means valid.
static func errors(doc: Dictionary, items: Dictionary) -> Array:
	var out := []
	if not (doc.get("shops") is Dictionary):
		out.append("Shops.json: missing 'shops' object")
		return out
	var shops: Dictionary = doc["shops"]
	for id: String in shops:
		out.append_array(shop_errors(id, shops[id], items))
	return out


static func shop_errors(id: String, shop: Variant, items: Dictionary) -> Array:
	var out := []
	var where := "shop '%s'" % id
	if _snake.search(id) == null:
		out.append("%s: id must be snake_case" % where)
	if not (shop is Dictionary):
		out.append("%s: must be an object" % where)
		return out
	for key: String in shop:
		if not SHOP_KEYS.has(key):
			out.append("%s: unknown key '%s'" % [where, key])
	var name: Variant = shop.get("display_name")
	if not (name is String) or String(name).strip_edges().is_empty():
		out.append("%s: display_name must be a non-empty string" % where)
	if shop.get("currency") != CURRENCY:
		out.append("%s: currency must be \"%s\"" % [where, CURRENCY])
	for key in ["location_id", "cannot_afford_notice"]:
		if shop.has(key) and not (shop[key] is String):
			out.append("%s: %s must be a string" % [where, key])
	if shop.has("_pending") and not (shop["_pending"] is Dictionary):
		out.append("%s: _pending must be an object" % where)
	if not (shop.get("stock") is Array):
		out.append("%s: stock must be an array" % where)
		return out
	var seen := {}
	var stock: Array = shop["stock"]
	for i in stock.size():
		var row: Variant = stock[i]
		var at := "%s stock[%d]" % [where, i]
		if not (row is Dictionary):
			out.append("%s: must be an object" % at)
			continue
		for key: String in row:
			if not ROW_KEYS.has(key):
				out.append("%s: unknown key '%s'" % [at, key])
		var item_id: Variant = row.get("item_id")
		if not (item_id is String) or not items.has(item_id):
			out.append("%s: item_id '%s' is not in the item data" % [at, str(item_id)])
		elif seen.has(item_id):
			out.append("%s: item_id '%s' is stocked twice" % [at, item_id])
		else:
			seen[item_id] = true
		var price: Variant = row.get("price")
		if price != null and not _whole_at_least(price, 1):
			out.append("%s: price must be whole SOVS, at least 1 SOV, or null (pending)" % at)
		if not row.has("price"):
			out.append("%s: price is required (null marks it pending)" % at)
		if row.has("count") and not _whole_at_least(row["count"], 1):
			out.append("%s: count must be a whole number, at least 1" % at)
	return out


## The rows a shop sells: priced, known items only. A null price is pending and not offered.
## Each row: {"id", "name" (item display_name), "price", "count", "max_stack" (item's, or null)}.
static func rows(shop: Dictionary, items: Dictionary) -> Array:
	var out := []
	for row: Variant in shop.get("stock", []):
		if not (row is Dictionary):
			continue
		var id := String(row.get("item_id", ""))
		var price: Variant = row.get("price")
		if not items.has(id) or price == null or not _whole_at_least(price, 1):
			continue
		var item: Dictionary = items[id]
		var max_stack: Variant = item.get("max_stack")
		out.append({
			"id": id,
			"name": String(item.get("display_name", id)),
			"price": int(price),
			"count": int(row.get("count", 1)),
			"max_stack": int(max_stack) if (max_stack is int or max_stack is float) else null,
		})
	return out


## Money as the game writes it: "1 SOV", "40 SOVS" (economy_system.md §1.3).
static func sovs_text(amount: int) -> String:
	return "1 SOV" if amount == 1 else "%d SOVS" % amount


## Buys one row. False (and nothing changes) when the wallet is short: the caller shows its
## cannot-afford notice. Otherwise pays through purchase_sovs and returns true.
static func buy(state, row: Dictionary) -> bool:
	var price := int(row.get("price", 0))
	if price < 1 or not state.can_afford(price):
		return false
	state.purchase_sovs(String(row["id"]), price, int(row.get("count", 1)), row.get("max_stack"))
	return true


static func _whole_at_least(v: Variant, minimum: int) -> bool:
	if v is int:
		return v >= minimum
	if v is float:
		return v == floorf(v) and v >= minimum
	return false
