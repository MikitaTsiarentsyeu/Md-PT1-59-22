import bl

menu = """
Menu:
1. Create a schedule for the day
2. Add an item to the schedule
3. View the schedule
4. Delete item in the schedule
5. Delete the schedule
6. Exit
Enter :
"""
def add_schedule():
    name_schedule = input("Enter the name of the schedule:\n")
    print(bl.add_schedule(name_schedule))

def add_item():
    item1 = input("Enter the item:\n").title()
    time = input("Enter the time of the item:\n").title()
    name_schedule = input("Enter the name of the schedule\n")
    print(bl.add_item(time, item1, name_schedule))

def view_schedule():
    name_schedule = input("Enter the name of the schedule:\n")
    for i in bl.view_schedule(name_schedule):
        if isinstance(i, dict):
            print(i["Time"], i["Item"]) 
        else:
            print(i)

def delete_item():
    name_schedule = input('Enter the name of the schedule for delete item\n')
    theme = input("Enter value for delete item\n")
    print(bl.delete_item(name_schedule, theme))

def delete_schedule():
    name_schedule = input("Enter the name of the schedule\n")
    print(bl.delete_schedule(name_schedule))

def main_cycle():
    while True:
        print(menu)
        choice = input()
        if choice == '1':
            add_schedule()
        elif choice == '2':
            add_item()
        elif choice == '3':
            view_schedule()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            delete_schedule()
        elif choice == '6':
            print("Stop")
            break
        else:
            print("not valida menu point, try again")


main_cycle()
