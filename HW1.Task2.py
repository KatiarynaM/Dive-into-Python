'''Напишите код, который запрашивает число и сообщает является ли оно 
простым или составным. Используйте правило для проверки: “Число является 
простым, если делится нацело только на единицу и на себя”. Сделайте ограничение 
на ввод отрицательных чисел и чисел больше 100 тысяч.'''


while True:
      a = int(input('Введите Ваше число от 2 до 100 000:'))
      if 1 < a <= 100000:
            break

b = int(a / 2)
while b > 1:
      if (a % b) == 0: 
            print('число является составным')
            break
      b += -1
else:
      print('число является простым')