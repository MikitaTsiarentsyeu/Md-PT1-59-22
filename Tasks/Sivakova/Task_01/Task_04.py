

filename =  "text.txt"

with open('text.txt', 'r', encoding='UTF-8') as r:
    print ('\033[1m') 
    print("Hi there! You open the text.txt file with the text:")
    print ('\033[0m')
    print(r.read())
    print ('\033[1m') 
    
user_value = int(input("Please enter the velue that will change the format of the text(more than 35/ press 0 to exit from the programm):\n"))
while user_value <= 35 and user_value>0:   
    print("Please, check the value")
    user_value = int(input("Please enter the velue that will change the format of the text(more than 35/ press 0 to exit from the programm):\n"))
else:
    print("Sucsses!")
    print ('\033[0m')
    


        
    def make_string(paragraph):
        words = paragraph.split()
        result = []
        safezone = []
        count = 0
        
        for word in words:
            if count+len(word)+1 <= user_value:
                lenghtplus = len(word) + 1
                count += lenghtplus
                safezone.append(word)
            elif count+len(word)+1 >= user_value:
                distance = (user_value - count)
                if distance < len(safezone):
                    for element in range(distance):
                        safezone[element]+= ' '
                    
                else:
                    for element in range(len(safezone)):
                        safezone[element]+= ' '
                    
                count = len(word)+1
                result.append(safezone)
                safezone = []
                safezone.append(word)      
        result.append(safezone)
        for symbol in range(len(result)):
            result[symbol] = ' '.join(result[symbol])
        edit = '\n'.join(result)    
        return edit





    with open('text.txt', 'r', encoding='UTF-8') as r:
        final = []
        usualtext = r.readlines()
        add = [final.append((make_string(paragraph))) for paragraph in (usualtext)]         
        with open('text1_copy.txt', 'w', encoding='UTF-8') as w:   
                w.writelines('\n'.join(final))
        print ('\033[1m')
        additional_q = input("Want to preview a file? Yes/No ")
        if additional_q == "Yes":
            with open('text1_copy.txt', 'r', encoding='UTF-8') as new_file:
                print ('You have created a new text file with the following content:') 
                print(new_file.read())
        else:
            print("Good luck!")
        print ('\033[0m')
