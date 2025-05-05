import json
import csv


# 1
print("Task 1")
with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

print(f"Количество студентов: {len(students)}")

oldest_student = students[0]
for student in students:
    if student["возраст"] > oldest_student["возраст"]:
        oldest_student = student

print("Информация о старшем студенте:")
print(f"Имя: {oldest_student["имя"]}; возраст: {oldest_student["возраст"]}; город: {oldest_student["город"]}.")

subject = "Python"
count = sum(subject in student["предметы"] for student in students)
print(f"Количество студентов, изучающих {subject}: {count}.")


# 2
print("\nTask 2")
with open("sales.csv", "r", encoding="utf-8") as csvfile:
    data = list(csv.reader(csvfile))

total = sum(int(row[2]) for row in data[1:])
print(f"Общая сумма продаж: {total}")

products = {}
for row in data[1:]:
    if row[1] not in products:
        products[row[1]] = int(row[2])
    else:
        products[row[1]] += int(row[2])

max_sales_volume = max(products.values())
print("Продукты с самым высоким объемом продаж:")
for product in products:
    if products[product] == max_sales_volume:
        print(product)

info_per_month = {}
for row in data[1:]:
    month = row[0].rsplit("-", maxsplit=1)[0]
    if month not in info_per_month:
        info_per_month[month] = int(row[2])
    else:
        info_per_month[month] += int(row[2])

print("Сумма продаж по месяцам:")
for month, amount in info_per_month.items():
    print(f"{month}: {amount}")


# 3
print("\nTask 3")
with open("employees.json", "r", encoding="utf-8") as file:
    employees = json.load(file)

with open("performance.csv", "r", encoding="utf-8") as csvfile:
    performance = list(csv.reader(csvfile))[1:]
    performance = [[int(value) for value in employee] for employee in performance]

for employee in employees:
    employee_id = employee["id"]
    for row in performance:
        if row[0] == employee_id:
            employee['производительность'] = row[1]

print(f"Средняя производительность: {sum(row[1] for row in performance)/len(performance)}")
max_performance = max(row[1] for row in performance)
for employee in employees:
    if employee["производительность"] == max_performance:
        print(f"{employee["имя"]}, производительность: {max_performance}")