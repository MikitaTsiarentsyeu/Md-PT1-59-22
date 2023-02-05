def apply(l, func):
    for i in l:
        func(i)

l = [1,2,3,4,5]
apply(l, print)

def proccess(x):
    print(x*x)

apply(l, proccess)