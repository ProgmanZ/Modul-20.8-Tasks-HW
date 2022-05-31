# Задача 9. Протокол соревнований

def enter_iteration():
    while True:
        number = input('Сколько записей вносится в протокол? ')
        if not number.isdigit():
            print('Ошибка ввода. Ожидается число.\n')
        elif int(number) < 3:
            print('Принять участие могут минимум 3 участника.\n')
        else:
            return int(number)


def check_entered_string(current_iteration):
    while True:
        user_string = input(f'{current_iteration}-я запись: ').strip().split(' ')
        if len(user_string) != 2:
            print('Неверно указаны вводные данные. Должно быть 2 значения через пробел.')
            print('Укажите по шаблону в виде: "Результат в цифрах" "Имя участника"\n')
        elif user_string[0].isalpha():
            print('Первое значение должно быть цифровым.\n')
        elif user_string[1].isdigit():
            print('Второе значение не может быть цифровым.\n')
        else:
            return user_string[1], int(user_string[0])


scores_db = dict()
result_db = dict()

for number_iteration in range(1, enter_iteration() + 1):
    string_score = check_entered_string(number_iteration)
    if string_score[0] not in scores_db.keys():
        scores_db[string_score[0]] = list()
    scores_db[string_score[0]].append(string_score[1])

for name, values in scores_db.items():
    result_db[(name, sum(values))] = max(values)

print(sorted(result_db))




