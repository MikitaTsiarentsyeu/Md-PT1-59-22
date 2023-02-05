
# Начальная сумма депозита
summa = float(input ('Начальная сумма'))
# Срок в годах
term = float(input ("Срок депозита в годах" ))
#Годовой процент
pro = float(input('Годовой процент'))
t = summa * (1 + pro/100*term)
k = summa *((1 + pro/100*term) ** term)
#Спросить нужна ли капитализация
if input('Нужна ли капитализация? (Да/Нет) ').lower() == 'да': print (round(k,2))
else: print(round(t,2))