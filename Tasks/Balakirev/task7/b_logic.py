import data


def get_all_contacts():
    names = data.directory_data()
    res = []
    list_cont = []
    if len(names) > 0:
        for row in names:
            for val in row.values():
                list_cont.append(val)
            res.append(', '.join(list_cont))
            list_cont = []
    return '\n'.join(res)


def add_contact(surname, name, number):
    if number.isnumeric():
        if len(number) > 12 and number[:3] == '375':
            info = {'Surname': surname, 'Name': name, 'Number': number}
            data.add_contact(info)
            return "Contact successfully created"
        else:
            return 'Invalid number format'
    else:
        return 'Invalid data format'


def edit_numbers(value, info):
    if info[1].isnumeric():
        if len(info[1]) == 12 and info[1][:3] == '375':
            return change(value, info)
        else:
            return 'Invalid number format'
    else:
        return 'Invalid data format'


def change(value, info):
    res = data.directory_data()
    result = []
    flag = False
    for i in res:
        if i['Surname'] == value or i['Name'] == value or i['Number'] == value:
            i[info[0]] = info[1]
            flag = True
        result.append(i)
    if flag:
        data.remove_rename(result)
        data.sorted_contact()
        return "Contact successfully created"
    else:
        return 'Contact not found'


def edit(value, info):
    if info[0] == 'Number':
        return edit_numbers(value, info)
    else:
        return change(value, info)


def remove(value):
    res = data.directory_data()
    result = []
    flag = False
    for i in res:
        if i['Surname'] == value or i['Name'] == value or i['Number'] == value:
            flag = True
        else:
            result.append(i)
    if flag:
        data.remove_rename(result)
        data.sorted_contact()
        return "Contact successfully removed"
    else:
        return 'Contact not found'


def search(value):
    content = data.directory_data()
    result = []
    for i in content:
        if i['Surname'] == value or i['Name'] == value:
            for val in i.values():
                result.append(val)
            return ', '.join(result)
    return 'Contact not found'


def search_number(value):
    if value.isnumeric():
        content = data.directory_data()
        result = []
        for i in content:
            if i['Number'] == value:
                for val in i.values():
                    result.append(val)
                return ', '.join(result)
        return 'Contact not found'
    else:
        return 'Invalid data format'
