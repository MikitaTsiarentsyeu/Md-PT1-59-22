import random
"""import time

print ('\033[1m'"Let's conculate the sum of values from the list"'\033[0m')
def sum(l):
    res=0
    for i in l:
        if not isinstance(i, list):
            res+=i         
        else:
          res=sum(i)+res
    return res
l = [1, 2, [2, 4, [[7, 8], 4, 6]]]
res01 = sum(l)
print(f'The result is: {res01}')

time.sleep(2)

print ('\033[1m'"Next we'll count the Fibonacci numbers"'\033[0m')
def fib(n: int) -> list:
    
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    li = fib(n-1)
    li.append(li[-1] + li[-2])
   
    return li
res = fib(int(input('Please, enter your values:\n')))
print(f'The result is: {res}')

time.sleep(2)

print ('\033[1m'"We can also reverse your string \n"'\033[0m')
def reverseString(any_string):
    if len(any_string) == 1:
        return any_string
    else:
        return  any_string[-1] + reverseString(any_string[:-1])
   

res2= reverseString(str(input('Enter your string \n')))
print(f'The resuli is \n {res2}')


print ('\033[1m'"Let's try to sort values with marge sort\n"'\033[0m')

time.sleep(2)

def merge_sort(nums):
   
    part1 = len(nums) // 2
    n1 = nums[:part1]     
    n2 = nums[part1:]

    if len(n1) > 1:
        n1 = merge_sort(n1)
    if len(n2) > 1: 
        n2 = merge_sort(n2)
        
    list_of_numbers = []
    partone = len(n1)
    parttwo = len(n2)

    i = 0
    k = 0

    
    while i < partone and k < parttwo:
        if n1[i] <= n2[k]:
            list_of_numbers.append(n1[i])
            i += 1
        else:
            list_of_numbers.append(n2[k])
            k += 1

    list_of_numbers += n1[i:] + n2[k:]
    return list_of_numbers


a = merge_sort(list(input('Please, input the list of numbers through space \n').split(" ")))
ares3=" ".join(a)
print(f'The result is \n {ares3}')

print ('\033[1m'"Let's try to sort values with quick sort\n"'\033[0m')
time.sleep(2)"""

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums, m_nums,e_nums = [], [], []
       
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)

a = quicksort(list(input('Please, input the list of numbers through space \n').split(" ")))
ares4 = " ".join(a)
print(f'The result is \n {ares4}')