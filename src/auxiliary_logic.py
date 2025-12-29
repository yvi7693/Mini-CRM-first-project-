def validate_name(name: str) -> bool:
    if len(name) == 0:
        return False

    if name.find(" ") != -1:
        return False

    return True

def validate_age(number: str) -> bool:
    if not number.isdigit():
        return False

    if int(number) < 0 or int(number) > 200:
        return False

    return True


def validate_number_phone(number_phone: str) -> bool:
    if not number_phone.isdigit():
        return False

    if len(number_phone) != 11:
        return False

    return True


