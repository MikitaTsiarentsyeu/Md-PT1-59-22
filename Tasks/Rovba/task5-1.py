"""
1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию
о количестве букв в верхнем и нижнем регистре.
check_str('The quick Brown Fox') -> '3 upper case, 13 lower case
"""

def check_str(s) -> str:

    sum_big = 0
    sum_small = 0
    Big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    Small_letters = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    for s_index in range(0, len(s)):
        if s[s_index] in Big_letters:
            sum_big += 1
        elif s[s_index] in Small_letters:
            sum_small += 1

    return f"{sum_big} upper case, {sum_small} lower case"


s = 'The quick Brown Fox'
print(check_str(s))
