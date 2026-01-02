import json
import os
from datetime import date

def validate_name(name: str) -> bool:
    if len(name) == 0:
        return False

    if name.find(" ") != -1:
        return False

    return True


def validate_number_phone(number_phone: str) -> bool:
    if not number_phone.isdigit():
        return False

    if len(number_phone) != 11:
        return False

    return True

def validate_email(email: str) -> bool:
    if len(email) < 6:
        return False

    if not "@" in email or not "." in email:
        return False

    return True

def validate_founded(year: str) -> bool:
    if not year.isdigit():
        return False

    if int(year) < 0 or int(year) > date.today().year:
        return False

    return True

def write_json_file(path: str, dictionary: dict):

    if not os.path.isfile(path):
        dataset = [dictionary]

    else:
        with open(path, "r", encoding="UTF-8") as file:
            dataset = json.load(file)

        dataset.append(dictionary)

    with open(path, "w", encoding="UTF-8") as file:
        json.dump(dataset, file, indent = 4)

def read_json_file(path: str) -> list[dict]:

    with open(path, "r", encoding="UTF-8") as file:
        array_dictionary = json.load(file)

    return array_dictionary


def create_dictionary(name: str, founded: str, number_phone: str, email: str) -> dict:

    dictionary = {
        "identifier_number": id(name),
        "name": name,
        "founded": founded,
        "number_phone": number_phone,
        "email": email,
        "date_add": str(date.today())
    }

    return dictionary