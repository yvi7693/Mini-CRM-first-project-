from src.auxiliary_logic import *
from src.constant import *


def add_client(name: str, founded: str, number_phone: str, email: str):

    client_id = revel_id(PATH_CLIENT)
    parameters_client = create_dictionary(client_id, name, founded, number_phone, email)
    write_json_file(PATH_CLIENT, parameters_client)


def watch_all_clients(path: str) -> list[dict]:
    list_client = read_json_file(path)

    return list_client

def edit_client(path: str, client_id: int, name: str, founded: str, number_phone: str, email: str):
    array_clients = read_json_file(path)

    array_clients[client_id] = create_dictionary(name, founded, number_phone, email)

    edit_file(path, array_clients)


def delete_client(client_id: int, path: str):
    array_clients = read_json_file(path)

    array_clients.pop(client_id)

    edit_file(path, array_clients)

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
            if client['founded'] <= value:
                filtering_clients.append(client)

        else:
            if client['founded'] >= value:
                filtering_clients.append(client)

    return filtering_clients



def sort_client():
    pass

def find_statistic():
    pass

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
