from src.basic_logic import *
from src.display import *
from src.constant import *


def start():
    show_greeting()
    main_loop()

def main_loop():
    show_start_information()
    command = input(show_input_message("Введите команду >>"))

    is_working = True
    while is_working:

        if command == ADD_COMMAND:

            client_type = input(show_input_message("Введите объект ввода: people/company >>"))

            if client_type == "people":
                first_name = input(show_input_message("Введите имя клиента >> "))
                last_name = input(show_input_message("Введите фамилию клиента >> "))
                age = input(show_input_message("Введите возвраст клиента >>"))
                number_phone = input(show_input_message("Введите номер телефона клиента начиная c '+7' >> "))
                email = input(show_input_message("Введите почту клиента >>"))

                if validate_client(first_name, last_name, age, number_phone, email) == True:

                    add_client_people(first_name, last_name, age, number_phone, email)

                else:

                    validate_client()
                    continue


            elif client_type == "company":
                name = input("Введите название компании >> ")
                founded = input("Введите год основания компании >> ")
                number_phone = input("Введите номер телефона клиента >> ")
                email = input("Введите почту клиента >> ")
                site = input("Введите сайт клиента >> ")

                add_client_company(name, founded, number_phone, email, site)

            is_working = False

        elif command == LIST_COMMAND:
            watch_all_clients()
            is_working = False

        elif command == EDIT_COMMAND:
            edit_client()
            is_working = False

        elif command == DELETE_COMMAND:
            delete_client()
            is_working = False

        elif command == SEARCH_COMMAND:
            search_client()
            is_working = False

        elif command == FILTER_COMMAND:
            filtering_clients()
            is_working = False

        elif command == SORT_COMMAND:
            sort_client()
            is_working = False

        elif command == STAT_COMMAND:
            find_statistic()
            is_working = False

        else:
            print("Некорректный ввод команды")
            command = input("Введите команду >>")



def stop():
    pass

