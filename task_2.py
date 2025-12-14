salary = 5000
spend = 6000
months = 10
increase = 0.03

# Начинаем с нулевой подушки
money_needed = 0
current_spend = spend

for month in range(months):
    # Сколько не хватает в этом месяце
    shortage = current_spend - salary
    if shortage > 0:
        money_needed += shortage

    # Увеличиваем траты на следующий месяц
    current_spend = current_spend * (1 + increase)

# Округляем до целого
money_needed = round(money_needed)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_needed)
