# Задача 2. Универсальная программа 2

def is_prime(number):
    result_list = [1 if number % i != 0 else 0 for i in range(1, number + 1)]
    return True if result_list.count(0) == 2 else False


def crypto(item_data):
    if not isinstance(item_data, dict):
        result_func = [element for index, element in enumerate(item_data) if is_prime(index)]
    else:
        result_func = [element for index, element in item_data.items() if is_prime(index)]
    return result_func
