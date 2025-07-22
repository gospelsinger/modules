from functools import reduce


# 1
def cube(n):
    return n ** 3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubed = list(map(cube, numbers))
print(cubed)


# 2
def is_multiple_of_5(n):
    return n % 5 == 0

numbers = range(100)
print(list(filter(is_multiple_of_5, numbers)))


# 3
def is_odd(n):
    return n % 2 == 1

def multiply(x, y):
    return x * y

numbers = range(10)
odd_product = reduce(multiply, filter(is_odd, numbers))
print(odd_product)