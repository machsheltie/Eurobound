class_name DialogueRunner
## Pure dialogue-tree traversal — no UI, no autoload access, fully testable.
## Understands the fields the slice needs (text/speaker/options/leads_to/
## requires.item/sets_flags) and ignores the rest of the authored schema.

var collected_flags: Array = []
var current_key: String = ""

var _tree: Dictionary

func _init(tree: Dictionary) -> void:
	_tree = tree

func start(node_key: String = "default_greeting") -> Dictionary:
	collected_flags = []
	return _enter(node_key)

func available_options(inventory: Dictionary) -> Array:
	var node: Dictionary = _tree.get(current_key, {})
	var visible: Array = []
	for option in node.get("options", []):
		var req: Variant = option.get("requires")
		if req is Dictionary and req.has("item"):
			if int(inventory.get(req["item"], 0)) > 0:
				visible.append(option)
		else:
			visible.append(option)
	return visible

func choose(option: Dictionary) -> Dictionary:
	for flag in option.get("sets_flags", []):
		collected_flags.append(flag)
	var next: Variant = option.get("leads_to", "")
	if next == null or String(next).is_empty():
		current_key = ""
		return {}
	return _enter(String(next))

func _enter(key: String) -> Dictionary:
	if not _tree.has(key):
		push_error("DialogueRunner: unknown dialogue node '%s'" % key)
		current_key = ""
		return {}
	current_key = key
	var node: Dictionary = _tree[key]
	for flag in node.get("sets_flags", []):
		collected_flags.append(flag)
	return node
