import csv
import json


def convert_csv_to_json(data: list[list[str]], columns: list[str]) -> list[str]:
    json_objects = []
    for row in data:
        dict_data = {}
        for i, value in enumerate(row):
            dict_data[columns[i]] = value
        json_obj = json.dumps(dict_data, indent=4)
        json_objects.append(json_obj)
    return json_objects


with open("data.csv", "r", encoding="utf-8") as csvfile:
    reader = list(csv.reader(csvfile, delimiter=",", lineterminator="\n"))

json_data = convert_csv_to_json(reader[1:], reader[0])
for obj in json_data:
    print(obj)