from src.auxiliary_logic import *
from src.constant import *


def add_client_people(first_name: str, last_name: str, age: int, number_phone: str, email: str):

    parameters_client = create_dictionary_people(first_name, last_name, age, number_phone, email)
    write_json_file(PATH_CLIENT, parameters_client)


def add_client_company(name: str, founded: int, number_phone: str, email: str, site: str):
    parameters_client = {
        "identifier_number": id(name),
        "name": name,
        "founded": founded,
        "number_phone": number_phone,
        "email": email,
        "site": site,
        "date_add": str(date.today())
    }

    with open(PATH_CLIENT, "a", encoding="UTF-8") as file:
        json.dump(parameters_client, file, indent = 4)
        file.write(",")

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
    if validate_name(first_name) == False or validate_name(last_name) == False:
        return False

    if not validate_age(age):
        return False

    if not validate_number_phone(number_phone):
        return False

    if not validate_email(email):
        return False

    return True