def fibonacci(n: int) -> list:
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    li = fibonacci(n - 1)
    li.append(li[-1] + li[-2])
    return li


print(f"fib(6) -> {fibonacci(6)}")
print(f"fib(12) -> {fibonacci(12)}")