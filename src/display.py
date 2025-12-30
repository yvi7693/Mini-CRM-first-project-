from src.constant import *

def show_start_information():
    print(f"{START_INFO_STYLE}1. {ADD_COMMAND} - Добавить нового клиента\n2. {LIST_COMMAND} - посмотреть список всех клиентов\n3. {EDIT_COMMAND} - изменить данные о клиенте\n4. {DELETE_COMMAND} - удалить клиента\n5. {SEARCH_COMMAND} - поиск клиентов\n6. {FILTER_COMMAND} - фильтры\n7. {SORT_COMMAND} - сортировка\n8. {STAT_COMMAND} - статистика")

def show_greeting():
    print(f"{GREETING_STYLE}  Hello!")

def show_input_message(message: str):
    print(f'{INPUT_STYLE} {message}',end = "")

def show_statement_message(message: str):
    print(f'{STATEMENT_STYLE} {message}')

def show_error_message(message: str):
    print(f'{ERROR_STYLE} {message}')