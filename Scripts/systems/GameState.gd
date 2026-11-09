var graffiti_found: Array[String] = []

func graffiti_progress() -> int:
    return graffiti_found.size()

func graffiti_complete() -> bool:
    return graffiti_found.size() >= 9