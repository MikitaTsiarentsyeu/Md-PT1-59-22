import decimal
eq = input("Please enter your eq in format y = kx + b:\n")
effect = eq.replace (' ', '').replace ('*', '')
effect1 = effect.replace ('+', '').replace ('y', '').replace ('=', '') 
result=effect1.split('x')
h = decimal.Decimal(input("Please enter x:"))
k=decimal.Decimal(result[0])
b=decimal.Decimal(result[1])
y=decimal.Decimal(k*h+b)
print(f"The answer is:\n" ,y)