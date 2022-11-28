# #Реализовать:
# 1.текстовый вывод текущего времени
# 2.текстовый вывод времени, введённого с консоли (пользователь должен вводить данные в формате hh:mm).
# Дать пользователю возможность выбрать режим работы программы, время выводить числительными на русском языке.

# Для получения текущего времени использовать модуль datetime.

# min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
# min == 30: половина такого-то (15:30 - половина четвёртого)
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
# min >= 45 без min такого-то (08:54 - без шести минут девять)

from datetime import datetime

type_of_work = input("Please enter the type of program operation: current time(c) or your time (t):\n")
while True:
    if len(type_of_work) != 1:
        print("Please enter the program type in the correct form: current time(c) or your time (t):")

    if type_of_work[0] != 'c' or type_of_work[0] != 't':
        print("The data is in incorrect format, a dot is mnissing")

print("the main logic goes here")
# # Current datetime
# now = datetime.now().time()
# current_time = [now.hour, now.minute]

# while True:
#     user_input = input("Please enter the data in the dd.mm.yyyy format:\n")

#     if len(user_input) != 10:
#         print("The data is in incorrect format, the length is wrong")
#         continue

#     if user_input[2] != '.' or  user_input[5] != '.':
#         print("The data is in incorrect format, a dot is mnissing")
#         continue

#     parts = user_input.split('.')
#     failed = False
#     for i, part in enumerate(parts):
#         if not part.isnumeric():
#             failed = True
#             break
#         parts[i] = int(part)


