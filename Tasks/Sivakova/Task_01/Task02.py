import decimal
import time
import math

formula = input("Hello there! I'm gonna help you with conculation! Please. enter the formula in format: 'y=kx+b': \n" )
new_formula = formula.replace(" ", "") 
withone = new_formula.replace ('=x', '=1*x')
withoutsymbol = withone.replace ('*', '')

print("Ok! Hope follow the formula and now we have your values!" )


x= decimal.Decimal(input("Please enter x velue: "))

    
withoneandx= withone.replace("x", str(x))
all= withoneandx.replace("x", str(x))
withouty = all.replace("y=", "")
withoutplus = withouty.replace("+", " ")
withoutany = withoutplus.replace("*", " ")
final = withoutany.split(" ")

k = decimal.Decimal(final[0])
x = decimal.Decimal(final[1])
b = decimal.Decimal(final[2])
view = "y={}*{}+{}".format(k, x, b)
print("Great! Final version of formula is: " + view)
print("Let's conculate...")
time.sleep(2)


final_f = decimal. Decimal((k*x)+b).__round__(2)


print ("The result is: " + str(final_f))
print("Have a good day!:)")




