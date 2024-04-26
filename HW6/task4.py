'''
Создайте модуль и напишите в нём функцию, которая получает на вход дату в
 формате DD.MM.YYYY. Функция возвращает истину, если дата может существовать 
 или ложь, если такая дата невозможна. Для простоты договоримся, что год может
 быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 
года) действует Григорианский календарь.Проверку года на високосность вынести в 
отдельную защищённую функцию.

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей 
даты на проверку.'''

from datetime import datetime as dt
from calendar import isleap
from sys import argv


def check_date(date: str):
      try:
            t = dt.strptime(date, '%d.%m.%Y')
            _isleap(t.year)
            return True
      except:
          return False


def _isleap(year: int):
      print("Високосный" if isleap(year) else "Не високосный")


if __name__ == "__main__":
      if len(argv) == 2:
            print(check_date(argv[1:]))
      print(check_date(input('Введите дату чч.мм.гггг: ')))