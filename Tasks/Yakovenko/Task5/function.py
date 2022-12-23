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

def get_ranges(a):
    l = []
    list_1 = []
    list_new = []
    string = ''
    
    for i in range(len(a)-1):
        if a[i+1] - a[i] >= 2:
            list_1.append(a[i+1])

    for j in list_1:
        x = a.index(j)
        l.append(x)
    
    for s in range(0,len(l)+1):                               
        if s == 0:
            p = a[s:l[s]]

        if s == len(l):
            p = a[l[s-1]:a[-1]]      

        if s != 0 and s != len(l):
            p = a[l[s-1]:l[s]]
        list_new.append(p)

    for y in list_new:
        if y == list_new[-1] and len(y) > 1:
            string += f'{y[0]}-{y[-1]}'

        elif y == list_new[-1] and len(y) == 1:
            string += f'{y[0]}'

        elif len(y) == 1:
            string += f'{y[0]}, '
            
        else: string += f'{y[0]}-{y[-1]}, '

    print(string)

get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])