from decimal import Decimal 

eq = input("Please enter your equation in format y = kx + b:\n")

# "y = 2x + 3"
# "y = -200.4x - 555.55"
# "y = 5x"
# "y = -x + 43"
# "y = -3x - 122"
# "y = 3*x + 42" # задание со звёздочкой


print("до преобразования",eq)
eq=eq.replace(" ","")
print(eq)

r=eq.find("=")
print("Позиция знака равно", r)

if (len(eq)-1)==eq.find("x"):
    b=0
    
else:
    if ("*" in eq): 
        symbol=eq.find("*")
        print("Позиция переменной равно при *",symbol)
        b = Decimal (eq[(symbol+2):(len(eq))])
    else: 
        symbol=eq.find("x")
        print("Позиция переменной равно при отс знака",symbol)
        b = Decimal (eq[(symbol+1):(len(eq))])

if eq.find("x")==2:
    k=1

elif (eq.find("x")==3 and eq[2]=="-"):
    k=-1
else: 
    k = Decimal (eq[(r+1):(eq.find("x"))])


print("K = ",k,type(k))



print("b = ",b,type(b))

x = Decimal(input("Please eneter the x value:\n"))

y=k*x+b

print("the answer is y=",y)
