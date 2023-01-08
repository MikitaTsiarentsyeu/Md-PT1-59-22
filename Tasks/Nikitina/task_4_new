while True:
    string = input("Please enter max symbols in the string more than 35:\n")

    if not string.isnumeric():
        print("Incorrect value")
        continue
    number = int(string)
    if number < 35:
        print("The value must be more than 35")
        continue
    break

list = []
with open('text.txt', 'r') as original:    
    with open('text_new.txt', 'w') as new_file:   
        text = original.read().split()   
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
                new_file.write(''.join(list) + '\n') 
                list = [i, ' ']
        new_file.write(''.join(list))
print ('New file ready')