# Задача 7. Функция сортировки

def tpl_sort(user_tuple):
    for i in user_tuple:
        if isinstance(i, float):
            return user_tuple
    return tuple(sorted(user_tuple))


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))

