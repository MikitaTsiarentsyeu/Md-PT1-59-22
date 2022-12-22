depth_list = [1,2,[3,4,[5,6],8,[2,[3,7,8],5,8],[7,8],9]]
def sum_list_numb(l:list) -> "taking list return sum(number)":
    if len(l) == 1:
        if isinstance(l[0],list):
            riturn = sum_list_numb(l[0])
        else:
            riturn = l[0]
    elif isinstance(l[0],list):
        remove = l.pop(1)
        riturn = sum_list_numb(l)
    elif isinstance(l[1], list):
        remove = l.pop(0)
        l[0].append(remove)
        riturn = sum_list_numb(l)
    else:
        remove = l.pop(1)
        l[0] += remove
        riturn = sum_list_numb(l)
    return riturn
print(sum_list_numb(depth_list))


def fibonaci(number) ->"fibonaci(5) return list[0,1,1,2,3]":
    if number == 1:
        list_n = []
        list_n.append(0)
        return list_n
    list_return = fibonaci(number-1)
    number -= 1
    if len(list_return) == 1:
        list_return.append(number-list_return[number-1])
    else:
        list_return.append(list_return[number-2]+list_return[number-1])
    return list_return

print(fibonaci(12))

def str_rear_front(st_text)-> "word hello to word olleh ":
    if len(st_text) == 0:
        return st_text
    changed = str_rear_front(st_text[1:]) + st_text[0]
    return changed

f = "hello bro"
print(str_rear_front(f))

def quick_sort(s):
    if len(s) <= 1:
        return s
    element = s[0]
    "takin a reference element, for exemple s[0] == 2"
    left = list(filter(lambda x: x < element,s))
    "then controls it, if there is elements less than 2,and return list of elements less then 2  [1]"
    center = [i for i in s if i == element]
    "taking reference element as middle point,why list ? there can be more then one same elements, return a " \
    "list of reference elements"
    right = list(filter(lambda x: x > element, s))
    "after controls it, if there is elements grater than 2,and return list of elements grater then 2  [6,8,9,4,6,4]"
    "return result of lists summarised "
    "and so on till len(s) <= 1"
    return quick_sort(left) + center + quick_sort(right)

f = [2,6,8,9,4,1,6,4]
print(quick_sort(f))
