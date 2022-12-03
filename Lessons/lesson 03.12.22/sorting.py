l = [4,2,3,5,7,6,8,0,9,1]

# l.sort()
print(sorted(l))
print(l)

test_str = "Abc Aac aaa aab"
print(sorted(test_str.split()))


#bubble sort
# for j in range(len(l)-1):
#     print(l)
#     for i in range(len(l)-j-1):
#         if l[i] > l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]
# print(l)


#selection sort
for i in range(len(l)-1):
    min = i
    current = i+1
    while current < len(l):
        if l[current] < l[min]:
            min = current
        current += 1
    l[i], l[min] = l[min], l[i]
    print(l)


print(l)