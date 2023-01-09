# task 1
def sum_list_numb(sourcer) -> int:
    numbers = 0
    index_list = []

    if type(sourcer) != int:
        if len(sourcer) == 2 and sourcer[1] == []:
            return sum_list_numb(sourcer[0])

        elif len(sourcer) == 2 and type(sourcer[0]) == type(numbers) and type(sourcer[1]) == type(index_list):
            for i in sourcer[1]:

                if type(i) == type(numbers):
                    numbers += i

                elif type(i) == type(index_list):
                    index_list += i

            return sum_list_numb([sourcer[0] + numbers, index_list])

        elif len(sourcer) != 1:
            for i in sourcer:

                if type(i) == type(numbers):
                    numbers += i

                elif type(i) == type(index_list):
                    index_list += i
            return sum_list_numb([numbers, index_list])

    else:
        return sourcer


# test_1 = sum_list_numb([1, 2, [22, 4, [[7, 8], 4, 6]]])
# print(test_1)


# task 2
def fibanachi(sourcer) -> list:
    # prepare and validation
    if type(sourcer) == int:
        if sourcer == 1:
            return [0]
        else:
            sourcer = [[0, 1], sourcer - 2]

    # calculations
    if type(sourcer) == list:
        if sourcer[1] != 0:
            total = sourcer[0]
            total.append(sourcer[0][-1] + sourcer[0][-2])
            fibanachi([total, (sourcer[1] - 1)])
    return sourcer[0]


# test_2 = fibanachi(10)
# print(test_2)

# task 3
def reverse(sourcer):
    # prepare
    if type(sourcer) == str:
        sourcer = [sourcer, len(sourcer), '']

    # calculations
    if type(sourcer) == list:
        if sourcer[1] == 0:
            return sourcer[2]

        elif sourcer[1] != 0:
            index_summ = sourcer[2] + sourcer[0][-1]
            index_del = sourcer[0][0:-1]
            return reverse([index_del, sourcer[1] - 1, index_summ])

# test_3 = reverse("hello")
# print(test_3)
