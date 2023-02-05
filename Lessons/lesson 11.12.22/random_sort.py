import random

l = [4,2,6,3,4,7,5,1,8]


[4,2,6,3,4,7,5,1,8]
[4,3,6,2,4,7,5,1,8]
[8,3,6,2,4,7,5,1,4]
[8,3,6,2,4,7,5,4,1]


def sort(l:list):
    counter = 0
    while not is_sorted(l):
        counter += 1
        print(counter)
        swap(l)

def is_sorted(l:list) -> bool:
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def swap(l:list):
    i = generate_index(len(l))
    j = i
    while i == j:
        j = generate_index(len(l))
    l[i], l[j] = l[j], l[i]

def generate_index(n:int) -> int:
    return random.randint(0, n-1)

sort(l)
print(l)