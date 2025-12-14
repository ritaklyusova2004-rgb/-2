money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0  # счетчик месяцев
budget = money_capital  # начальный бюджет

while True:
    # Хватает ли денег на этот месяц?
    if budget + salary >= spend:
        # Тратим
        budget = budget + salary - spend
        months += 1
        # Увеличиваем траты на следующий месяц
        spend = spend * (1 + increase)
    else:
        break  # деньги кончились

print("Количество месяцев, которое можно протянуть без долгов:", months)