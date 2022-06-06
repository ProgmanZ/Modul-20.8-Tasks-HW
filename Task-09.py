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


competition = list()
result_list = list()

for num_iter in range(1, enter_iteration() + 1):

    string_score = check_entered_string(num_iter)

    if string_score not in competition:
        competition.append(string_score)
    else:
        if competition[competition.index(string_score)][1] < string_score[1]:
            competition[competition.index(string_score)] = string_score
print()

for i in range(3):
    for competitor in competition:
        if competitor[1] == max(score for name, score in competition):
            print(f'{i + 1}-е место. {competitor[0]} ({competitor[1]})')
            for name in competition:
                if competitor[0] == name[0]:
                    competition.remove(name)
            break
