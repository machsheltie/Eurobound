extends SceneTree
## Blind critic loop capture. Windowed only (headless has no renderer).
## godot --path game --resolution 1920x1080 --script <abs>/capture.gd -- <manifest.json> <out_dir> [shot_id ...]
## Writes <out_dir>/<shot_id>.jpg (max 1280 px wide, quality 0.8). Quits when done.
const BROS := {
	"chadwick": "res://assets/characters/party/chadwick/chadwick.aseprite",
	"bradley": "res://assets/characters/party/bradley/bradley.aseprite",
	"lord_pilsner": "res://assets/characters/party/lord_pilsner/lord_pilsner.aseprite",
}
const MAX_W := 1280
const QUALITY := 0.8


func _initialize() -> void:
	_run.call_deferred()


func _run() -> void:
	var args := OS.get_cmdline_user_args()
	var manifest: Dictionary = JSON.parse_string(FileAccess.get_file_as_string(args[0]))
	var out_dir: String = args[1]
	var only: Array = args.slice(2)
	DirAccess.make_dir_recursive_absolute(out_dir)
	var hall = (load(manifest["scene"]) as PackedScene).instantiate()
	hall.spawn_player = false
	root.add_child(hall)
	for i in 24:
		await process_frame
	var ws: float = hall.WORLD_SCALE
	var cam := root.get_viewport().get_camera_3d()
	var spawned: Array = []
	var failed := 0
	for shot: Dictionary in manifest["shots"]:
		if not only.is_empty() and not only.has(shot["id"]):
			continue
		for n: Node in spawned:
			n.queue_free()
		spawned.clear()
		hall.night = shot["time"] == "night"
		for spec: Dictionary in shot["bros"]:
			var s := PartySprite3D.new()
			hall.add_child(s)
			CharacterLooks.dress(s, spec["who"], BROS[spec["who"]])
			s.facing = spec["facing"]
			s.action = spec.get("action", "idle")
			s.position = Vector3(spec["at"][0], 0, spec["at"][1]) * ws
			s.add_to_group(hall.ACTOR_GROUP)
			spawned.append(s)
		for i in 10:
			await process_frame
		for i in spawned.size():
			(spawned[i] as PartySprite3D).frame = int(shot["bros"][i].get("frame", 2))
			(spawned[i] as PartySprite3D).pause()
		for i in 6:
			await process_frame
		await RenderingServer.frame_post_draw
		var img := root.get_viewport().get_texture().get_image()
		if shot.has("crop"):
			var c: Dictionary = shot["crop"]
			var k := float(img.get_width()) / root.get_visible_rect().size.x
			var p := cam.unproject_position((spawned[int(c["on"])] as Node3D).global_position + Vector3(0, float(c.get("dy", 0.9)), 0)) * k
			var r := Rect2i(int(p.x - c["w"] * k * 0.5), int(p.y - c["h"] * k * 0.5), int(c["w"] * k), int(c["h"] * k)).intersection(Rect2i(Vector2i.ZERO, img.get_size()))
			img = img.get_region(r)
		if img.get_width() > MAX_W:
			img.resize(MAX_W, int(round(img.get_height() * MAX_W / float(img.get_width()))), Image.INTERPOLATE_LANCZOS)
		img.convert(Image.FORMAT_RGB8)
		var path: String = out_dir.path_join(shot["id"] + ".jpg")
		if img.save_jpg(path, QUALITY) != OK:
			failed += 1
		print("saved ", path, " ", img.get_size())
	quit(1 if failed > 0 else 0)
