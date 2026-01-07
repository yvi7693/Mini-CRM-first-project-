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
    if list_client is None:
        show_error_message("Нет клиентов!!! Чтобы просмотреть список, для начала добавьте своего первого клиента.")

    else:

        show_info_message("ALL Clients:")
        show_list_client(list_client)

    return None


def processing_edit_client() -> None:
    processing_list_client()
    show_input_message("Введите id клиента данные которого хотели бы отредактировать >> ")
    client_id = input()

    if not validate_id(client_id):
        show_error_message("Ввденный id не корректен")

    else:

        show_input_message("Введите параметр который хотите изменить 'name/founded/phone/email' >> ")
        parameter = input()

        validating = True

        if parameter == "name":
            show_input_message("Введите название компании >> ")
            edit_value = input()

            if not validate_name(edit_value):
                validating = False


        elif parameter == "founded":
            show_input_message("Введите год основания компании >> ")
            edit_value = input()

            if not validate_founded(edit_value):
                validating = False

        elif parameter == "phone":
            show_input_message("Введите номер телефона клиента >> ")
            edit_value = input()

            if not validate_number_phone(edit_value):
                validating = False

        elif parameter == "email":
            show_input_message("Введите электронную почту клиента >> ")
            edit_value = input()

            if not validate_email(edit_value):
                validating = False

        else:
            show_error_message("Введен некорректный параметр!!!\nПопробуйте ещё раз.")

        if validating:
            edit_client(PATH_CLIENT, int(client_id), parameter, edit_value)
            show_info_message("Данные клиента успешно отредактированы :)")


        else:
            show_error_message("Не корректный ввод, попробуйте еще раз!!!")

    return None


def processing_delete_client() -> None:
    processing_list_client()

    show_input_message("Введите id клиента которого хотели бы удалить >> ")
    client_id = input()

    if not validate_id(client_id):
        show_error_message("Введенный id не корректен")

    else:
        show_input_message("Вы уверены что хотите удалить клинта из списка y/n >> ")
        permission = input()
        if permission == YES:
            delete_client(int(client_id), PATH_CLIENT)
            show_info_message("Клиент удалён")

        else:
            show_error_message("Удаление клиента отменено.")

    return None


def processing_search_client() -> None:

    show_input_message("Введите параметр по которому хотите осуществить поиск 'name/founded/phone/email' >> ")
    parameter = input()

    if validate_parameter(parameter):
        if parameter == NAME_KEY:
            show_input_message("Введите имя компании >> ")
            search_value = input()

        elif parameter == FOUNDED_KEY:
            show_input_message("Введите год основания >> ")
            search_value = input()

        elif parameter == PHONE_KEY:
            show_input_message("Введите номер телефона >> ")
            search_value = input()

        elif parameter == EMAIL_KEY:
            show_input_message("Введите адрес электронно почты >> ")
            search_value = input()

        else:
            show_error_message("Введен некорректный параметр!!!\nПопробуйте ещё раз.")


        if search_client(PATH_CLIENT, parameter, search_value) is None:
            show_error_message("Клиент по вашему запросу не найден")

        else:
            show_info_message("Клиенты соответствующие поисковому запросу:")
            show_list_client(search_client(PATH_CLIENT, parameter, search_value))
    else:
        show_error_message("Введен некорректный параметр!!!\nПопробуйте ещё раз.")

    return None


def processing_filtering_client() -> None:
    show_input_message("Введите параметр по которому необходимо провести фильтрацию year/... >> ")
    parameter = input()

    if parameter == YEAR_PROCESSING:
        show_input_message("Провести фильтрацию <- later/earlier -> >>")
        period = input()

        if period == LATER_FILTER or period == EARLIER_FILTER:

            show_founded_year(read_json_file(PATH_CLIENT))
            show_input_message("Введите год относительно которого нужно провести фильтрацию >> ")
            value = input()

            if validate_filtering_value(value):

                filtering_clients = filtering_founded_clients(period, int(value), PATH_CLIENT)
                show_info_message("Отфильтрованный список клиентов:")
                show_list_client(filtering_clients)

            else:
                show_error_message("Введен не корректный год!!! Попробуйте ещё раз.")

        else:
            show_error_message("Введен некорректный период фильтрации!!! Попробуйте ещё раз.")

    else:
        show_error_message("Введен некорректный параметр!!! Попробуйте ещё раз.")

    return None


def processing_sort_client() -> None:

    show_input_message("Введите параметр по которому хотели бы провести сортировку year/... >> ")
    parameter = input()

    if parameter == YEAR_PROCESSING:

        show_input_message("Вид сортировки ascending - a / descending - d >> ")
        type_sort = input()
        if type_sort == TYPE_SORT_A or type_sort == TYPE_SORT_D:

            sorted_clients = sort_client_founded(type_sort, PATH_CLIENT)
            show_info_message("Отсортированный список клиентов:")
            show_list_client(sorted_clients)

        else:
            show_error_message("Введён некорректный тип сортировки!!! Попробуйте ещё раз.")

    else:
        show_error_message("Введен некорректный параметр!!! Попробуйте ещё раз.")

    return None


def processing_statistic_client() -> None:

    statistic = find_statistic(PATH_CLIENT)
    show_info_message("Статистика по базе клиентов: ")
    show_statistic(statistic)

    return None

