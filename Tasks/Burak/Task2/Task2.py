from decimal import Decimal
equation = input('Please enter an equation of the following type y = kx + b:\n')
eq = equation.replace(' ', '')
eqwithoutstar = eq.replace('*', '')
eqinlist = list()
eqinlist.extend(eqwithoutstar)
del eqinlist[:2]
k = Decimal(''.join(eqinlist[:eqinlist.index('x')]))
b = Decimal(''.join(eqinlist[eqinlist.index('x')+2:]))
if k == '':
    k = 1
elif k == '-':
    k = -1
x = Decimal(input('Please, enter the value of "x":\n'))
print(f"So, the result of your equation is:\n{x*k + b}")
