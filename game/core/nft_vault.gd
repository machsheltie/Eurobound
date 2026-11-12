class_name NftVault
extends RefCounted
## NFT Legacy Vault (author round v42).
## Specs: design/economy/legacy_vault_cards.md (cards), economy-wallet-crypto spec section 2 and 7c.
## - Each held card is a flag "nft_vault_<id>" on GameState, so saves need no schema change.
## - Registry: assets/data/nft/legacy_vault.json. Copy is author-only: fields stay "" where the
##   doc has none and the UI shows "—". Nothing in this class ever writes or invents copy.

const PATH := "res://assets/data/nft/legacy_vault.json"
const FLAG_PREFIX := "nft_vault_"
const COPY_FIELDS := ["tagline", "edition", "future_value", "collectors_note", "acquisition_story"]


static func _cards() -> Array:
	if not FileAccess.file_exists(PATH):
		return []
	var d = JSON.parse_string(FileAccess.get_file_as_string(PATH))
	return d.get("cards", []) if d is Dictionary else []


## Every registered card (owned or not), in registry order.
static func all_cards() -> Array:
	return _cards()


## The registry entry for an id, or {} when unknown.
static func card(id: String) -> Dictionary:
	for c in _cards():
		if c["id"] == id:
			return c
	return {}


static func owns(state, id: String) -> bool:
	return bool(state.flags.get(FLAG_PREFIX + id, false))


## Grants a card once. False for an unknown id or one already held.
static func award(state, id: String) -> bool:
	if card(id).is_empty() or owns(state, id):
		return false
	state.flags[FLAG_PREFIX + id] = true
	return true


## Owned cards in registry order.
static func list(state) -> Array:
	return _cards().filter(func(c): return owns(state, c["id"]))


## Card name with its mint number, e.g. "Sea-Monkeys (Mint #73)"; just the name if no mint.
static func title(c: Dictionary) -> String:
	var mint := String(c.get("mint", ""))
	return String(c["display_name"]) + ("" if mint == "" else " (Mint %s)" % mint)


## Text of one copy field ("" when blank). Fields are {text, locked}.
static func field_text(c: Dictionary, field: String) -> String:
	var f = c.get("copy", {}).get(field, {})
	return String(f.get("text", "")) if f is Dictionary else ""


## True when the field's text is author-locked in the doc (approval is a data edit).
static func field_locked(c: Dictionary, field: String) -> bool:
	var f = c.get("copy", {}).get(field, {})
	return f is Dictionary and bool(f.get("locked", false))


## True when the card has at least one copy field filled.
static func has_copy(c: Dictionary) -> bool:
	for f in COPY_FIELDS:
		if field_text(c, f) != "":
			return true
	return false
