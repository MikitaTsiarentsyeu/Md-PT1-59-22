C = float(input("Введите начальную сумму вклада"))
n = int(input("На сколько лет?"))
p = int(input("Под какой процент?"))
S = C
for i in range(0,n):
    S=S/100.0*p+S
print ('Количество денег за', n, ' лет составит', '%.2f' % S, 'рублей')

C = float(input("Введите начальную сумму вклада"))
n = int(input("На сколько месяцев?"))
p = float(input("Под какой процент в месяц?"))
S = C
for i in range(0,n):
    S=S/100.0*p+S
print ('Количество денег за', n, ' месяцев составит', '%.2f' % S, 'рублей')

C = float(input("Введите начальную сумму вклада"))
n = int(input("На сколько дней?"))
p = int(input("Размер годовой ставки"))
k = int (365) #кол-во дней в году
S = C*(1+(p/100)/k)**n
print ('За', n, 'дней Вы получите', '%.2f' % S, 'рублей')