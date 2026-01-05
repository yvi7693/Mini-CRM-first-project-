from src.basic_logic import *
from src.display import *
from src.constant import *
from src.command_working import *


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
            processing_add_client()

        elif command == LIST_COMMAND:
            processing_list_client()

        elif command == EDIT_COMMAND:
           processing_edit_client()

        elif command == DELETE_COMMAND:
            processing_delete_client()

        elif command == SEARCH_COMMAND:
            processing_search_client()

        elif command == FILTER_COMMAND:
            processing_filtering_client()

        elif command == SORT_COMMAND:
            processing_sort_client()

        elif command == STAT_COMMAND:
            processing_statistic_client()

        elif command == EXIT_COMMAND:
            stop()
            break

        else:
            show_error_message("Некорректный ввод команды!!! \n Попробуйте ещё раз.")


def stop():
    show_info_message("work has been stopped.")

