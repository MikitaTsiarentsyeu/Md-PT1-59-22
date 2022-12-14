# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию
# о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'

# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False

# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
# отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

def check_str(a:str) -> str:
    "WRITE ONLY STRING PLEASE :)"
    counterUp = 0
    counterDown = 0
    for i in a:
        if i == " ":
            a.replace(" ","")
        if i.isupper():
            counterUp += 1
        if i.islower():
            counterDown += 1            
    print(f"{counterUp} upper case,{counterDown} lower case")

check_str(a = input("Please input string:\n"))


def is_prime(digit:int) -> bool:
    if digit == 2 or digit == 3: 
        return True
    if digit % 2 == 0 or digit < 2: 
        return False
    for i in range(3, int(digit ** 0.5) + 1, 2):
        if digit % i == 0:
            return False
    return True
print(is_prime(355))
