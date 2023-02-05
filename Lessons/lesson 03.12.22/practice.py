d = {"one":1, "two":2, "three":3, "four":4, "five":5, "eight":8, "ten":10, "eleven":11, "thirteen":13, "seventeen":17, "nineteen":19}

s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

l = [d[i] for i in s.split()]
print(l)

l = list(set(l))
print(l)

# print(sum([x for x in l if x%2 != 0]))

# [print(l[i]*l[i+1]) if i%2==0 else print(l[i]+l[i+1]) for i in range(len(l)-1)]

sum = 0
flag = True
for i in range(len(l)-1):
    if flag:
        print(l[i]*l[i+1])
    else:
        print(l[i]+l[i+1])

    flag = not flag
    if l[i] % 2 != 0:
        sum += l[i]

if l[i+1] % 2 != 0:
    sum += l[i+1]

print(sum)