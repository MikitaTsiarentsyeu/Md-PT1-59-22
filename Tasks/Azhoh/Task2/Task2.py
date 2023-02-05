eq = input("Dear friend, enter the task in the format: y = kx + b \n")
res1 = eq.replace(" ","").replace("*","").replace("+","").replace("=","").replace("y","")
res2 = res1.split("x")
k = float(res2[0])
b = float(res2[1])
x = float(input("Please enter the value x: \n"))
y=(k*x)+b

print("Result of the k value:", k)
print("Result of the b value:", b)
print("Result of the task value: y = ", round(y,2))