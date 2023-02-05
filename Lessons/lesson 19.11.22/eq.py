a, b, c = int(input("Enter the a value")), int(input("Enter the b value")), int(input("Enter the c value"))
if a == 0:
    print("the a value must be greater than 0")
    exit()

D = b*b - 4*a*c

if D>0:
    x1, x2 = (-b - D**0.5)/(2*a), (-b + D**0.5)/(2*a)
    print("The answer is ", x1, ', ', x2)
elif D==0:
    x = -b/(2*a)
    print("The answer is ", x)
else:
    print("there are no roots")