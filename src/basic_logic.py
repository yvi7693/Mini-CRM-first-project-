from src.auxiliary_logic import *
from src.constant import *


def add_client(name: str, status: str, founded: str, number_phone: str, email: str, country: str) -> None:

    client_id = revel_id(PATH_CLIENT)

    parameters_client = format_to_json(client_id, name, status, founded, number_phone, email, country)
    write_json_file(PATH_CLIENT, parameters_client)

    return None

def watch_all_clients(path: str) -> list[dict] | None:
    list_client = read_json_file(path)

    if list_client is None:
        return None

    new_list = parsing_json(list_client)

    return new_list


def edit_client(path: str, client_id: int, parameter: str, value: str) -> None:
    array_clients = read_json_file(path)

    if array_clients is None:
        return None

    array_clients[client_id][parameter] = value

    edit_file(path, array_clients)

    return None


def delete_client(client_id: int, path: str) -> None:
    array_clients = read_json_file(path)

    array_clients.pop(client_id)

    edit_file(path, array_clients)

    return None


def search_client(path: str, parameter: str, value: str) -> list[dict] | None:
    array_clients = read_json_file(path)

    searching_array = []

    for item in array_clients:
        if item[parameter] == value:
            searching_array.append(item)

    if len(searching_array) == 0:
        return None

    else:
        return searching_array

def filtering_founded_clients(period: str, value: int, path: str) -> list[dict] | None:
    array_clients = read_json_file(path)

    if array_clients is None:
        return None

    filtering_clients = []

    for client in array_clients:

        if period == "later":
            if int(client[FOUNDED_KEY]) <= value:
                filtering_clients.append(client)

        else:
            if int(client[FOUNDED_KEY]) >= value:
                filtering_clients.append(client)

    return filtering_clients



def sort_client_founded(type_sort: str, path: str) -> list[dict] | None:
    array_clients = read_json_file(path)

    if array_clients is None:
        return None

    for i in range(len(array_clients) - 1):

        is_working = True

        for j in range(len(array_clients) - 1):

            if type_sort == "a":
                if array_clients[j][FOUNDED_KEY] > array_clients[j+1][FOUNDED_KEY]:
                    array_clients[j], array_clients[j+1] = array_clients[j+1], array_clients[j]
                    is_working = False

            else:
                if array_clients[j][FOUNDED_KEY] < array_clients[j + 1][FOUNDED_KEY]:
                    array_clients[j], array_clients[j + 1] = array_clients[j + 1], array_clients[j]
                    is_working = False

        if is_working:
            break

    return array_clients


def find_statistic(path: str) -> dict | None:
    statistic = {
        "count_client_last_week": count_client_last_week(path)
    }

    if statistic["count_client_last_week"] is None:
        return None

    return statistic


def validate_client(name: str, status: str, founded: str, number_phone: str, email: str, country: str) -> bool:
    if not validate_name(name):
        return False

    if not validate_status(status):
        return False

    if not validate_founded(founded):
        return False

    if not validate_number_phone(number_phone):
        return False

    if not validate_email(email):
        return False

    if not validate_country(country):
        return False

    return True

def validate_id(client_id: str) -> bool:
    if not client_id.isdigit():
        return False

    if revel_id(PATH_CLIENT) <= int(client_id):
        return False

    return True


def validate_parameter(parameter: str) -> bool:
    if parameter == NAME_KEY:
        return True

    if parameter == STATUS_KEY:
        return True
    if parameter == FOUNDED_KEY:
        return True

    if parameter == PHONE_KEY:
        return True

    if parameter == EMAIL_KEY:
        return True

    if parameter == COUNTRY_KEY:
        return True

    return False


def validate_filtering_value(value: str) -> bool:
    if value.isdigit():
        return True

    if int(value) > 0:
        return True

    if validate_founded(value):
        return True

    return False


def overwriting_id(path: str) -> None:
    list_client = read_json_file(path)

    if list_client is None:
        return None

    for i in range(len(list_client)):
        list_client[i][ID_KEY] = i

    edit_file(path, list_client)

    return None