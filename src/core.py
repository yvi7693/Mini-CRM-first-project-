from src.basic_logic import *
from src.display import *


def start():
    show_greeting()
    main_loop()

def main_loop():
    show_start_information()
    command = input(show_input_message("Введите команду >>"))

    flag = True
    while flag:

        if command == "1":

            object = input(show_input_message("Введите объект ввода: people/company >>"))

            if object == "people":
                first_name = input(show_input_message("Введите имя клиента >> "))
                last_name = input(show_input_message("Введите фамилию клиента >> "))

                age = input(show_input_message("Введите возвраст клиента >>"))

                while age < 0:
                    print("Некорректный возраст!!!")
                    age = input(show_input_message("Введите возвраст клиента >>"))

                number_phone = input(show_input_message("Введите номер телефона клиента начиная c '+7' >> "))

                while len(number_phone) != 12 or number_phone[0:2] != "+7":
                    print("Не корректный номер телефона !!!")
                    number_phone = input(show_input_message("Введите номер телефона клиента начиная c '+7' >> "))

                email = input(show_input_message("Введите почту клиента >>"))

                add_client_people(first_name, last_name, age, number_phone, email)


            elif object == "company":
                name = input("Введите название компании >> ")
                founded = input("Введите год основания компании >> ")
                number_phone = input("Введите номер телефона клиента >> ")
                email = input("Введите почту клиента >> ")
                site = input("Введите сайт клиента >> ")

                add_client_company(name, founded, number_phone, email, site)

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

