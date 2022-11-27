"""
Пользователь вводит уравнение вида y = kx + b (за одну операцию input)
Нужно определить значения k и b, учесть при этом пограничные случаи,
например наличие лишних пробелов и разную длину чисел,
запросить у пользователя значение x и вычислить значение y,
выдать его в качестве ответа.
"""
import decimal

eq = input("Please enter your eq in format y = kx + b:\n")

eq = eq.replace(' ','') 
eq = eq.replace('*','')

k_end = eq.find('x')
k = eq[2:k_end]

if k == '' or k == '+':
    k = 1
elif k == '-':
    k = -1
else:
    k = decimal.Decimal(k)

if eq[-1] == 'x':
    b = 0
else:
    b = eq[k_end+1:]
    b = decimal.Decimal(b)

x = input("Please enter the x value:\n")
x = decimal.Decimal(x)
print(f"The answer is {x*k + b}")
