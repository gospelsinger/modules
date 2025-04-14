import csv


# Открываем файл для чтения
with open("data.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)  # Выводим каждую строку файла


# Список списков
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print(list(reader))


# Запись данных в CSV файл
data = [
    ['Имя', 'Возраст', 'Город'],
    ['Анна', '25', 'Москва'],
    ['Петр', '30', 'Санкт-Петербург'],
    ['Мария', '28', 'Киев']
]

with open("new_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)


# Запись и чтение данных с использованием словаря
data = [
    {'Имя': 'Анна', 'Возраст': '25', 'Город': 'Москва'},
    {'Имя': 'Петр', 'Возраст': '30', 'Город': 'Санкт-Петербург'},
    {'Имя': 'Мария', 'Возраст': '28', 'Город': 'Киев'}
]

# Записываем данные в CSV файл с использованием словаря
with open('data_with_headers.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = ['Имя', 'Возраст', 'Город']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Записываем заголовки
    writer.writerows(data)  # Записываем данные

# Чтение данных из CSV файла с использованием словаря
with open('data_with_headers.csv', "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Имя'], row['Возраст'], row['Город'])