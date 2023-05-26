# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from pprint import pprint
from collections import Counter
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = []
for student in students:
    names += [student['first_name']] #['Вася', 'Петя', 'Маша', 'Маша', 'Петя']

for key, value in (Counter(names).items()): #dict_items([('Вася', 1), ('Петя', 2), ('Маша', 2)])
    print(f'{key}: {value}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = []
for student in students:
    names += [student['first_name']] #['Вася', 'Петя', 'Маша', 'Маша', 'Оля']

n = Counter(names).most_common()[0] #('Маша', 2)
print(f'Самое частое имя среди учеников: {n[0]}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
def classs_search(school, i = 0, names = []):
    for classs in school:
        i += 1
        for student in classs:
            names += [student['first_name']]
        n = Counter(names).most_common()[0]
        print(f'Самое частое имя в классе {i}: {n[0]}')

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
classs_search(school_students)


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for classs in school:
    names = []
    for student in classs['students']:
        names += [student['first_name']]
        boy = 0
        girl = 0
        for gendr in names:
            if is_male[gendr] == True:
                boy += 1
            elif is_male[gendr] == False:
                girl += 1
    print(f'{classs["class"]}: девочки {girl}, мальчики {boy}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
for classs in school:
    gendrs = {'class': '', 'man': 0, 'woman': 0}
    gendrs['class'] = classs['class']
    for student in classs['students']:
        name = student['first_name']
        if is_male[name] == False:
            gendrs['woman'] += 1
        elif is_male[name] == True:
            gendrs['man'] += 1
    gendrs_class.append(gendrs)

print(gendrs_class) # [{'class': '2a', 'man': 0, 'woman': 2}, {'class': '3c', 'man': 2, 'woman': 0}]

i = 0
if gendrs_class[i]['man'] > gendrs_class[i+1]['man']:
    print(f'Больше всего мальчиков в классе {gendrs_class[i]["class"]}')
elif gendrs_class[i]['man'] < gendrs_class[i+1]['man']:
    print(f'Больше всего мальчиков в классе {gendrs_class[i+1]["class"]}')
if gendrs_class[i]['woman'] > gendrs_class[i+1]['woman']:
    print(f'Больше всего девочек в классе {gendrs_class[i]["class"]}')
elif gendrs_class[i]['woman'] < gendrs_class[i+1]['woman']:
    print(f'Больше всего девочек в классе {gendrs_class[i+1]["class"]}')