from decimal import Decimal


def deposit(money, time, percent):
    capital = input('Include monthly capitalization in the terms of the contract?(Yes or No)')
    if capital.lower() == 'yes':
        return money * (1 + (percent/100)/12) ** (time*12)
    else:
        return ((money * percent * time) / 100) + money


money = int(input('Enter the initial deposit amount in rubles'))
time = int(input('Enter term of deposit in years'))
percent = int(input('Enter the annual interest on the deposit'))
final_amount = Decimal(str(deposit(money, time, percent)))
print(final_amount.quantize(Decimal('1.00')))
