import decimal
eq = input('Please enter your equation in the format y = kx + b: \n')
x = decimal.Decimal(input("Please enter the value x: \n"))
error1 = eq.replace(" ","").replace("*","").replace("=","").replace("y","").replace("+","")
error2 = error1.split("x")
k = decimal.Decimal(error2[0])
b = decimal.Decimal()
if error2[1] == '':
   b = 0.0
else:
   b = decimal.Decimal(error2[1])
y=(k*x)+b

print(f'The value of the number k = {k},\n'
      f'The value of the number b = {b},\n'
      f'The result of solving the equation will be y = {y}')


