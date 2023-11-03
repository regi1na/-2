salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_spend = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(months):
    total_spend = total_spend + salary - spend * (1 + increase) ** i
money_capital = round(abs(total_spend), 2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
