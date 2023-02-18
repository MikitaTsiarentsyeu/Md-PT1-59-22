while True:
    user_symb = (input('Please enter the maximum number of characters per line. More than 35 symbols:\n'))
    if not user_symb.isdigit():   
        print('Please enter only numbers!\n')
        continue
    user_symb = int(user_symb) 
    if user_symb <= 35: 
        print('Please enter more than 35 symbols!\n')
        continue
    break      

with open('text.txt', 'r', encoding = 'utf-8') as start:    
    with open('example_40_symbols.txt', 'w', encoding = 'utf-8') as finish:   
        text = start.read().split()    
        list = [] 
        for i in text:           
            if user_symb - len(''.join(list)) >= len(i):  
                list.append(i), list.append(' ')  
            else:   
                list.pop() 
                while len(''.join(list).rstrip()) != user_symb: 
                    for j, k in enumerate(list):
                        if len(''.join(list).rstrip()) == user_symb: 
                            break 
                        if k != ' ': 
                            list.insert(j + 1, ' ') 
                finish.write(''.join(list) + '\n') 
                list = [i, ' ']
        finish.write(''.join(list))
print ('Formatted text is ready:)')