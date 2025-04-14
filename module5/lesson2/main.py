import csv

# 1
def get_products_info(filename: str, delimiter=",") -> list[list[str]]:
    with open(filename, "r", encoding="utf-8") as f:
        products_info = [row.rstrip().split(delimiter) for row in f.readlines()]
    return products_info

def create_csv_file(filename: str, data: list[list[str]]) -> None:
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


products = get_products_info("products.txt", "\t")
create_csv_file("products.csv", products)


# 2
with open('products.csv') as csvfile:
    reader = csv.reader(csvfile)
    total = 0
    for _, count, price in reader:
        total += int(count) * int(price)
    print(f"Общая стоимость заказа: {total}")
