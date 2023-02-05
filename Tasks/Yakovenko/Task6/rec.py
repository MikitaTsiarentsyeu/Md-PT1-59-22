def merge(l1,l2):
    i=j=0
    finish_list=[]

    while i<len(l1) and j<len(l2):

        if l1[i] < l2[j]:
            finish_list.append(l1[i])
            i+=1
        else:
             finish_list.append(l2[j])
             j+=1
    if i<len(l1):
        finish_list += l1[i:]
    if j<len(l2):
        finish_list += l2[j:]        
    return finish_list

def m_sort(list):

    if len(list) == 1:
        return list

    mid = len(list)//2
    left = m_sort(list[:mid])
    right = m_sort(list[mid:])

    return merge(left,right)

print(m_sort([3,51784187,188,2,5685,6,7]))

def quick(l):
    if len(l) <=1:
        return l

    base = l[1]
    left = list(filter(lambda x: x<base, l))
    mid = [i for i in l if i == base]
    right = [j for j in l if j > base]

    return quick(left) + mid +quick(right)

print(quick([18,1234,1,1,2,3,55]))


def sum(li):
    summ = 0
    for i in li:
        if isinstance(i,list):
            summ += sum(i)
        else:
            summ += i
    return summ
li = [1, 1, [1, 1, [[1, 1], 1, 1]]]
print(sum(li))

def reflect(s):
    if len(s)==1:
        return s
    else:
        return reflect(s[1:]) + s[0]
s="abc2"
print(reflect(s))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

number = int(input('Enter a number: '))
fibo_series = []
for i in range(0, number):
    fibo_series.append(fibonacci(i))
print(fibo_series)