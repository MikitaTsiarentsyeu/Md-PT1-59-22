def maker(n):
    def action(x):
        return x ** n
    return action

square = maker(2)
cube = maker(3)
forth = maker(4)
# for i in range(1, 5):
#     print(square(i)))

funcs = [maker(i) for i in range(1, 101)]
print([f(2) for f in funcs])