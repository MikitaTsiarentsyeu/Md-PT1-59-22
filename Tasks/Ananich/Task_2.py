import re
equation = input("Please enter your equation in format y = kx + b:\n")
str1 = equation.replace(" ", "")
str2 = str1.replace("*", "")
fin_str = re.sub("[y|=|+]","",str2)
li = fin_str.split('x')
if li[0] == '-':
    k = -1
elif li[0] == '':
    k = 1
else:
    k = float(li[0])
if li[1] == '':
    b = 0
else:
    b = float(li[1])            
x = float(input("Please enter the x value:\n"))
fin_equation = "y={}*{}+{}".format(k, x, b)
print("Final version of equation is: " + fin_equation)
y = float(k*x+b)
print("The result is:", y)