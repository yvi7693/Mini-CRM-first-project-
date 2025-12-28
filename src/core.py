from src.basic_logic import *
from src.display import *


def start():
    show_start_information()
    main_loop()

def main_loop():
    command = int(input("Введите команду >>"))
    flag = True

    while flag:

        if command == "1":

            object = str(input("Введите объект ввода: people/company >>"))

            if object == "people":
                first_name = str(input("Введите имя клиента >> "))
                last_name = str(input("Введите фамилию клиента >> "))
                age = int(input("Введите возвраст клиента >>"))
                number_phone = int(input("Введите номер телефона клиента >> "))
                email = str(input("Введите почту клиента >>"))

                add_client_people(first_name, last_name, age, number_phone, email)


            elif object == "company":
                name = str(input("Введите название компании >> "))
                founded = int(input("Введите год основания компании >> "))
                number_phone = int(input("Введите номер телефона клиента >> "))
                email = str(input("Введите почту клиента >> "))
                site = str(input("Введите сайт клиента >> "))



            flag = False

        elif command == "2":
            watch_all_clients()
            flag = False

        elif command == "3":
            edit_client()
            flag = False

        elif command == "4":
            delete_client()
            flag = False

        elif command == "5":
            search_client()
            flag = False

        elif command == "6":
            filtering_clients()
            flag = False

        elif command == "7":
            sort_client()
            flag = False

        elif command == "8":
            find_statistic()
            flag = False

        else:
            print("Некорректный ввод команды")
            command = input("Введите команду >>")



def stop():
    pass

