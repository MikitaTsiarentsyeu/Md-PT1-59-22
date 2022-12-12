user_symb = (input("Please enter max symbols in the string more than 35:\n"))
if user_symb.isdigit() == True:
    user_symb = int(user_symb)
    if int(user_symb) <= 35:
       print("Incorrect value") 
    else: 
        if int(user_symb) > 35:
          print("Correct value")
          with open('text.txt', 'r') as text:
            print("Hello, you open the file text.txt")
            with open('formatted_text.txt', 'w') as formatted_text: 
                text = text.read().split()
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
                        formatted_text.write(''.join(list) + '\n') 
                        list = [i, ' ']
                formatted_text.write(''.join(list))
        print ("Formatted text is ready")  
