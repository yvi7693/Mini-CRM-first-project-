from basic_logic import *

def start():
    pass

def main_loop():
    command = input("Введите команду >>")
    flag = True

    while flag:

        if command == "1":
            add_client()
            flag = False

        elif command == "2":
            watch_all_clients()
            flag = False

        elif command == "3":
            edit_client()
            flag = False

        elif command == "4":
            delete_client()
            flag = False

        elif command == "5":
            search_client()
            flag = False

        elif command == "6":
            filtering_clients()
            flag = False

        elif command == "7":
            sort_client()
            flag = False

        elif command == "8":
            find_statistic()
            flag = False

        else:
            print("Некорректный ввод команды")
            command = input("Введите команду >>")



def stop():
    pass

