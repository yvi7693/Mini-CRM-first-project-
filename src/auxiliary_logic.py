def validate_name(name: str) -> bool:
    if len(name) == 0:
        return False

    if name.find(" ") != -1:
        return False

    return True

def validate_age(age: str) -> bool:
    if age.isdigit() == False:
        return False

    if int(age) < 0 or int(age) > 200:
        return False

    return True

