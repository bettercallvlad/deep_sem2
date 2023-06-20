# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10%
# перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

MODES = """Действия:
пополнение - 1
снятие - 2
выйти - 3
Выберите действие: """

LUXURY_LIMIT = 5_000_000
TAX_LUXURY = 0.9
TAX_OUTCOME = 0.015
MAX_TAX_OUT = 600
MIN_TAX_OUT = 30

MONEY_DIV = 50
BONUS_FOR_OPERATION = 1.03
OPERATIONS_FOR_BONUS = 3

balance = 0
operations_count = 0

while True:
    choose = input(f"{MODES}")

    if balance >= LUXURY_LIMIT:
        balance *= TAX_LUXURY
        print('Раскулачивание')
    if operations_count % OPERATIONS_FOR_BONUS == 0:
        balance *= BONUS_FOR_OPERATION
        print('Бонус за 3 операции')

    if choose == '1':
        income = int(input())
        if income % MONEY_DIV == 0:
            balance += income
        else:
            print('incorrect summ')
        operations_count += 1

    elif choose == '2':
        outcome = int(input())
        if outcome % MONEY_DIV == 0:
            comission = balance * TAX_OUTCOME
            if comission >= MAX_TAX_OUT:
                comission = MAX_TAX_OUT
            elif comission <= MIN_TAX_OUT:
                comission = MIN_TAX_OUT
            balance -= comission
            balance -= outcome
        else:
            print('incorrect summ')
        operations_count += 1

    elif choose == '3':
        break

    else:
        print(f'Incorrect')

    print(f'current balance: {balance}')
