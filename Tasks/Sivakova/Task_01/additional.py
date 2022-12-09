
i = input().split()
l = list(set([{"one":1, "two":2, "three":3, "four":4, "five":5, "eight":8, "ten":10, "eleven":11, "thirteen":13, "seventeen":17, "nineteen":19}[i] for i in i]))
print(sum([i for i in l if i %2 != 0]))
[print(l[i]*l[i+1]) if i%2==0 else print(l[i]+l[i+1]) for i in range(len(l)-1)]