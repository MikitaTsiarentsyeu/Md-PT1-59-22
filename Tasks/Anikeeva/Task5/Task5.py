string = "The quick Brown Fox"
if len(string) < 1:
        print("Enter something")
else:
    def check_str(string):
        counter1 = 0
        counter2 = 0
        for i in string:
            if i.isupper():
                counter1 += 1
            elif i.islower():
                counter2 += 1
            else:
                pass
        return f'{counter1} upper case, {counter2} lower case'
    print (check_str(string))

def is_prime(n):
    if n == 2 or n == 3: 
        return True
    if n % 2 == 0 or n < 2: 
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
print(is_prime(2381))

list1 = [0,1,2,3,4,5,8,9,11,13,14,15,17,19,20]
def get_ranges(l):
    list2 = []
    counter = 0
    for i in range(len(list1)):
        if i != len(list1)-1 and list1[i+1]-list1[i] == 1:
            counter += 1
        elif counter == 0:
                list2.append(str(list1[i]))
        else:
            list2.append(f'{list1[i-counter]}-{list1[i]}')
            counter = 0
    return f'{",".join(list2)}'
print (get_ranges(list1))