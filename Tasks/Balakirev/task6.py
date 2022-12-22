def sum_el(lst: list) -> int:
    total = 0
    for element in lst:
        if isinstance(element, list):
            total = total + sum_el(element)
        else:
            total = total + element
    return total


lst = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(f"{lst}, cумма элементов равна - {sum_el(lst)}")


def fibonacci(n: int) -> list:
    if n == 2:
        return [0, 1]
    li = fibonacci(n - 1)
    li.append(li[-1] + li[-2])
    return li


print(f"fib(5) -> {fibonacci(5)}")
print(f"fib(10) -> {fibonacci(10)}")


def reverse(string: str) -> str:
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


string = 'hello'
print(f'reverse("hello") => {reverse(string)}')


def merge(left_list, right_list):
    sorted_list = []
    left_index = right_index = 0
    left_length, right_length = len(left_list), len(right_list)
    for i in range(left_length + right_length):
        if left_index < left_length and right_index < right_length:
            if left_list[left_index] <= right_list[right_index]:
                sorted_list.append(left_list[left_index])
                left_index += 1
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1
        elif left_index == left_length:
            sorted_list.append(right_list[right_index])
            right_index += 1
        elif right_index == right_length:
            sorted_list.append(left_list[left_index])
            left_index += 1
    return sorted_list


def merge_sort(mylist: list) -> list:
    if len(mylist) <= 1:
        return mylist
    mid = len(mylist) // 2
    left_list = merge_sort(mylist[:mid])
    right_list = merge_sort(mylist[mid:])
    return merge(left_list, right_list)


mylist = [10, 5, 8, 2, 7]
print(merge_sort(mylist))
