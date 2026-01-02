from src.auxiliary_logic import *
from src.constant import *


def add_client(name: str, founded: str, number_phone: str, email: str):

    parameters_client = create_dictionary(name, founded, number_phone, email)
    write_json_file(PATH_CLIENT, parameters_client)


def watch_all_clients(path: str) -> list[dict]:
    list_client = read_json_file(path)

    return list_client

def edit_client():
    pass

def delete_client():
    pass

def search_client():
    pass

def filtering_clients():
    pass

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
