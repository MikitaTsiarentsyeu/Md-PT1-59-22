import decimal

L = 12
D = decimal.Decimal(input('please enter the deposit amount: '))
T = decimal.Decimal(input('please enter the deposit term (years): '))
n = decimal.Decimal(input('please enter the interest rate : '))
K = input('Do you want to calculate the monthly capitalization (Yes or No)? ')

if K == 'Yes':
    print(round(D * (1+n/100/L) ** (T*12), 2))
else:    
    print(round(D * (1+n/100) ** T, 2))


