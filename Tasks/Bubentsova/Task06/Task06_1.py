def elements_sum(s, i=0, res=0):
    if i == len(s):
        return res
    if isinstance(s[i], list):
        res += elements_sum(s[i])
    else:
        res += s[i]
    return elements_sum(s, i+1, res)


print(elements_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))
print(elements_sum([1, 2, [2, 4, [[7, 8], 4, 6]], [23, [1, 2]], [5], [8, 1]]))
print(elements_sum([1, 2, [2, 4, [[7, 8], 4, 6]], [23, [1, 2]], [5], [8, 1], 4, 7.5, [12, 58]]))