@tool
extends TaproomMazeRoom
## Mirror maze plate M1 (sections 1-4; approved art v2 night, round v43). One-point camera fitted
## 2026-11-12 from the checker floor (8 tile rows + tile widths at three heights, residuals under
## 1.3 px at 1536 wide): focal 2697 px at 2752 wide, pitch 17.97 deg, camera 6.74 tiles up, 21.54
## tiles from the back wall. A tile is ~0.6 m (the 4.0-tile niche opening ~ 2.4 m). Niche positions
## were measured from the plate in px and unprojected onto the wall planes; the far side niches sit
## closer to the centre than the near ones (the painted walls converge a little).


func _init() -> void:
	plate_prefix = "res://assets/worlds/debaucheryville/absinthe_arcade/interior/taproom_maze/aa_int_maze_m1_"
	focal_px = 2696.9
	pitch_deg = 17.97
	cam_height = 6.74
	cam_z = 21.54
	world_scale = 0.6
	default_spawn = "default"
	plate_id = "m1"
	floor_half_width = 6.9
	floor_depth = 11.5
	default_spawn_xz = Vector2(0, 10)
	niches = {
		"back_l": {"wall": "back", "pos": Vector3(-2.50, 0.53, 0.0), "h": 4.01},
		"back_r": {"wall": "back", "pos": Vector3(2.52, 0.53, 0.0), "h": 4.01},
		"left_far": {"wall": "left", "pos": Vector3(-6.81, 0.45, 2.29), "h": 3.97},
		"left_near": {"wall": "left", "pos": Vector3(-7.35, 0.45, 5.49), "h": 4.61},
		"right_far": {"wall": "right", "pos": Vector3(6.81, 0.45, 2.29), "h": 3.97},
		"right_near": {"wall": "right", "pos": Vector3(7.39, 0.45, 5.49), "h": 4.61},
	}
