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

for num_iter in range(1, enter_iteration() + 1):

    string_score = check_entered_string(num_iter)

    if string_score[0] not in scores_db.keys():
        scores_db[string_score[0]] = list()

    scores_db[string_score[0]].append(string_score[1])


max_score = {name: max(scores) for name, scores in scores_db.items()}
prev_score = {name: max(scores[:-1]) for name, scores in scores_db.items()}

for name, scores in max_score.items():
    if list(max_score.values()).count(scores) > 1:
        prev_score[name] += scores
    else:
        prev_score[name] = scores

count = 0
print()

for previous_score in sorted(prev_score.values(), reverse=True)[:3]:
    for name, score in prev_score.items():

        if previous_score == score:
            count += 1
            print(f'{count}-е место.\t{name}\t{max_score[name]}')

# qwerty 197128
# Alex 95715
# M 95715

# Исходный словарь, который вводится при запуске программы с последними результатами
# {
#   'Jack': 95715,
#   'qwerty': 197128,
#   'Alex': 95715,
#   'M': 95715
#   }

# Словарь, в котором у одинаковых набранных баллах к последнему результату прибавляется предыдущий,
# с прошлой игры. Получается, что Jack не может быть на 3-м месте.
# Он, суммарно, за два предыдущих матча набрал меньше очков - чем М.
# Так же он набрал суммарно за все игры меньше всех.

# Суммы очков за последнюю и предпоследнюю игры
# {
# 'Jack': 165200,
# 'qwerty': 197128,
# 'Alex': 191430,
# 'M': 179362
# }

# Полный словарь после ввода
#  {
#     'Jack': [69485, 95715],
#     'qwerty': [95715, 197128],
#     'Alex': [95715, 93289, 95715],
#     'M': [83647, 95715]
#   }