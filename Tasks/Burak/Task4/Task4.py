chunk = input('Please, enter the value of chunk you need, which must be higher than 35:\n')
if chunk.isdigit() == True:
    chunk = int(chunk)
    if chunk > 35:
        with open('text.txt', 'r') as text:
            with open('readytext.txt', 'w') as readytext:
                for i in text:
                    while i:
                        if len(i) > chunk:
                            line = i[:chunk + 1]
                            if ' ' in line:
                                if '\n' in line:
                                    line = line[:(line.rfind('\n') + 1)].split()
                                else:
                                    line = line[:(line.rfind(' ') + 1)].split()
                                index = 1
                                alignment = 1
                                while len(''.join(line)) < chunk:
                                    line.insert(index, ' ')
                                    if index + alignment + 1 >= len(line):
                                        alignment = alignment + 1
                                        index = 1
                                    else:
                                        index = index + alignment + 1
                                readytext.write(''.join(line) + '\n')
                                if '\n' in i[:chunk + 1]:
                                    i = i[i[:chunk + 1].rfind('\n') + 1:]
                                else:
                                    i = i[i[:chunk + 1].rfind(' ') + 1:]

                        else:
                            readytext.write(i.strip() + '\n')
                            i = ''
else:
    print('Perhaps the entered value is not a number or it is greater than 35.')
print('Good job!')
