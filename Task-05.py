# Задача 5. Одна семья

family_db = {
    ('Иванов', 'Иван'): 15,
    ('Иванова', 'Елена'): 12,
    ('Иванова', 'Татьяна'): 38,
    ('Иванов', 'Илья'): 45,
    ('Петров', 'Александр'): 46,
    ('Петров', 'Евгений'): 24,
    ('Петрова', 'Алла'): 26,
    ('Петрушина', 'Инга'): 22,
    ('Петрушин', 'Антон'): 24,
    ('Петряков', 'Семен'): 64,
    ('Осокин', 'Владимир'): 65,
    ('Осокина', 'Анастасия'): 47,
    ('Осокин', 'Анатолий'): 36,
    ('Лазарева', 'Елена'): 35,
    ('Лазарев', 'Руслан'): 38,
    ('Лазарева', 'Ольга'): 18,
    ('Федотов', 'Геннадий'): 48,
    ('Федотова', 'Ирина'): 44,
    ('Федотов', 'Иван'): 28
}


def enter_string():
    while True:
        user_string = input('Введите Фамилию Имя и возраст человека для добавления через пробел:').strip().split(' ')
        if len(user_string) != 3:
            print('Ошибка ввода. Проверьте вводимые данные. Количество элементов в строке не равно 3-м.')
        elif user_string[0].isdigit() or user_string[1].isdigit():
            print('Ошибка ввода. В фамилии и имени не должно быть цифр')
        elif user_string[2].isalpha():
            print('Ошибка ввода. Возраст не может содержать буквы.')
        else:
            return tuple(user_string[:2]), int(user_string[2])


def enter_iteration():
    while True:
        user_number = input('Введите количество добавляемых людей: ')
        if not user_number.isdigit():
            print('Ошибка ввода. Ожидается ввод только числового значения.')
        else:
            return int(user_number)


def enter_variant():
    print('В программе предустановленная база данных.\nВы можете использовать ее или создать новую. ')
    print('Чтобы создать новую базу данных - введите \'Y\' и нажмите \'Enter\'.')
    print('Чтобы продолжить использовать имеющуюся базу - нажмите \'Enter\'.')
    number = input('Ваш выбор: ')
    if number.lower() == 'y':
        return True
    else:
        return False


def check_name_surname(data_tuple, db_dict):
    if data_tuple in db_dict.keys():
        return True
    else:
        return False


def check_enter():
    while True:
        user_string = input('Введите фамилию: ')
        if user_string.isdigit():
            print('Ошибка ввода. Имя не должно содержать цифр.')
        else:
            return user_string


if enter_variant():
    family_db.clear()
    for _ in range(enter_iteration()):
        data_name_surname, age = enter_string()
        check_name_surname(data_name_surname, family_db)


surname = check_enter().capitalize()
keys_found = [surname_in_db for surname_in_db in family_db.keys() if surname_in_db[0].startswith(surname)]
if len(keys_found) > 0:
    print()
    for key in keys_found:
        print(f'{key[0]} {key[1]} {family_db[key]}')
else:
    print('Ничего не найдено.')