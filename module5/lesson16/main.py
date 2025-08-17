import json
import csv


# 0
with open("student_list.json", "r", encoding="utf-8") as file:
    students = json.load(file)


# 1
def get_average_score(student: dict) -> float:
    subjects = student["subjects"]
    return sum(student["grades"][subject] for subject in subjects) / len(subjects)

for student_name in students:
    print(f"Средний балл для студента {student_name}: {get_average_score(students[student_name])}")


# 2
def get_best_student(students: dict) -> str:
    return max(students, key=lambda st_name: get_average_score(students[st_name]))

def get_worst_student(students: dict) -> str:
    return min(students, key=lambda st_name: get_average_score(students[st_name]))

best_student_name = get_best_student(students)
worst_student_name = get_worst_student(students)
print(f"Наилучший студент: {best_student_name} (Средний балл: {get_average_score(students[best_student_name])})")
print(f"Худший студент: {worst_student_name} (Средний балл: {get_average_score(students[worst_student_name])})")


# 3
def find_student(student_name: str) -> None:
    translation = {
        "age": "Возраст",
        "subjects": "Предметы",
        "grades": "Оценки",
    }
    if student_name in students:
        print(f"Имя: {student_name}")
        for key, value in students[student_name].items():
            print(f"{translation.get(key, key)}: {value}")
    else:
        print("Студент с таким именем не найден")

find_student("Jacob")
find_student("Nika")


# 4
sorted_students = sorted(students, key=lambda st_name: get_average_score(students[st_name]), reverse=True)
print("Сортировка студентов по среднему баллу:")
for student_name in sorted_students:
    print(f"{student_name}: {get_average_score(students[student_name])}")


# 5
def create_student_dict(student_name: str) -> dict:
    student = {
        "name": student_name
    }
    if student_name in students:
        for key, value in students[student_name].items():
            student[key] = value
    return student

students_list = [create_student_dict(student_name) for student_name in students]


# 6
headers = ["name", "age", "grade"]
data = [[student["name"], student["age"], get_average_score(student)] for student in students_list]

with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(data)