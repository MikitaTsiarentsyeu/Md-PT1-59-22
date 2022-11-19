x = 20

if x == 0:
    print("it's zero")
elif x == 1:
    print("it's one")
elif x == 2:
    print("it's two")
elif x == 3:
    print("it's three")
else:
    print("idk this number")

print("the end")


x = 0

if x == 0:
    print("it's zero")
elif x > 0:
    print("it's positive")
else:
    print("it's negative")


if x >= 0:
    if x == 0:
        print("it's zero")
    elif x > 0:
        print("it's positive")
else:
    print("it's negative")

x = 10

if x == 10:
    pass
else:
    print("it's not ten")

x = False
print("it's true") if x else print("it's false")

if x:
    print("it's true")
else:
    print("it's false")



print("it's positive") if x > 0 else print("it's zero") if x == 0 else print("it's negative")

x = -1
x = "positive" if x > 0 else "negative"
print(x)