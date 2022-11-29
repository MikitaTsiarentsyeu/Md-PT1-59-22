import decimal

# Hello user
input_parametrs = input("Hello!\nMy name finbot.Let's calculate your profit."
                        "Provide plesase,initial amount (for example, 20000),"
                        " term in years (for example, 5)),"
                        " annual percentage (for example, 15). Example:\n20000,5,15.4\n").split(',')

# calculations
amount, date_range, fee_year = decimal.Decimal(input_parametrs[0]), \
                               decimal.Decimal(input_parametrs[1]), \
                               decimal.Decimal(input_parametrs[2])
index = 1

while decimal.Decimal(index) <= date_range:
    amount = amount * (1 + (fee_year / decimal.Decimal('100')))
    index = index + 1
    final_profit = amount

# result task
print('Final summ:', amount, '\nYour profit:', amount - decimal.Decimal(input_parametrs[0]),
      '\nInclude monthly capitalization ? Input Y/N')

# additional info
user_activity = input()

if user_activity == 'Y':
    amount = decimal.Decimal(input_parametrs[0])
    index = 1
    print('Final summ:\n')

    while decimal.Decimal(index) <= date_range * decimal.Decimal('12'):
        amount = amount * (1 + (fee_year / decimal.Decimal('100')))
        index = index + 1
    print(amount)

elif user_activity == 'N':
    print('Okay, goodbye. We are waiting for your visit again')

else:
    print("I'm sorry, I don't understand you. Goodbye")