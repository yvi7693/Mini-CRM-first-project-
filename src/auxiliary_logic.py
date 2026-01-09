import json
import os
from datetime import date, timedelta

from src.constant import ID_KEY, NAME_KEY, FOUNDED_KEY, PHONE_KEY, DATE_KEY, EMAIL_KEY, STATUS_KEY, COUNTRY_KEY, \
    WORK_STATUS, ACTIVE_STATUS, ARCHIVE_STATUS


def validate_name(name: str) -> bool:
    if len(name) == 0:
        return False

    if name.find(" ") != -1:
        return False

    return True

def validate_status(status: str) -> bool:
    if status == WORK_STATUS or status == ACTIVE_STATUS or status == ARCHIVE_STATUS:
        return True

    return False


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

def validate_country(country: str) -> bool:
    if len(country) == 0:
        return False

    return True

def write_json_file(path: str, dictionary: dict) -> None:

    if not os.path.isfile(path):
        dataset = [dictionary]

    else:
        with open(path, "r", encoding="UTF-8") as file:
            dataset = json.load(file)

        dataset.append(dictionary)

    with open(path, "w", encoding="UTF-8") as file:
        json.dump(dataset, file, indent = 4)

        return None

def read_json_file(path: str) -> list[dict] | None:

    try:
        with open(path, "r", encoding="UTF-8") as file:
            array_dictionary = json.load(file)
    except FileNotFoundError:
        return None

    else:

        if not array_dictionary:
            return None

        else:
            return array_dictionary


def edit_file(path: str, array_dictionary: list[dict]):

    with open(path, 'w', encoding="UTF-8") as file:
        json.dump(array_dictionary, file, indent=4)


def format_to_json(client_id: int, name: str, status: str, founded: str, number_phone: str, email: str, country: str) -> dict:

    dictionary = {
        ID_KEY: client_id,
        NAME_KEY: name,
        STATUS_KEY: status,
        FOUNDED_KEY: founded,
        PHONE_KEY: number_phone,
        EMAIL_KEY: email,
        COUNTRY_KEY: country,
        DATE_KEY: str(date.today())
    }

    return dictionary

def revel_id(path: str) -> int | None:

    if not os.path.exists(path):
        return 0

    client_array = read_json_file(path)

    if client_array is None:
        return 0

    client_id = len(client_array)

    return client_id

def count_client_last_week(path: str) -> int | None:
    array_clients = read_json_file(path)

    if array_clients is None:
        return None

    start_date = date.today() - timedelta(days=6)

    count = 0

    for client in array_clients:
        if parsing_date(client[DATE_KEY]) >= start_date:
            count += 1

    return count

def count_domestic_client(path: str):
    array_clients = read_json_file(path)

    if array_clients is None:
        return None

    count = 0

    for item in array_clients:
        if item[COUNTRY_KEY] == "Russia":
            count += 1

    return count


def count_foreign_client(path: str):
    array_clients = read_json_file(path)

    if array_clients is None:
        return None

    count = 0

    for item in array_clients:
        if item[COUNTRY_KEY] != "Russia":
            count += 1

    return count

def count_working_client(path):
    array_clients = read_json_file(path)

    if array_clients is None:
        return None

    count = 0

    for item in array_clients:
        if item[STATUS_KEY] == WORK_STATUS:
            count += 1

    return count

def parsing_date(data: str) -> date:
    year = int(data[0:4])
    month = int(data[5:7])
    days = int(data[8:10])

    return date(year, month, days)

def parsing_json(array: list[dict]) -> list[dict]:
    for i in range(len(array)):
        array[i] = "id: " + str(array[i][ID_KEY]) + "\n" + "name: " + array[i][NAME_KEY] + "\n" + "status: " + str(array[i][STATUS_KEY]) + "\n" + "founded: " + array[i][FOUNDED_KEY] + "\n" + "number phone: " + array[i][PHONE_KEY] + "\n" + "email: " + array[i][EMAIL_KEY] + "\n" + "country: " + str(array[i][COUNTRY_KEY]) + "\n" + "add date: " + str(array[i][DATE_KEY])

    return array






