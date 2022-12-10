# 1. Подготовиться к чтению содержимого файла text.txt
# 2. Дать пользователю ввести с клавиатуры условный параметр "максимальное количество символов в строке", 
# который должен быть больше 35
# 3. Отформатировать текст с учётом максимального количества символов, при этом
# если слово целиком не умещается в строке, оно должно быть перенесено на следующую, 
# а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
# (модуль textwrap использовать нельзя)

while True:
    number_user = input("Please enter the maximum number in line (more than 35 only)\n")

    if len(number_user) != 2:
        print("Please use only two digits\n")
        continue
    if not number_user.isnumeric():
        print("The data is in incorrect format, you must only use digits")
        continue
    number = int(number_user)
    if number < 35:
        print("The value must be more than 35")
        continue
    break

list = []
with open('ss.txt', 'r') as donor:    
    with open('ss_new.txt', 'w') as receiver:   
        text = donor.read().split()   
        for i in text:           
            if number - len(''.join(list)) >= len(i):  
                list.append(i), list.append(' ')  
            else:   
                while len(''.join(list).rstrip()) != number: 
                    for j, k in enumerate(list):
                        if len(''.join(list).rstrip()) == number: 
                            break 
                        if k != ' ':
                            list.insert(j + 1, ' ') 
                receiver.write(''.join(list) + '\n') 
                list = [i, ' ']
        receiver.write(''.join(list))
print ('New file ready')
