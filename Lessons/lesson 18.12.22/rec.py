def print_hello(n):
    i = 0
    while True:
        print("hello")
        i+=1
        if i == n:
            break


print_hello(5)

def print_hello(n, i=0):
    if i == n:
        return
    print("hello")
    print_hello(n, i+1)

print_hello(5)
# 1! = 1
# 2! = 1*2 = 2
# 3! = 1*2*3 = 6
# 4! = 1*2*3*4 = 24

def factorial(n):
    if n == 1:
        return 1
    c = factorial(n-1)
    print(c)
    return c*n
    
print(factorial(4))


# 486 => 18
# 1111 => 4

def digit_sum(n:int):
    if n == 0:
        return 0
    return n%10 + digit_sum(n//10)

print(digit_sum(123))


def digit_sum(n, i, res=0):
    n = str(n) if isinstance(n, int) else n
    if i == len(n):
        return res
    res += int(n[i])
    return digit_sum(n, i+1, res)
