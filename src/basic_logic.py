from src.auxiliary_logic import *
from src.constant import *


def add_client(name: str, founded: str, number_phone: str, email: str) -> None:

    client_id = revel_id(PATH_CLIENT)
    parameters_client = create_dictionary(client_id, name, founded, number_phone, email)
    write_json_file(PATH_CLIENT, parameters_client)

    return None

def watch_all_clients(path: str) -> list[dict]:
    list_client = read_json_file(path)

    return list_client


def edit_client(path: str, client_id: int, name: str, founded: str, number_phone: str, email: str) -> None:
    array_clients = read_json_file(path)

    array_clients[client_id] = create_dictionary(client_id, name, founded, number_phone, email)

    edit_file(path, array_clients)

    return None


def delete_client(client_id: int, path: str) -> None:
    array_clients = read_json_file(path)

    array_clients.pop(client_id)

    edit_file(path, array_clients)

    return None


def search_client(path: str, parameter: str, search_value: str) -> list[dict] | None:
    array_clients = read_json_file(path)

    searching_array = []

    for item in array_clients:
        if item[parameter] == search_value:
            searching_array.append(item)

    if len(searching_array) != 0:
        return searching_array

    else:
        return None

def filtering_founded_clients(period: str, value: int, path: str) -> list[dict]:
    array_clients = read_json_file(path)
    filtering_clients = []

    for client in array_clients:

        if period == "later":
            if int(client['founded']) <= value:
                filtering_clients.append(client)

        else:
            if int(client['founded']) >= value:
                filtering_clients.append(client)

    return filtering_clients



def sort_client_founded(type_sort: str, path: str) -> list[dict]:
    array_clients = read_json_file(path)

    for i in range(len(array_clients) - 1):

        is_working = True

        for j in range(len(array_clients) - 1):

            if type_sort == "a":
                if array_clients[j]['founded'] > array_clients[j+1]['founded']:
                    array_clients[j], array_clients[j+1] = array_clients[j+1], array_clients[j]
                    is_working = False

            else:
                if array_clients[j]['founded'] < array_clients[j + 1]['founded']:
                    array_clients[j], array_clients[j + 1] = array_clients[j + 1], array_clients[j]
                    is_working = False

        if is_working:
            break

    return array_clients


def find_statistic(path: str) -> dict:
    statistic = {
        "count_client_last_week": count_client_last_week(path)
    }

    return statistic

def validate_client(name: str, founded: str, number_phone: str, email: str) -> bool:
    if not validate_name(name)  or not validate_name(name):
        return False

    if not validate_founded(founded):
        return False

    if not validate_number_phone(number_phone):
        return False

    if not validate_email(email):
        return False

    return True

def validate_id(client_id: str) -> bool:
    if not client_id.isdigit():
        return False

    if revel_id(PATH_CLIENT) < int(client_id):
        return False

    return True

def validate_parameter(parameter: str) -> bool:
    if parameter == "name":
        return True

    if parameter == "founded":
        return True

    if parameter == "phone":
        return True

    if parameter == "email":
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
