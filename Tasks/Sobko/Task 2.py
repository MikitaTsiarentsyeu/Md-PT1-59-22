eq = input("Please enter your eq in format y = kx + b:\n")
error = eq.replace (' ', '').replace ('*', '')
error1 = error.replace ('y', '').replace ('=', '').replace ('+', '') 
result = error1.split('x')
x = float(input("Please enter x: "))
k = float(result[0])
b = float()
if result[1] == '':
   b = 0.0
else:
   b = float(result[1])
y = (k * x) + (b)
print(f'The value of the number k = {k},\n'
      f'The value of the number b = {b},\n'
      f'The result of solving the equation will be y = {y}')