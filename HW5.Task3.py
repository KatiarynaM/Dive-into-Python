"""Создайте функцию генератор чисел Фибоначчи"""

def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


k = int(input('Введите число k: '))
print(list(fib(k)))

