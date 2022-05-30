# Задача 8. Контакты 3

def check_entered_name_surname(data_for_check):
    for element in data_for_check:
        if element.isdigit():
            return True
    return False


def enter_name_surname():
    while True:
        client_name_surname = input('Введите имя и фамилию нового контакта (через пробел): ').strip().split(' ')
        if check_entered_name_surname(client_name_surname):
            print('В Имени или Фамилии не может быть цифр.')
            continue
        elif len(client_name_surname) != 2:
            print('Ошибка ввода. Проверьте вводимые данные.\n')
        else:
            return client_name_surname[0].capitalize(), client_name_surname[1].capitalize()


def enter_phone():
    while True:
        phone_number = input('Введите номер телефона: ')
        if not phone_number.isdigit():
            print('Ошибка ввода. Номер телефона может состоять только их цифр.')
        else:
            return int(phone_number)


def enter_variant():
    while True:
        print('Введите номер действия:')
        print(' 1. Добавить контакт')
        print(' 2. Найти человека')
        number = input()
        if number == '1':
            return True
        elif number == '2':
            return False
        else:
            print('Такого варианта не предусмотрено.\n')


def search_surname(search_name, dict_for_search):
    for element in dict_for_search.keys():
        if element[1] == search_name.capitalize():
            print('{0} {1} {2}'.format(*element, dict_for_search[element]))
            return
    print('Такой фамилии нет в телефонной книге')


phonebook_db = dict()

while True:
    if enter_variant():
        name_surname = enter_name_surname()
        if name_surname in phonebook_db.keys():
            print('Такой человек уже есть в контактах.')
            print('Текущий словарь контактов:', phonebook_db)
            continue
        phone = enter_phone()
        phonebook_db[name_surname] = phone
        print('Текущий словарь контактов:', phonebook_db)
    else:
        name_for_search = input('Введите фамилию для поиска: ')
        search_surname(name_for_search, phonebook_db)
