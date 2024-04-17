"""Напишите функцию принимающую на вход только ключевые параметры 
и возвращающую словарь, где ключ — значение переданного аргумента, 
а значение — имя аргумента. Если ключ не хешируем, используйте его 
строковое представление."""

from collections.abc import Hashable

def create_dict(**kwargs):
      result = {}
      temp = set()
      for key, value in kwargs.items():
            try:
                  temp.add(value)
            except:
                  value = str(value)
            result[value] = key
      return result



print(create_dict(a = 4, b = 7, c = [7,9]))