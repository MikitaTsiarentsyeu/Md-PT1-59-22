user = input ("Do you want to enter time by yersellf? Yes/No ")
if user == "Yes":
       while True:
        user1 = input("Please enter your time in the hh:mm fornmat only ")
 
        if len(user1) !=5:
            print("Please check out the format and try again")
            continue
        if user1[2] != ":":
            print("Please check out the dot and try again")
            continue
        numbers = user1.split(':')
        print(numbers)
        failed = False
        for i, num in enumerate(numbers):
            if not num.isnumeric():
                failed = True
                break
            numbers[i] = int(num)
        print(numbers)
    
        if failed:
            print("Please check out the format in a numbers and try again")
            continue

        if numbers[0] == 24:
            print("The first value myst be less then 24")
            continue
        
        break
  

