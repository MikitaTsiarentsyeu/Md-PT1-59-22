def quicksort_rec(l):
    if len(l) < 2:
        return l
    else:
        ref_element = l[0]
        less_then_ref_element = [i for i in l[1:] if i < ref_element]
        greater_then_ref_element = [i for i in l[1:] if i > ref_element]
        return quicksort_rec(less_then_ref_element) + [ref_element] + quicksort_rec(greater_then_ref_element)


print(quicksort_rec([5, 15, 75, 3, 4, 7, 1, 8]))
print(quicksort_rec([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(quicksort_rec([12, 5, 7, 1, 3, 0, 0.1, 0.11, 0.112]))