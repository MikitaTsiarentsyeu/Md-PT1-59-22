d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
     'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
     'eighteen': 18, 'nineteen': 19, 'twenty': 20}


number = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()
for i in range(len(number)):
    number[i] = d[number[i]]
print(number)


number = set(number)
print(number)


number = sorted(number)
print(number)


for i in range(len(number)-1):
    if i % 2 == 0:
        print(f'{number[i]}*{number[i+1]} = {number[i]*number[i+1]}')
    else:
        print(f'{number[i]}+{number[i+1]} = {number[i]+number[i+1]}')


for i in range(0, 21, 2):
    if i in number:
        number.remove(i)
print(sum(number))


#перейти от строки к набору целых чисел
#исключить дубликаты
#отсортировать по возрастанию
#вывести произведение первого и второго чисел, сумму второго и третьего, произведение третьего и четвёртого и т. д. для коллекции любой длины
#вывести полную сумму всех нечётных чисел
#использовать в программе только одну переменную
