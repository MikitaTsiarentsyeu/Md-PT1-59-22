user_list = [2,3,4,22,23,5,7,8,9,10,11,13,4,15,17,18,55,2]
new_list = sorted(set(user_list))
print(new_list)
def get_ranges(new_list):
    l = []
    for i in range((len(new_list)-1)):
        if new_list[i]+1 == new_list[i+1] and new_list[i]-1 != new_list[i-1]:
            l.append(str(new_list[i])+'-')
        elif new_list[i]+1 != new_list[i+1] and new_list[i]-1 == new_list[i-1]:
            l.append(str(new_list[i])+', ')
        elif new_list[i]+1 != new_list[i+1] and new_list[i]-1 != new_list[i-1]:
            l.append(str(new_list[i])+', ')
    if new_list[-1]-1 == new_list[-2]:
        l.append(str(new_list[-1]))
    else:
        len(new_list)
    if new_list[-1]-1 != new_list[-2]:
        l.append(str(new_list[-1]))
    else:
        len(new_list)
    return (''.join(l))
print(get_ranges(user_list))