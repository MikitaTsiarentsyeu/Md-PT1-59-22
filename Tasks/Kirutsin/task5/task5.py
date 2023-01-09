# 1 task
def check_str(text_source: str) -> str:
    index_upper = 0
    index_lower = 0

    for i in text_source:
        # checking lower
        if i.lower() == i and i.upper() != i:
            index_lower += 1
        # checking upper
        if i.lower() != i and i.upper() == i:
            index_upper += 1
    final_string = str(index_upper) + ' upper case, ' + str(index_lower) + ' lower case'
    return final_string

# test 1
# source = 'The quick Brown Fox'
# print(check_str(source))



# 2 task
def is_prime(int_source: int) -> bool:
    index = 0

    # calculations
    for i in range(int_source):
        if i != 0:
            if int_source % i == 0:
                index += 1
    if int_source % int_source == 0:
        index += 1

    # result
    if index == 2:
        result = True
    else:
        result = False
    return result

# test 2
# source = 777
# print(is_prime(source))


# 3 task
def get_ranges(list_source: list) -> str:
    path = []
    index = 0

    # calculations
    for i in range(len(list_source)):
        if i != len(list_source)-1 and list_source[i+1]-list_source[i] == 1:
            index += 1

        elif index == 0:
            path.append(str(list_source[i]))

        elif index != 0:
            path.append(f'{list_source[i - index]}-{list_source[i]}')
            index = 0

    result = f'{",".join(path)}'
    return result

#test 3
source = [0, 1, 2, 3, 4, 7, 8, 10]
print(get_ranges(source))