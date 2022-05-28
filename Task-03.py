# Задача 3. Функция

def slicer(user_tuple, element):
    user_tuple = list(user_tuple)
    del(user_tuple[:user_tuple.index(element)+1])
    user_tuple = user_tuple[:user_tuple.index(element)+1]
    user_tuple.insert(0, element)

    return tuple(user_tuple)


# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
