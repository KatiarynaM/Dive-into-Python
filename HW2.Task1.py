"""Напишите программу, которая получает целое число и возвращает его 
шестнадцатеричное строковое представление. Функцию hex используйте для 
проверки своего результата."""

BASE = 16

num = int(input('Введите число:  '))
hex_digits = '0123456789ABCDEF'
result = ''
while num > 0:
      remainder = num % BASE
      hex_digit = hex_digits[remainder]
      result = hex_digit + result
      num  //= BASE

print(result)
