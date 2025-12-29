def validate_name(name: str) -> bool:
    if len(name) == 0:
        return False

    if name.find(" ") != -1:
        return False

    return True

