'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
и знаменателем. Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions'''

import fractions

fract_1 = input("Введите первую дробь через /: ")
fract_2 = input("Введите вторую дробь через /: ")

print("Проверка")
print(f"{fract_1} + {fract_2} = {fractions.Fraction(fract_1) + fractions.Fraction(fract_2)}")
print(f"{fract_1} * {fract_2} = {fractions.Fraction(fract_1) * fractions.Fraction(fract_2)}")
print(" ")

def main():
    
    print(f"{fract_1} + {fract_2} = {fract_sum(fract_1, fract_2)}")
    print(f"{fract_1} * {fract_2} = {fract_milt(fract_1, fract_2)}")

    

def fract_sum(fract_1: str, fract_2: str) -> str:
    # получение числителей и знаменателей из дробей
    fract_1_part = split_fraction(fract_1)
    fract_2_part = split_fraction(fract_2)
    # ищем НОК, приводим к общему знаменателю
    fract_lcm = my_lcm(fract_1_part[1], fract_2_part[1])
    # добавочные множители для приведения к единому знаменателю
    mult_1 = int(fract_lcm / fract_1_part[1])
    mult_2 = int(fract_lcm / fract_2_part[1])
    fract_1_part = [i * mult_1 for i in fract_1_part]
    fract_2_part = [i * mult_2 for i in fract_2_part]
    # сложение дроби
    fract_1_part[0] += fract_2_part[0]

    return str(fract_1_part[0]) + "/" + str(fract_1_part[1])


# приведение дроби из строкового представления к списку чисел
# [числитель, знаменатель]
def split_fraction(fract: str) -> list:
    fraction_parts = fract.split("/")
    fraction_parts = [int(a) for a in fraction_parts]
    return fraction_parts


# произведение дробей
def fract_milt(fract_1: str, fract_2: str) -> str:
    # получение числителей и знаменателей из дробей
    fract_1_part = split_fraction(fract_1)
    fract_2_part = split_fraction(fract_2)
    # умножение дробей
    fract_1_part[0] *= fract_2_part[0]
    fract_1_part[1] *= fract_2_part[1]

    return str(fract_1_part[0]) + "/" + str(fract_1_part[1])


# Поиск НОД
def my_gcd(num_1: int, num_2: int) -> int:
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1

    while num_2:
        num_1 %= num_2
        num_1, num_2 = num_2, num_1

    return int(num_1)


# Поиск НОК
def my_lcm(num_1: int, num_2: int) -> int:
    return int(num_1 / my_gcd(num_1, num_2) * num_2)

# Старт
if __name__ == "__main__":
    main()