def level1():
    print("starting level1")
    level2()
    print("finishing level1")

def level2():
    print("starting level2")
    level3()
    print("finishing level2")

def level3():
    print("starting level3")
    level4()
    print("finishing level3")

def level4():
    print("starting level4")
    print("finishing level4")


def level(n=1):
    if n == 5:
        return
    print(f"starting level{n}")
    level(n+1)
    print(f"finishing level{n}")

# level1()
# print("the end")y

level()