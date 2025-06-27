import itertools


# 1
numbers = [1, 2, 3, 4]
print(*itertools.combinations(numbers, 2), sep="\n")


# 2
word = "Python"
print(*itertools.permutations(word), sep="\n")

count = 0
for perm in itertools.permutations(word):
    count += 1
print(count)


# 3
'''Задача 3: Объединение списков в цикле
Даны три списка: ['a', 'b'], [1, 2, 3], ['x', 'y']. Используя itertools.cycle,
объедините их в один список в цикле, повторяя этот цикл 5 раз.'''
list1 = ["a", "b"]
list2 = [1, 2, 3]
list3 = ["x", "y"]
combined_list = list1 + list2 + list3

count = 1
result = []
for item in itertools.cycle(combined_list):
    if count > len(combined_list) * 5:
        break
    result.append(item)
    count += 1
print(result)
''' Все равно не понимаю, то ли я сделала, т.к. в задании сказано, что
1) должен быть какой-то цикл, в котором с помощью itertools.cycle данные списки объединяются в один
2) потом этот цикл должен повториться 5 раз
Не понимаю, как это можно реализовать в соответствии именно с такой формулировкой'''

# Без цикла:
# result = list(itertools.islice(itertools.cycle(combined_list), len(combined_list) * 5))
# print(result)


# 4
def generate_fibonacci():
    f1, f2 = 1, 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2

print(*itertools.islice(generate_fibonacci(), 10))
# Можно ли написать как-то бесконечный генератор чисел Фибоначчи, не используя yield?


# 5
colors = ["red", "blue"]
items = ["shirt", "shoes"]
for pair in itertools.product(colors, items):
    print(" ".join(pair))