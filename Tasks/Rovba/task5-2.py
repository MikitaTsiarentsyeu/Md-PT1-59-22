"""
2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
is_prime(787) -> True
is_prime(777) -> False
"""

def is_prime(n:int) -> bool:
    if n == 1 or n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True


while True:
    p = input("Please enter a number greater then zero\n")
    if p.isnumeric() == False: 
        print("Entered number must be numbers!")
        continue
    p = int(p)
    if p < 1:
        print("Entered number mast be greater then zero!")
        continue
    break

if is_prime(p):
    print(p, "is prime number")
else:
    print(p, "is composite number")
