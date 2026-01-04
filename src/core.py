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
            show_input_message("Введите id клиента данные которого хотели бы отредактировать >> ")
            client_id = input()

            if not validate_id(client_id):
                show_error_message("Ввденный id не корректен")

            else:

                show_input_message("Введите название компании >> ")
                name = input()

                show_input_message("Введите год основания компании >> ")
                founded = input()

                show_input_message("Введите номер телефона клиента начиная c '8' >> ")
                number_phone = input()

                show_input_message("Введите почту клиента >> ")
                email = input()

                if validate_client(name, founded, number_phone, email):
                    edit_client(PATH_CLIENT, int(client_id), name, founded, number_phone, email)
                    show_info_message("Данные клиента успешно отредактированы :)")

                    continue

                else:

                    show_error_message("Не корректный ввод, попробуйте еще раз!!!")

                    continue

        elif command == DELETE_COMMAND:
            show_input_message("Введите id клиента которого хотели бы удалить >> ")
            client_id = input()

            if not validate_id(client_id):
                show_error_message("Ввденный id не корректен")

            else:
                delete_client(int(client_id), PATH_CLIENT)
                show_info_message("Клиент удалён")


        elif command == SEARCH_COMMAND:
            show_input_message("Введите параметр по которому хотите осуществить поиск 'name/founded/phone/email' >> ")
            parameter = input()

            if validate_parameter(parameter):
                if parameter == "name":
                    show_input_message("Введите имя компании >> ")
                    search_value = input()

                elif parameter == "founded":
                    show_input_message("Введите год основания >> ")
                    search_value = input()

                elif parameter == "phone":
                    show_input_message("Введите номер телефона >> ")
                    search_value = input()

                elif parameter == "email":
                    show_input_message("Введите адрес электронно почты >> ")
                    search_value = input()

                else:
                    show_error_message("Введен некорректный параметр!!!\nПопробуйте ещё раз.")
                    continue

                if search_client(PATH_CLIENT, parameter, search_value) is None:
                    show_error_message("Клиент по вашему запросу не найден")

                else:
                    show_info_message("Клиенты соответствующие поисковому запросу:")
                    show_list_client(search_client(PATH_CLIENT, parameter, search_value))

            else:
                show_error_message("Введен некорректный параметр!!!\nПопробуйте ещё раз.")
                continue




        elif command == FILTER_COMMAND:

            show_input_message("Введите параметр по которому необходимо провести фильтрацию year/... >> ")
            parameter = input()

            if parameter == "year":
                show_input_message("Провести фильтрацию <- later/earlier ->")
                period = input()

                if period == "later" or period == "earlier":

                    show_founded_year(read_json_file(PATH_CLIENT))
                    show_input_message("Введите год относительно которого нужно провести фильтрацию")
                    value = input()

                    if validate_filtering_value(value):

                        filtering_clients = filtering_founded_clients(period, int(value), PATH_CLIENT)
                        show_info_message("Отфильтрованный список клиентов:")
                        show_list_client(filtering_clients)

                    else:
                        show_error_message("Введен не корректный год!!! Попробуйте ещё раз.")

                else:
                    show_error_message("Введен некорректный период фильтрации!!! Попробуйте ещё раз.")
                    continue

            else:
                show_error_message("Введен некорректный параметр!!! Попробуйте ещё раз.")
                continue






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

