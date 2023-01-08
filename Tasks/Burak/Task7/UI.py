import BL

menu = """
0. EXIT
1. I want to sell my car
2. Let me watch all cars
3. Find a car
4. I want to remove the ad
"""


def addcar():
    mark, model, year, engine_displacement, fuel_type, mileage, gear, location, price = \
        input("What is the mark of your car?\n"), input("What is the model of your car?\n"), \
        input("What is the year of your car's first registration?\n"), input("What is your car's engine displacement?\n"), \
        input("What is the type of fuel?\n"), input("What is the mileage on your car?\n"), \
        input("What gearbox is in your car?\n"), input("Where the car is located?\n"), \
        input("How much do you want to sell your car for?\n")
    print(BL.addcarad(mark, model, year, engine_displacement, fuel_type, mileage, gear, location, price))

def watchallcars():
    print(BL.watchallcars())

def search():
    print(BL.search(input()))

def removead():
    request = input('Remind me of some of the characteristics of your car:\n')
    print(BL.remove(request))


def main_cycle():
    while True:
        print("Let's define what you want to do")
        print(menu)
        choice = input()
        if choice == '0':
           break
        if choice == '1':
            addcar()
        elif choice == '2':
            watchallcars()
        elif choice == '3':
            search()
        elif choice == '4':
            removead()
        else:
            print("not valida menu point, try again")


main_cycle()
