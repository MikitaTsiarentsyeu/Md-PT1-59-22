l = [5,2,3,7,5,6,8,4,1,0,2,4,6]

# sorted(l)[0]

min = 0
for i in range(1, len(l)):
    if l[i] < l[min]:
        min = i

print(min, l[min])