#Пользователь вводит уравнение вида y = kx + b (за одну операцию input)
#Нужно определить значения k и b, учесть при этом пограничные случаи, например наличие лишних пробелов и разную длину чисел,
#запросить у пользователя значение x и вычислить значение y, выдать его в качестве ответа.
#"y = kx + b"
#"y = 2x + 3"
#"y = -200.4x - 555.55"
#"y = 5x"
#"y = -x + 43"
#"y = -3x - 122"
#"y = 3*x + 42" # задание со звёздочкой

import decimal

str1 = input("Please enter your eq in format y = kx + b:\n")
x = decimal.Decimal(input("Please enter the x value:\n"))
str1 = str1.replace(" ", "").replace("y", "").replace("=", "").replace("x", "")
str1 = str1.split("+")
k = str1[0]
b = str1[1]
#"y = kx + b"
if k =="k" and b =="b":   
    print("y = kx + b")
#"y = -x + 43"
if k=="-":
    k = -1
    y = decimal.Decimal(k)*x+decimal.Decimal(b)
    print("y= ", y)
#"y = 5x"
if b=="":
    y = decimal.Decimal(k)*x
    print("y= ", y)
#other cases
y = decimal.Decimal(k)*x+decimal.Decimal(b)
print("y= ", y) 