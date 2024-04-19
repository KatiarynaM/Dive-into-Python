"""Напишите функцию, которая принимает на вход строку 
- абсолютный путь до файла. Функция возвращает кортеж 
из трёх элементов: путь, имя файла, расширение файла."""


import os

def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)


link1 = r"C:\Users\Asus\Desktop\учеба\ДЗ\python\Dive into python\HW5.Task1.py"
link2 = r'https://gb.ru/lessons/436852/homework'


print(parse_path(link1))
print(parse_path(link2))

