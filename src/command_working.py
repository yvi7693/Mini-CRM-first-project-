from src.display import *
from src.basic_logic import *


def processing_add_client() -> None:
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


    else:

        show_error_message("Не корректный ввод, попробуйте еще раз!!!")

    return None


def processing_list_client() -> None:
    list_client = watch_all_clients(PATH_CLIENT)

    show_info_message("ALL Clients:")
    show_list_client(list_client)

    return None


def processing_edit_client() -> None:
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


        else:

            show_error_message("Не корректный ввод, попробуйте еще раз!!!")

    return None


def processing_delete_client() -> None:

    show_input_message("Введите id клиента которого хотели бы удалить >> ")
    client_id = input()

    if not validate_id(client_id):
        show_error_message("Ввденный id не корректен")

    else:
        delete_client(int(client_id), PATH_CLIENT)
        show_info_message("Клиент удалён")

    return None



