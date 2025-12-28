from basic_logic import *

def start():
    pass

def main_loop():
    command = input("Введите команду >>")

    if command == "1":
        add_client()

    elif command == "2":
        watch_all_clients()

    elif command == "3":
        edit_client()

    elif command == "4":
        delete_client()

    elif command == "5":
        search_client()

    elif command == "6":
        filtering_clients()

    elif command == "7":
        sort_client()

    elif command == "8":
        find_statistic()

def stop():
    pass

