extends LocationBase
## The vertical slice's one location. Vlad guards the Absinthe Arcade
## entrance; one Feral Segway Tourist roams the plaza.

func _ready() -> void:
	location_id = "debaucheryville_clocktower_plaza"
	spawn_point = Vector2(480, 500)
	super._ready()
	spawn_npc("vlad_validator", Vector2(480, 140))
	spawn_enemy("feral_segway_tourist", Vector2(240, 320))
