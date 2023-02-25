while True:
    task = input("Please enter the maximum number in line 'more than 35 only'\n")
    if not task.isdigit():   
        print('Please enter only numbers\n')
        continue
    task = int(task) 
    if task <= 35: 
        print('Please enter more than 35 symbols\n')
        continue
    break      
with open('text.txt', 'r', encoding = 'utf-8') as start:    
    with open('example_40.txt', 'w', encoding = 'utf-8') as finish:   
        text = start.read().split()    
        list = [] 
        print(len(''.join(list)))
        for i in text:           
            if task - len(''.join(list)) >= len(i):  
                list.append(i), list.append(' ')  
            else:   
                list.pop() 
                while len(''.join(list).rstrip()) != task: 
                    for j, k in enumerate(list):
                        if len(''.join(list).rstrip()) == task: 
                            break 
                        if k != ' ': 
                            list.insert(j + 1, ' ') 
                finish.write(''.join(list) + '\n') 
                list = [i, ' ']
        finish.write(''.join(list))
print ('your new file has been created successfully')