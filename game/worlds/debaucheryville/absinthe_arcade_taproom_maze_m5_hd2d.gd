@tool
extends TaproomMazeRoom
## Mirror maze plate M5 (section 5: four niches and the open archway onto the Taproom bar, which is
## the section's True exit; round v44 maze_section5 = approve). Camera fitted 2026-11-12 from the
## checker floor (7 tile rows + widths, residuals under 0.6 px at 1536 wide): focal 1840 px at 2752
## wide, pitch 10.85 deg, camera 4.91 tiles up, 24.59 tiles from the archway. This plate's tile is
## smaller than M1's (~0.4 m) so the niches come out the same real height (~2.6 m).


func _init() -> void:
	plate_prefix = "res://assets/worlds/debaucheryville/absinthe_arcade/interior/taproom_maze/aa_int_maze_m5_"
	focal_px = 1839.8
	pitch_deg = 10.85
	cam_height = 4.91
	cam_z = 24.59
	world_scale = 0.4
	default_spawn = "default"
	plate_id = "m5"
	floor_half_width = 9.4
	floor_depth = 16.5
	default_spawn_xz = Vector2(0, 14)
	has_exit_arch = true
	arch_half_width = 2.4
	niches = {
		"left_far": {"wall": "left", "pos": Vector3(-7.08, 0.5, 2.50), "h": 6.25},
		"left_near": {"wall": "left", "pos": Vector3(-10.45, 0.5, 7.00), "h": 6.67},
		"right_far": {"wall": "right", "pos": Vector3(7.00, 0.5, 3.05), "h": 6.20},
		"right_near": {"wall": "right", "pos": Vector3(10.52, 0.5, 7.00), "h": 6.75},
	}
