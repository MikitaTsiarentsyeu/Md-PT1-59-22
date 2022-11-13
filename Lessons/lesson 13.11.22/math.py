print(type(5))

print(type(int('5')))

print(int(2.3))
print(int(2.8))
print(int(-2.8))

print(type(12/3) == type(12//3))
print(12/3 == 12//3)

print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))


print(type(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))

print(type(2.33))
print(1.1 + 2.2)

x = float('22.33')
print(type(x), x)
print(x)

print(float(45))

import decimal
# x = decimal.Decimal(0.1)
x = decimal.Decimal('0.1')
print(type(x))
print(x)
print(x*3)

print(float('0.1')+float('0.1')+float('0.1'))
print(decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1'))

import fractions
x = fractions.Fraction('1.48')
print(x+x*2)

import math
print(math.pow(2, 10))
print(math.pow(144, 0.5))
print(math.sqrt(144))
print(math.sin(math.pi))