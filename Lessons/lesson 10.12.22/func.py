def test_print(val):
    print(str(val).upper())

test_print(4567)
test_print("test")

def my_sum(x, y):
    return x+y

print(my_sum(2, 3))

print(type(my_sum), my_sum)

# test_func() error

def test_func():
    print("this is just a test")


def level1():
    print("level 1")
    res = level2()
    print("end of level 1")
    return res

def level2():
    print("level 2")
    res = level3()
    print("end of level 2")
    return res

def level3():
    print("level 3")
    print("end of level 3")
    return "the most important value in the universe"

res = level1()
print(res)


# sign = "*"
# if sign == "+":
#     def operator(x, y):
#         return x+y
# elif sign == "*":
#     def operator(x, y):
#         return x*y  VERY BAD APPROACH

def operator(x, y, sign):
    if sign == "+":
        return x+y
    elif sign == "*":
        return x*y 

print(operator(2, 3, "+"))


def test_args_func(x, y):
    print(f"x: {x}, y: {y}")

test_args_func("second value", "first value")

# test_args_func(1, 2, 3)

def test_ref(x):
    print(id(x))
    x[0] += 2
    print(id(x))

test_val = [3]
print(id(test_val))
test_ref(test_val)
print(id(test_val))
print(test_val)


def return_several_values(x, y):
    return x, y, x+y

x, y, res = return_several_values([2], [3])
print(x, y, res)

def return_none():
    return

x = return_none()
print(repr(x))