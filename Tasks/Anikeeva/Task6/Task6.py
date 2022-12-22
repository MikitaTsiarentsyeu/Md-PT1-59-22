import random
def results (res):
    sum = 0
    for element in res:
        if (type (element)) == type ([]):
            sum = sum + results (element)
        else:
            sum = sum + element
    return sum
print ("The sum is equal to the elements:", results([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib(num):
    while num > 0:
        if num == 1:
            return [0]
        elif num == 2:
            return [0, 1]
        list = fib(num-1)
        list.append(list[-1] + list[-2])
        return list
print(fib(10))


def reverse(back):
    if len(back) == 1:
        return back
    return back [-1] + reverse (back [:-1])
s = reverse (input())
print(s)


def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)
list = [-2, 14, 48, 42, -48, 38, 44, -25, 14, -14, 41, -30, -35, 36, -5]
print (quicksort(list))


def mergeSort(lst):
    if len(lst)>1:
        mid = len(lst)//2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                lst[k]=lefthalf[i]
                i=i+1
            else:
                lst[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            lst[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            lst[k]=righthalf[j]
            j=j+1
            k=k+1
lst = [-2, 14, 48, 42, -48, 38, 44, -25, 14, -14, 41, -30, -35, 36, -5]
mergeSort(lst)
print(lst)