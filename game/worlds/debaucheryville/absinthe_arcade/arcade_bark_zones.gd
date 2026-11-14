class_name ArcadeBarkZones
extends Node3D
## One-shot proximity barks for the Arcade's ambient groups (final.md section 3). Each zone is a
## group's spawn node; stepping inside the radius fires the group's next line once, and the zone
## re-arms only after the leader walks away. No prompts, no state, no choices.

signal barked(group: String, node_id: String, line: String)

const RADIUS_M := 1.6
const SHOW_S := 4.0

var zones: Array = []  # [{group, node_id, pos: Vector3 (world), inside: bool}]
var bark: Label3D
var _cursors: Dictionary = {}
var _show_left := 0.0


func add_zone(group: String, node_id: String, world_pos: Vector3) -> void:
	zones.append({"group": group, "node_id": node_id, "pos": world_pos, "inside": false})


func _ready() -> void:
	bark = Label3D.new()
	bark.name = "bark"
	bark.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	bark.no_depth_test = true
	bark.font_size = 36
	bark.outline_size = 10
	bark.pixel_size = 0.004
	bark.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	bark.width = 520.0
	bark.modulate = Color(0.95, 0.95, 0.85)
	bark.visible = false
	add_child(bark)


func _process(delta: float) -> void:
	var leader: Node3D = null
	for n in get_tree().get_nodes_in_group("player"):
		if n is Node3D and get_parent() != null and get_parent().is_ancestor_of(n):
			leader = n
			break
	tick(delta, leader.global_position if leader != null else Vector3.INF)


## Advances the bark timer and fires any zone the leader just entered. Returns the line fired, "" if none.
func tick(delta: float, leader_pos: Vector3) -> String:
	if _show_left > 0.0:
		_show_left -= delta
		if _show_left <= 0.0 and bark != null:
			bark.visible = false
	var fired := ""
	for z: Dictionary in zones:
		var flat := Vector2(leader_pos.x - z["pos"].x, leader_pos.z - z["pos"].z)
		var near := leader_pos != Vector3.INF and flat.length() <= RADIUS_M
		if near and not z["inside"] and fired.is_empty() and _show_left <= 0.0:
			z["inside"] = true
			fired = ArcadeHallLines.next_bark(z["group"], _cursors)
			if fired.is_empty():
				continue
			if bark != null:
				bark.text = fired
				bark.global_position = z["pos"] + Vector3(0, 2.3, 0)
				bark.visible = true
			_show_left = SHOW_S
			barked.emit(z["group"], z["node_id"], fired)
		elif not near:
			z["inside"] = false
	return fired
