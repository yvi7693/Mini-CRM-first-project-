from src.constant import *

def show_start_information() -> None:
    print(f"{MENU_STYLE}1. {ADD_COMMAND} - Добавить нового клиента\n2. {LIST_COMMAND} - посмотреть список всех клиентов\n3. {EDIT_COMMAND} - изменить данные о клиенте\n4. {DELETE_COMMAND} - удалить клиента\n5. {SEARCH_COMMAND} - поиск клиентов\n6. {FILTER_COMMAND} - фильтры\n7. {SORT_COMMAND} - сортировка\n8. {STAT_COMMAND} - статистика\n9. {EXPORT_COMMAND} - экспортировать файл с клиентами\n10. {EXIT_COMMAND} - завершить работу")

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

        print(f"{LIST_STYLE}{client}")
        print(f"{INFO_STYLE}=========================")

    return None


def show_founded_year(list_founded: list[dict]) -> None:
    print(f"{INFO_STYLE}Founded year:")
    for client in list_founded:
        print(f"{LIST_STYLE} - {client}")

    return None


def show_statistic(list_statistic: str) -> None:
    print(f"{LIST_STYLE}{list_statistic}")

    print(f"{INFO_STYLE}===============================")

    return None