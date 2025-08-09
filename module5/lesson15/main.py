# 1
students_dict = {
    'Саша': 27,
    'Кирилл': 52,
    'Маша': 14,
    'Петя': 36,
    'Оля': 43,
}
print(sorted(students_dict, key=lambda name: students_dict[name]))


# 2
data = [
    (82, 191),
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184)
]
sorted_data = sorted(
    data,
    key=lambda wh: wh[0] / ((wh[1] / 100) ** 2)
)
print(sorted_data)


# 3
students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]
print(min(students_list, key=lambda student: student["age"]))