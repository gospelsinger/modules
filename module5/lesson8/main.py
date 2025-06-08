from collections import Counter, namedtuple, defaultdict, deque
from random import randint, choice


# 1
random_nums = [randint(1, 20) for _ in range(200)]
counter = Counter(random_nums)
most_common = counter.most_common(3)

for num, count in most_common:
    print(f"Число {num} встретилось {count} раз")


# 2
Book = namedtuple("Book", ["title", "author", "genre"])

book1 = Book(title="Медвежий угол", author="Фредрик Бакман", genre="художественная литература")
book2 = Book(title="Звездная бабочка", author="Бернар Вербер", genre="фантастика")

for book in (book1,book2):
    print(f"{book.author}, {book.title}, жанр: {book.genre}")


# 3
dict_keys = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]

my_dict = defaultdict(list)
for _ in range(50):
    my_dict[choice(dict_keys)].append(randint(1, 1000))

print(my_dict)


# 4
d = deque(["apple", "banana", "orange"])
print(d)
d.appendleft("peach")
print(d)
d.append("lemon")
print(d)
d.appendleft("kiwi")
print(d)
d.popleft()
print(d)
d.pop()
print(d)


# 5
def enqueue(queue, element):
    queue.append(element)

def dequeue(queue):
    if queue:
        return queue.popleft()
    else:
        print("Очередь пуста.")
        return None

queue = deque()
print("Добавляю первые четыре элемента в очередь")
enqueue(queue, 1)
enqueue(queue, 2)
enqueue(queue, 3)
enqueue(queue, 4)
print(queue)

print(f"Извлекаю первый элемент: {dequeue(queue)}")
print(f"Извлекаю второй элемент: {dequeue(queue)}")
print(queue)

print("Добавляю еще два элемента в очередь")
enqueue(queue, 5)
enqueue(queue, 6)
print(f"Извлекаю третий элемент: {dequeue(queue)}")
print(queue)