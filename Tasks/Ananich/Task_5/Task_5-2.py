def is_prime(a):
    for i in range(2, (a//2)+1):
        if a%i == 0:
            return False
        else:
            return True
a = int(input("Enter a number:\n"))   
if a <=0:
    print("Error")
else:
    print(is_prime(a))     