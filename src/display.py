from src.constant import *

def show_start_information() -> None:
    print(f"{MENU_STYLE}1. {ADD_COMMAND} - Добавить нового клиента\n2. {LIST_COMMAND} - посмотреть список всех клиентов\n3. {EDIT_COMMAND} - изменить данные о клиенте\n4. {DELETE_COMMAND} - удалить клиента\n5. {SEARCH_COMMAND} - поиск клиентов\n6. {FILTER_COMMAND} - фильтры\n7. {SORT_COMMAND} - сортировка\n8. {STAT_COMMAND} - статистика\n9. {EXIT_COMMAND} - завершить работу")

    return None


def show_greeting() -> None:
    print(f"{INFO_STYLE}  Hello!")

    return None

def show_input_message(message: str) -> None:
    print(f'{INPUT_STYLE} {message}',end = "")

    return None


def show_error_message(message: str) -> None:
    print(f'{ERROR_STYLE} {message}')

    return None


def show_info_message(message: str) -> None:
    print(f'{INFO_STYLE} {message}')
    print()

    return None


def show_list_client(list_client: list[dict]) -> None:
    for client in list_client:

        print(f"{LIST_STYLE}id: {client['identifier_number']}")
        print(f"{LIST_STYLE}name company: {client['name']}")
        print(f"{LIST_STYLE}year founded: {client['founded']}")
        print(f"{LIST_STYLE}phone: {client['phone']}")
        print(f"{LIST_STYLE}email: {client['email']}")
        print(f"{LIST_STYLE}date add: {client['date_add']}")

        print(f"{INFO_STYLE}=========================")

    return None


def show_founded_year(list_client: list[dict]) -> None:
    print(f"{INFO_STYLE}Founded year:")
    for client in list_client:
        print(f"{LIST_STYLE} - {client['founded']}")

    return None


def show_statistic(statistic: dict) -> None:
    print(f"{LIST_STYLE}Количество клиентов за последнюю неделю: {statistic['count_client_last_week']}")

    return None