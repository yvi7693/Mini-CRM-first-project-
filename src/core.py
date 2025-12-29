from src.basic_logic import *
from src.display import *
from src.constant import *


def start():
    show_greeting()
    main_loop()

def main_loop():

    is_working = True
    while is_working:

        show_start_information()
        show_input_message("Введите команду >> ")
        command = input()

        if command == ADD_COMMAND:

            show_input_message("Введите объект ввода: people/company >> ")
            client_type = input()

            if client_type == "people":

                show_input_message("Введите имя клиента >> ")
                first_name = input()

                show_input_message("Введите фамилию клиента >> ")
                last_name = input()

                show_input_message("Введите возвраст клиента >> ")
                age = input()

                show_input_message("Введите номер телефона клиента начиная c '8' >> ")
                number_phone = input()

                show_input_message("Введите почту клиента >> ")
                email = input()

                if validate_client_people(first_name, last_name, age, number_phone, email):

                    add_client_people(first_name, last_name, age, number_phone, email)
                    show_statement_message("Клиент успешно добавлен :)")

                    continue

                else:

                    show_error_message("Не корректный ввод, попробуйте еще раз!!!")

                    continue


            elif client_type == "company":

                show_input_message("Введите название компании >> ")
                name = input()

                show_input_message("Введите год основания компании >> ")
                founded = input()

                show_input_message("Введите номер телефона клиента >> ")
                number_phone = input()

                show_input_message("Введите почту клиента >> ")
                email = input()

                show_input_message("Введите сайт клиента >> ")
                site = input()

                if validate_client_company(name, founded, number_phone, email, site):

                    add_client_company(name, founded, number_phone, email, site)
                    show_statement_message("Клиент успешно добавлен :)")

                    continue

                else:

                    show_error_message("Не корректный ввод, попробуйте еще раз!!!")

                    continue


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

