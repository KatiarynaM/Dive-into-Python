'''Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
 Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
 Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)'''

import random 
randintnum = random.randint(1, 1000)
print(randintnum)
effort = 10
while effort > 0:
      a = int(input(f'У Вас есть попыток {effort} угадать число от 0 до 1000:'))
      if a == randintnum:
            print(f'Ура! Вы угадали! {a} верное число.')
            break
      elif a > randintnum:
            print(f'Число {a} должно быть меньше.')
            effort -= 1
            continue
      elif a < randintnum:
            print(f'Число {a} дожно быть больше.')
            effort -= 1
            continue
else:
             print(f'Увы! Все попытки закончились!')