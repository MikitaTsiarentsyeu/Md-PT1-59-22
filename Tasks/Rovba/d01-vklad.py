# Пользователь задаёт значения депозита:
# - начальная сумма
# - срок в годах
# - годовой процент
# Нужно вычислить сумму на счсету в конце указанного срока и выдать ответ пользователю.


deposit = int(input("Input deposit amount: "))
n = int(input("Input number of years: "))
k = int(input("Input deposit interest(%): "))

deposit = round(deposit * (1 + k/100)**n, 2)

print("Grand total:", deposit)
