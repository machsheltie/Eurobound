class_name DebugCommands
extends RefCounted
## Developer console commands for LimboConsole (Eurobound-08bo). Debug builds only.
## Every command calls an EXISTING game API (GameState, GameClock, FieldStatus, SaveSystem,
## SceneRouter). None creates content or reaches anything a release player cannot. In a release
## build register() does nothing, and LimboConsole itself is switched off by
## res://addons/limbo_console.cfg (disable_in_release_build=true).
## The logic functions take the state, return the line to print, and are unit-tested.

const PARTY_TARGET := "party"
static var _registered := false


## Called once from SceneRouter.ensure_game_started. Debug builds only; safe to call repeatedly.
static func register(tree: SceneTree) -> void:
	if not OS.is_debug_build() or _registered or tree == null:
		return
	var console: Node = tree.root.get_node_or_null("LimboConsole")
	if console == null:
		return
	_registered = true
	var s := func() -> Node: return tree.root.get_node_or_null("GameState")
	var repo := func() -> Node: return tree.root.get_node_or_null("DataRepo")
	console.register_command(func(f: String) -> void: _say(console, set_flag(s.call(), f)), "set_flag", "set a flag true")
	console.register_command(func(f: String) -> void: _say(console, clear_flag(s.call(), f)), "clear_flag", "remove a flag")
	console.register_command(func() -> void: _say(console, list_flags(s.call())), "list_flags", "list every flag")
	console.register_command(func(n: int) -> void: _say(console, add_sovs(s.call(), n)), "give_sovs", "add SOVS")
	console.register_command(func(n: int) -> void: _say(console, remove_sovs(s.call(), n)), "take_sovs", "remove SOVS (refuses if short)")
	console.register_command(func(id: String, n: int = 1) -> void: _say(console, give_item(s.call(), repo.call(), id, n)), "give_item", "give an item by id")
	console.register_command(func(id: String, n: int = 1) -> void: _say(console, apply_status(s.call(), id, n)), "apply_status", "apply a status by id")
	console.register_command(func(id: String) -> void: _say(console, clear_status(s.call(), id)), "clear_status", "clear a status by id")
	console.register_command(func(h: int, m: int = 0, d: int = 0) -> void: _say(console, set_clock(s.call(), h, m, d)), "set_clock", "set the game clock: hour [minute] [day]")
	console.register_command(func() -> void: _say(console, save_now(tree)), "save_now", "save now")
	console.register_command(func(id: String, spawn: String = "") -> void: _say(console, goto_scene(tree, id, spawn)), "goto_scene", "go to a screen id from SceneRouter")


static func _say(console: Node, line: String) -> void:
	console.info(line)


static func set_flag(state, flag_name: String) -> String:
	if flag_name.is_empty():
		return "no flag name"
	state.set_flag(flag_name)
	return "flag set: %s" % flag_name


static func clear_flag(state, flag_name: String) -> String:
	if not state.flags.has(flag_name):
		return "no such flag: %s" % flag_name
	state.flags.erase(flag_name)
	return "flag cleared: %s" % flag_name


static func list_flags(state) -> String:
	var names: Array = state.flags.keys()
	if names.is_empty():
		return "no flags"
	names.sort()
	var lines: Array[String] = []
	for n in names:
		lines.append("%s = %s" % [n, state.flags[n]])
	return "%d flags\n%s" % [lines.size(), "\n".join(lines)]


static func add_sovs(state, amount: int) -> String:
	if amount <= 0:
		return "amount must be above 0"
	state.grant_sovs(amount)
	return "SOVS: %d" % state.sovs


static func remove_sovs(state, amount: int) -> String:
	if amount <= 0 or not state.spend_sovs(amount):
		return "cannot remove %d SOVS (have %d)" % [amount, state.sovs]
	return "SOVS: %d" % state.sovs


## `repo` is the DataRepo; an unknown id gives nothing (items are never made up here).
static func give_item(state, repo, item_id: String, count: int = 1) -> String:
	if count <= 0:
		return "count must be above 0"
	if repo == null:
		return "no DataRepo"
	var item: Dictionary = repo.get_item(item_id)
	if item.is_empty():
		return "unknown item id: %s" % item_id
	state.add_item(item_id, count, item.get("max_stack", null))
	return "%s x%d" % [item_id, int(state.inventory.get(item_id, 0))]


## Uses FieldStatus.apply_from_table: only statuses the status table already defines.
static func apply_status(state, status_id: String, count: int = 1) -> String:
	if not StatusTable.has_entry(status_id):
		return "unknown status id: %s" % status_id
	if not FieldStatus.apply_from_table(state, PARTY_TARGET, status_id, maxi(count, 1)):
		return "status not applied (no field duration in the table): %s" % status_id
	return "applied: %s" % status_id


static func clear_status(state, status_id: String) -> String:
	FieldStatus.remove(state, status_id)
	return "cleared: %s" % status_id


static func set_clock(state, hour: int, minute: int = 0, day: int = 0) -> String:
	if hour < 0 or hour > 23 or minute < 0 or minute > 59 or day < 0:
		return "usage: set_clock hour(0-23) [minute(0-59)] [day]"
	GameClock.set_time(state, day * GameClock.DAY + hour * 60 + minute)
	return "clock: day %d %s" % [GameClock.day(state), GameClock.watch_text(state)]


static func save_now(tree: SceneTree) -> String:
	var saver := tree.root.get_node_or_null("SaveSystem")
	if saver == null:
		return "no SaveSystem"
	return "saved" if saver.save_now("debug_console") else "save failed"


static func goto_scene(tree: SceneTree, screen_id: String, spawn_id: String = "") -> String:
	if not SceneRouter.travel(tree, screen_id, spawn_id):
		return "unknown screen id: %s" % screen_id
	return "going to %s" % screen_id
