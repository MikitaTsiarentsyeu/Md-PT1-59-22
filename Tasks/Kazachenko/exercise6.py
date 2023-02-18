#1
def sum_el(s, i=0, res=0):
    if i == len(s):
        return res
    if isinstance(s[i], list):
        res += sum_el(s[i])
    else:
        res += s[i]
    return sum_el(s, i+1, res)

print(sum_el([1, 2, [2, 4, [[7, 8], 4, 6]]]))



#2
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return [0, 1]    
    f_list = fibonacci(n-1)
    f_list.append(f_list[-1] + f_list[-2])
    return f_list

print(fibonacci(10))   
print(fibonacci(5))


#3
def reverse(s):
    if len(s) ==1:
        return s
    return s[-1] + reverse(s[:-1])

print(reverse("hello"))



#4
def quicksort(l):
    if len(l)<2:
        return l
    else:
        ref_el = l[0]
        less_el = [i for i in l[1:] if i < ref_el]
        more_el = [i for i in l[1:] if i > ref_el]
        return quicksort(less_el) + [ref_el] + quicksort(more_el)

print(quicksort([0,1,1,2,3,5,8,13,21,34]))
print(quicksort([2,2,5,6,7,10,10,12,27,27]))

