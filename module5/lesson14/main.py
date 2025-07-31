# 1
strings = ["apple", "kiwi", "banana", "fig"]
print(list(filter(lambda s: len(s) > 4, strings)))


# 2
students = [
    {"name": "John", "grade": 90},
    {"name": "Jane", "grade": 85},
    {"name": "Dave", "grade": 92}
]

print(max(students, key=lambda student: student["grade"]))


# 3
tuples = [(1, 5), (3, 2), (2, 8), (4, 3)]
print(sorted(tuples, key=lambda t: t[0] + t[1]))


# 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda num: num % 2 == 0, numbers)))


# 5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

persons = [Person("Mia", 29), Person("Nicolas", 31), Person("Nika", 18)]
print(sorted(persons, key=lambda person: person.age))