import data

def add_schedule(name_schedule):
    value = data.add_schedule(name_schedule)
    if value:
        return f"The schedule has been added"
    else:
        return f"A schedule with this name has already been created"


def add_item(item, time, name_schedule):
    item1 = {"Item": item,"Time": time}
    value = data.add_item(item1, name_schedule)
    if value:
        return f"The item has been added"

def view_schedule(name_schedule):
    value = data.view_schedule(name_schedule)
    if value != False:
        return value
    else:
        return ["The book has not been found"]

def delete_item(name_schedule, theme):
    value = data.delete_item(name_schedule, theme)
    if isinstance(value, bool):
        if value == True:
            return f"The item has been removed "
        elif value == False:
            return f"The value has not been found"
    else:
        return f"The schedule has not been found"

def delete_schedule(name_schedule):
    value = data.delete_schedule(name_schedule)
    if value :
        return f"The schedule has been removed"
    else:
        return f"The schedule has not been found"

