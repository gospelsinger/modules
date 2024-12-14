class Task:
    def __init__(self, name: str):
        self.name = name


class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            raise ValueError("Incorrect type of the task.")

    def get_next_task(self) -> Task | None:
        if not self.is_empty():
            next_task, self.tasks = self.tasks[0], self.tasks[1:]
            return next_task
        return None

    def is_empty(self):
        return len(self.tasks) == 0


queue = TaskQueue()
num_of_tasks = int(input("Введите количество задач: "))

for _ in range(num_of_tasks):
    new_task = Task(input("Введите следующую задачу: "))
    queue.add_task(new_task)

print("Текущие задачи:")
while not queue.is_empty():
    next_task = queue.get_next_task()
    print(f"Следующая задача: {next_task.name}")

print(f"Список задач пуст: {queue.is_empty()}")  # Ожидаемый результат: True