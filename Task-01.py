# Задача 1. Ревью кода

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

interests = {i for student_interest in students.values() for i in student_interest['interests']}
age = [len(i) for student_surname in students.values() for i in student_surname['surname']]
id = [':'.join([str(student_id), str(item['age'])]) for student_id, item in students.items()]

print(f'Список пар "ID студента — возраст": {", ".join(id)}.')
print(f'Полный список интересов всех студентов: {", ".join(interests)}.')
print(f'Общая длина всех фамилий студентов: {sum(age)}.')
