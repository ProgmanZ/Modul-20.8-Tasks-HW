# Своя функция zip


def my_zip(input_data_one, input_data_two):
    if isinstance(input_data_one, dict) and not isinstance(input_data_two, dict):
        input_data_one = tuple(input_data_one.values())
    elif isinstance(input_data_two, dict) and not isinstance(input_data_one, dict):
        input_data_two = tuple(input_data_two.values())
    elif isinstance(input_data_one, dict) and isinstance(input_data_two, dict):
        input_data_one = tuple(input_data_one.values())
        input_data_two = tuple(input_data_two.values())
    if isinstance(input_data_one, set):
        input_data_one = tuple(input_data_one)
    if isinstance(input_data_two, set):
        input_data_two = tuple(input_data_two)
    return ((input_data_one[n], input_data_two[n]) for n in
            range(min(len(input_data_one), len(input_data_two))))


# первая часть задания

user_string = 'abcd'
user_tuple = (10, 20, 30, 40)

result = ((user_string[letter], user_tuple[letter])
          for letter in range(min(len(user_string), len(user_tuple))))

print(result)
for i in result:
    print(i)


# вторая часть задания: my_zip_func(dict1, dict2) ----> ((dict1[n], dict2[n])....)

print('\nmy_zip_func(dict1, dict2) ----> ((dict1[n], dict2[n])....)')
dict_dict = my_zip({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'y': 5}, {'e': 11, 'f': 22, 'g': 33, 'h': 44})
[print(i) for i in dict_dict]
print(dict_dict)


# вторая часть задания: my_zip_func(set, dict2) ----> ((set, dict2[n])....)

print('\nmy_zip_func(set, dict2) ----> ((set, dict2[n])....)')
set_dict = my_zip({1,2,3,4}, {'e': 11, 'f': 22, 'g': 33, 'h': 44})
[print(i) for i in set_dict]
print(set_dict)


# вторая часть задания: my_zip_func(list, set) ----> ((list[n], set)....)

print('\nmy_zip_func(list, set) ----> ((list[n], set)....)')
list_dict = my_zip(['a', 'b', 'c', 'd'], {'ee', 'ff', 'gg', 'hh', 'ii'})
[print(i) for i in list_dict]
print(list_dict)


# вторая часть задания:  my_zip_func(list, tuple) ----> ((list[n], tuple[n])....)

print('\nmy_zip_func(list, tuple) ----> ((list[n], tuple[n])....)')
list_tuple = my_zip(['a', 'b', 'c', 'd'], ('ee', 'ff', 'gg', 'hh', 'ii'))
[print(i) for i in list_tuple]
print(list_tuple)