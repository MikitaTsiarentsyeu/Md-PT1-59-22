
import decimal


eq = (input("Please enter your eq in format y = kx + b:\n"))
eq = eq.replace (' ', '').replace ('*', '')
eq = eq.replace ('y', '').replace ('=', '').replace ('+', '') 
eq = eq.split('x')
x = decimal.Decimal(input("Please enter x: "))

if eq[0] == '-':
    k = -1
else:
    k = decimal.Decimal(eq[0])

if eq[1] == '':
   b = 0
else:
   b = decimal.Decimal(eq[1])
y = (k * x) + (b)
print(f'The value of the number k = {k},\n'
      f'The value of the number b = {b},\n'
      f'The result of solving the equation will be y = {y}')
