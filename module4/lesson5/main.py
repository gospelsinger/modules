class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def size(self):
        return len(self.items)


def calculate_rpn(elements: list[str]) -> int|float:
    operands = Stack()
    for elem in elements:
        if elem not in "+-*/^":
            elem = int(elem) if "." not in elem else float(elem)
            operands.push(elem)
        else:
            b, a = operands.pop(), operands.pop()
            expression = f"{a}{elem}{b}"
            for i, j in ("^", "**"), (":", "/"):
                expression = expression.replace(i, j)
            operands.push(eval(expression))
    return operands.pop()


elems = input('Введите выражение в виде обратной польской записи: ').split()
print(calculate_rpn(elems))