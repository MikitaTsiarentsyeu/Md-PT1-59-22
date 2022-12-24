
while True:
    param = input("Please enter line width (at least 35)\n")
    if param.isnumeric() == False: 
        print("Entered number must be numbers!")
        continue
    param = int(param)
    if param < 35:
        print("Entered number mast be greater then 34!")
        continue
    break

with open("text.txt",'r') as f:
    s = f.read()

s = s.split()
new_cand = '' # очередная строка-кандидат для анализа
str_file = '' # новые данные для файла в целом 
new_line = '' # новая строка, длиной param, которая войдёт в состав str_file

n = len(s) # общее кол-во элементов списка (слов из файла)
n1 = 0 # номер первого слова очередной строки (в общем списке)
n2 = 0 # номер последнего слова очередной строки (в общем списке)

words_k = 0  # кол-во слов в новой строке
space_k = 0  # кол-во пробелов в новой строке
space_dop_k = 0 # кол-во доп пробелов, которые нужно вставить до param
symbol_k = 0 # кол-во символов в строке с одиночными пробелами (не нормализованная строка)

pr_end_of_spisok = False
i = 0
while i < n:
    new_cand = s[i] # добавляем первое слово строки
    n1 = i
    n2 = i
    i += 1 # чтобы взять следующее слово
    while len(new_cand) < (param + 1) and pr_end_of_spisok == False: # (param + 1): учитываем \n
        if i != n: # если слово не последнее
            new_cand = new_cand + ' ' + s[i]
            n2 = i
            i += 1
        else:
            pr_end_of_spisok = True
    else: # если длина строки превысила param или мы достигли конца списка
        if pr_end_of_spisok == False:
            n2 -= 1 # восстановим корректное n2
            i -= 1  # -1 и у нас i будет указывать на следующий за корректным n2
            symbol_k = len(new_cand) - len(' ' + s[i]) 
        else:
            symbol_k = len(new_cand)
            # n2 здесь у нас и так корректный
            # i здесь = n2+1

        space_dop_k = param - symbol_k
        words_k = n2 - n1 + 1 # +1 коррекция n2 - n1
        
        if words_k == 1:
            space_k = 0
        elif words_k > 1:
            space_k = words_k - 1

        # сформируем матрицу пробелов на очередную строку *****
        pr = [' ' for m in range(space_k)] # создаём нужное коли-во промежуточных пробелов
        used_spaces = 0 # использованные доп пробелы
        if space_k == 0:
            # добавим в конце единственного слова недостающие space_dop_k пробелов
            pr.append(' ' * space_dop_k)
        elif space_k == 1:
            # добавим к единственному пробелу space_dop_k пробелов
            pr[0] = ' ' * space_dop_k
        elif space_k >= space_dop_k:
            # если реальных пробелов больше (или такое же), чем (как) дополнительных
            while used_spaces < space_dop_k:
                p = 0
                while p < space_k:
                    pr[p] += ' '
                    used_spaces += 1
                    p += 1
                    if space_dop_k == used_spaces: # если пробелы закончатся в "середине"
                        break
        else: # space_k < space_dop_k
            p = 0
            while p < space_dop_k:
                i_space = 0
                while i_space < space_k:
                    if p < space_dop_k:
                        pr[i_space] += ' '
                        i_space += 1
                        p += 1
                    else:
                        break
        
        # сформируем очередную строку *****
        j = n1
        i_pr = 0
        while j <= n2:
            if j != n2:
                new_line += s[j] + pr[i_pr]
                i_pr += 1
            else:
                new_line += s[j] + '\n'
            j += 1

        str_file += new_line
        new_line =''

print(str_file)

with open("res.txt",'w') as f:
    f.write(str_file)

print('Отформатированный текст успешно записан в файл "res.txt"')
