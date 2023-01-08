def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_values = fib(n - 1)
        fib_values.append(sum(fib_values[:-3:-1]))
        return fib_values


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(5))
print(fib(10))
print(fib(15))