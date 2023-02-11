list1 = list(map(int, input('Enter non-repeating integers in ascending order separated by commas:\n').split(',')))
def get_ranges(l):
    list2 = []
    counter = 0
    for i in range(len(list1)):
        if i != len(list1)-1 and list1[i+1]-list1[i] == 1:
            counter += 1
        elif counter == 0:
                list2.append(str(list1[i]))
        else:
            list2.append(f'{list1[i-counter]}-{list1[i]}')
            counter = 0
    return f'{",".join(list2)}'
print (get_ranges(list1))
