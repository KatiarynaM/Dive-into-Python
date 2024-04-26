'''Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке
терминала.Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры 
используйте генераторное выражение.'''

from random import randint
from sys import argv

def guess_number(lower_limit=0, upper_limit=100, count=10):
      n = randint(lower_limit, upper_limit)
      i = 1
      print(f"Компьютер загадал число. Отгадайте его. У вас {count} попыток")
      while i <= count:
            u = int(input(str(i) + '-я попытка: '))
            if u > n:
                  print('Меньше')
            elif u < n:
                  print('Больше')
            else:
                  print('Вы угадали с %d-й попытки' % i)
                  break
            i += 1
      else:
            print(f'Вы исчерпали {count} попыток. Было загадано', n)

if __name__=='__main__':
      print(argv)
      m = len(argv)
      guess_number(*map(int, argv[1:]))
