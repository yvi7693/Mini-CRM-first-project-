import json
from src.constant import *
from datetime import date

def add_client_people(first_name: str, last_name: str, age: int, number_phone: str, email: str):
    parameters_client = {
        "identifier_number": id(first_name),
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "number_phone": number_phone,
        "email": email,
        "date_add": str(date.today())
    }

    with open(PATH_CLIENT, "w", encoding="UTF-8") as file:
        json.dump(parameters_client, file, indent = 4)

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

    with open(PATH_CLIENT, "w", encoding="UTF-8") as file:
        json.dump(parameters_client, file, indent = 4)


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