# Задача 6. По парам

user_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result_tuple1 = [(user_list[i], user_list[i+1]) for i in range(0, len(user_list), 2)]

result_tuple2 = list(zip((i for i in range(0, len(user_list), 2)), (j for j in range(1, len(user_list), 2))))

