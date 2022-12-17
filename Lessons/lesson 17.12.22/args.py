def sum(*args):
    # print(args, type(args))
    res = 0
    for i in args:
        res += i
    return res

print(sum(1,2,3,4,5,6,7,8,9,10))

def my_print(*args, sep=" ", end="\n"):
    print(*args, sep=sep, end=end)

my_print(1,2,3,4,5,sep=",",end='.\n')

print(sum(*[1,2,3]))


def sum(**kwargs):
    print(kwargs, type(kwargs))

sum(test=42,new_arg="test value")

d = {"one":1, "two":2, 3:3}
sum(**d)

def my_print(*args, **kwargs):
    if "sep" in kwargs and "end" in kwargs:
        print(*args, sep=kwargs["sep"], end=kwargs["end"])
    else:
        print(*args)

