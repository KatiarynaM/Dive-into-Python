"""Возьмите задачу о банкомате из семинара 2:
Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег. 

Разбейте её на отдельные операции — функции. Дополнительно 
сохраняйте все операции поступления и снятия средств в список."""

from decimal import Decimal

MIN_SUM = 50
PROCENT_COMMISION = Decimal(0.015)
MIN_COMISSION = 30
MAX_COMISSION = 600
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX = 5_000_000
TAX_RATE = Decimal(0.1)
transes = []


def menu(balance: Decimal, count: int, is_flag: bool):
      dct = {'1': 'пополнить счет',
            '2': 'снять со счета',
            '3': 'выйти из программы'}


      for k, v in dct.items():
            if k.isdigit():
                  print(f'{k}: {v}')
            else:
                  print(v)
      if balance > LIMIT_BEFORE_TAX:
            balance *= (1 - TAX_RATE)
      choice = input('введите команду: ')
      if choice == '3':
            print(balance)
            is_flag = False
            return balance, is_flag
      elif choice == '1':
            new_balance = give_money(balance)
            transes.append(f'Внесено: {new_balance - balance}')
            print(transes)
            balance = new_balance
            count += 1
      elif choice == '2':
            new_balance = get_money(balance)
            transes.append(f'Снятo: {new_balance - balance}')
            print(transes)
            balance = new_balance
            count += 1
      else:
            print('Неверная команда')
      if count % 3 == 0:
            balance *= (1 + BONUS)
      print(f'Баланс: {balance}')
      print(transes)
      return balance, is_flag


def get_money(balance: Decimal):
      money_to_get = Decimal(input('Введите сумму снятия: '))
      procent = money_to_get * PROCENT_COMMISION

      if money_to_get % MIN_SUM == 0:
            if procent < MIN_COMISSION:
                  procent = MIN_COMISSION
            elif procent > MAX_COMISSION:
                  procent = MAX_COMISSION

            if money_to_get + procent <= balance:
                  return balance - (money_to_get + procent)
            else:
                  print('Недостаточно средств для снятия')
                  return balance
      else:
            print('Ошибка снятия денег, сумма должна быть кратна 50')
            return balance

def give_money(balance: Decimal):
      money_to_give = Decimal(input('Введите сумму пополнения: '))

      if money_to_give % MIN_SUM == 0:
            return balance + money_to_give
      else:
            print('Недостаточно средств для пополнения, сумма не кратна 50')
            return balance


if __name__ == '__main__':
      print('Добро пожаловать в программу банкомат')
      balance = 0
      count = 0
      is_flag = True
      while is_flag:
            balance, is_flag = menu(balance, count, is_flag)
