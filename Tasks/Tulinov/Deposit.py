import decimal

a = decimal.Decimal(input("Введите начальную сумму вклада "))
b = decimal.Decimal(input("Введите срок размещения в годах? "))
c = decimal.Decimal(input("Годовая процентная ставка? "))
d = decimal.Decimal(input("Если вам необходима капитализация поставьте 0, если ненужна поставьте 1? "))
f = 12

if d == 0:
    S = (a * ((1 + ((c/100)/f))**(f*b)))
    print (S)

if d == 1:
    S = (a + a * (c/100))
    print (S)