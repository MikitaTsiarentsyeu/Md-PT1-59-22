
#1
def sum_elements(sp):
    summa = 0
    for el in sp:
        if type(el) == list:
            summa += sum_elements(el)
        else:
            summa += el
    return summa

list1 = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(list1)
print('Summa=',sum_elements(list1))


#2
def fib(k):
    if k > 1:
        fib_list = fib(k-1)
    if k == 1:
        fib_list=[]  
        fib_list.append(0)
    elif k == 2:
        fib_list.append(1)
    else:
        fib_list.append(fib_list[k-2] + fib_list[k-3])
    return fib_list

print()
print('fib(5):', fib(5))        
print('fib(10):', fib(10))


#3
def reverse(s, i=-1):
    if i == len(s)-1: # усл выхода
        return
    i += 1
    reverse(s, i)
    print(s[i],end='')

print()
print('hello')
reverse('hello')


#4 
def merge_sort(u):
    if len(u) == 1:
        return u
    elif len(u) == 2:
        if u[0] > u[1]:
            u[0], u[1] = u[1], u[0]
        return u
    elif len(u) > 2: 
        an = len(u)//2
        a = merge_sort(u[:an])
        b = merge_sort(u[an:])
        ab = []
        while len(a)>0 or len(b)>0:
            if len(a)>0 and len(b)>0:
                if a[0] < b[0]:
                    ab.append(a.pop(0))
                else:
                    ab.append(b.pop(0))
            elif len(a)>0 and len(b)==0:
                ab.append(a.pop(0))
            elif len(a)==0 and len(b)>0:
                ab.append(b.pop(0))
        return ab

print('\n\nSorting:')
list3 = [6,5,3,1,8,7,2,4]
print(list3)
print(merge_sort(list3))
