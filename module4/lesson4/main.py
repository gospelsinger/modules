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


def check_brackets_string(bracket_s: str, brackets: dict[str, str] | None = None) -> bool:
    if brackets is None:
        brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    my_stack = Stack()
    for elem in bracket_s:
        if elem in brackets.keys():
            my_stack.push(elem)
        elif elem in brackets.values():
            if not my_stack.is_empty() and brackets[my_stack.peek()] == elem:
                my_stack.pop()
            else:
                return False
        else:
            return False
    return my_stack.is_empty()


s = input("Введите скобочную последовательность: ")
if check_brackets_string(s):
    print('Скобочная последовательность верная.')
else:
    print('Скобочная последовательность неверная.')