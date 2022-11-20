#Пользователь задаёт значения депозита:
#начальная сумма (например, 20000)
#срок в годах (например, 5))
#годовой процент (например, 15)
#Так же стоит предложить пользователю включить ежемесячную капитализацию. (опционально)
#Нужно вычислить сумму на счету в конце указанного срока и выдть ответ пользователю.
import decimal
dep = decimal.Decimal(input("Please enter the deposit value:"))
term = decimal.Decimal(input("Please enter the deposit term:"))
percent = decimal.Decimal(input("Please enter the percent value:"))

totalAmount=(dep*percent*term)/100+dep
totalAmount = round (totalAmount, 2)
print("Total for the entire period ", totalAmount)
