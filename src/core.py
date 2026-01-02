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

            show_input_message("Введите название компании >> ")
            name = input()

            show_input_message("Введите год основания компании >> ")
            founded = input()

            show_input_message("Введите номер телефона клиента начиная c '8' >> ")
            number_phone = input()

            show_input_message("Введите почту клиента >> ")
            email = input()

            if validate_client(name, founded, number_phone, email):

                add_client(name, founded, number_phone, email)
                show_info_message("Клиент успешно добавлен :)")

                continue

            else:

                show_error_message("Не корректный ввод, попробуйте еще раз!!!")

                continue


        elif command == LIST_COMMAND:
            list_client = watch_all_clients(PATH_CLIENT)

            show_info_message("ALL Clients:")
            show_list_client(list_client)

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
            show_error_message("Некорректный ввод команды!!! \n Попробуйте ещё раз.")




def stop():
    pass

