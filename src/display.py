from src.constant import *

def show_start_information():
    print(f"{MENU_STYLE}1. {ADD_COMMAND} - Добавить нового клиента\n2. {LIST_COMMAND} - посмотреть список всех клиентов\n3. {EDIT_COMMAND} - изменить данные о клиенте\n4. {DELETE_COMMAND} - удалить клиента\n5. {SEARCH_COMMAND} - поиск клиентов\n6. {FILTER_COMMAND} - фильтры\n7. {SORT_COMMAND} - сортировка\n8. {STAT_COMMAND} - статистика")

def show_greeting():
    print(f"{INFO_STYLE}  Hello!")

def show_input_message(message: str):
    print(f'{INPUT_STYLE} {message}',end = "")

def show_error_message(message: str):
    print(f'{ERROR_STYLE} {message}')

def show_info_message(message: str):
    print(f'{INFO_STYLE} {message}')
    print()

def show_list_client(list_client: list[dict]):
    for client in list_client:

        print(f"{LIST_STYLE}id: {client['identifier_number']}")
        print(f"{LIST_STYLE}name company: {client['name']}")
        print(f"{LIST_STYLE}year founded: {client['founded']}")
        print(f"{LIST_STYLE}phone: {client['number_phone']}")
        print(f"{LIST_STYLE}email: {client['email']}")
        print(f"{LIST_STYLE}date add: {client['date_add']}")

        print(f"{INFO_STYLE}=========================")