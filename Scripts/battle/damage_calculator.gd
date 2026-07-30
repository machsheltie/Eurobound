class_name DamageCalculator
## Pure damage math. RNG is injected so tests are deterministic.
## Formula (slice-simple, tune later): offense*2 − defense, ±2 spread,
## floor 1; crit chance = luck%, crit doubles.

static func compute(attacker: Dictionary, defender: Dictionary, rng: RandomNumberGenerator, multiplier: float = 1.0) -> Dictionary:
	var base := int(attacker.get("offense", 1)) * 2 - int(defender.get("defense", 0))
	base = maxi(1, base)
	var damage := maxi(1, int(round(base * multiplier)) + rng.randi_range(-2, 2))
	var crit := rng.randf() < float(attacker.get("luck", 0)) * 0.01
	if crit:
		damage *= 2
	return {"damage": damage, "crit": crit}
