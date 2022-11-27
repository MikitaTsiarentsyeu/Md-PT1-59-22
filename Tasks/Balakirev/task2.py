def solution(equation, x):
    for i, j in ('*', ' '), (' ', ''):
        equation = equation.replace(i, j)
    finding_var = equation.split('=')
    variables = finding_var[1].split('x')
    if variables[0] == '-':
        k = -1.0
    elif variables[0] == '':
        k = 1.0
    else:
        k = float(variables[0])
    if variables[1] == '':
        b = 0.0
    else:
        b = float(variables[1])
    y = k * x + b
    return k, b, y


equation = input('Enter your equation in format y = kx + b:')
x = float(input('Enter the x value:'))
k, b, y = solution(equation, x)
print(f'The value of the number k = {k},\n '
      f'The value of the number b = {b},\n '
      f'The result of solving the equation will be y = {y}')
