# Task > calculate deposite income at the end of the specified period and provide result to client

import sys
from decimal import *

greeting = print("Hello, this is the program to calculate deposit income.")
while True:
    try:
        initial_amount = Decimal(input("Please enter initial amount: "))
        annual_rate = Decimal(input("Please enter annual rate: "))
        number_of_deposite_years = Decimal(input("Please enter number of deposit years: "))
        is_monthly_capitalization = input("Would you like to calculate deposit income including monthly capitalization ('possible answers': Yes/No)?")
    except:
        print("ERROR: Entered value is not valid. Please enter correct value.")
        continue

    if is_monthly_capitalization == "Yes":
        # Algorithm
        number_of_deposite_months = int ( number_of_deposite_years * 12 )
        deposit_income_withMC = Decimal( initial_amount * ( 1 + (( annual_rate/100 ) / 12 )) ** number_of_deposite_months )
        # Result
        print("Deposit income including monthly capitalization in", number_of_deposite_years, "year(s):", deposit_income_withMC.quantize(Decimal('1.00'), ROUND_HALF_UP),"BYN")
        sys.exit()

    elif is_monthly_capitalization == "No":
        # Algorithm
        number_of_deposit_days = int( number_of_deposite_years * 365 ) # 365 is the constant for each year 
        interest_income = Decimal(( initial_amount * annual_rate * number_of_deposit_days ) / 365 ) / 100
        deposit_income = Decimal( initial_amount + interest_income )
        # Result
        print("Deposit income in", number_of_deposite_years, "year(s):", deposit_income.quantize(Decimal('1.00'), ROUND_HALF_UP),"BYN")
        sys.exit()
        
    else:
        print("ERROR: Entered value is not valid. Please enter some value specified in 'possible answers'.")