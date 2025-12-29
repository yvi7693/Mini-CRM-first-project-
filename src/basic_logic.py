from src.auxiliary_logic import *
from src.constant import *


def add_client_people(first_name: str, last_name: str, age: int, number_phone: str, email: str):

    parameters_client = create_dictionary_people(first_name, last_name, age, number_phone, email)
    write_json_file(PATH_CLIENT, parameters_client)


def add_client_company(name: str, founded: str, number_phone: str, email: str, site: str):

    parameters_client = create_dictionary_company(name, founded, number_phone, email, site)
    write_json_file(PATH_CLIENT, parameters_client)

def watch_all_clients():
    pass

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

def validate_client_people(first_name: str, last_name: str, age: str, number_phone: str, email: str) -> bool:
    if not validate_name(first_name)  or not validate_name(last_name):
        return False

    if not validate_age(age):
        return False

    if not validate_number_phone(number_phone):
        return False

    if not validate_email(email):
        return False

    return True

def validate_client_company(name: str, founded: str, number_phone: str, email: str, site: str) -> bool:
    if not validate_name(name):
        return False

    if not validate_founded(founded):
        return False

    if not validate_number_phone(number_phone):
        return False

    if not validate_email(email):
        return False

    if validate_site(site):
        return False

    return True