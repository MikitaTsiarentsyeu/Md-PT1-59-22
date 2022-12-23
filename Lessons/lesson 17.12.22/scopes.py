for i in range(10):
    i+1

print(i)
x = list("global value")

def scopes_test():
    # print(x)
    x = list("scopes test")
    print(x)

scopes_test()
print(x)

def fisrt_func(x):
    print(x)

def second_func(x):
    print(x)

def third_func(x):
    print(x)

fisrt_func(100)
second_func("test")
third_func([1,2,3])
print(x)



def test_global():
    global x
    x = "new value from test_global"

print(x)
test_global()
print(x)


def outer_func():
    outer_x = "outer"
    def inner_func():
        nonlocal outer_x
        outer_x = "inner"
        print(outer_x)
        print("inner func")
    inner_func()
    print(outer_x)
    return inner_func

y = outer_func()
y()
y()
y()
y()