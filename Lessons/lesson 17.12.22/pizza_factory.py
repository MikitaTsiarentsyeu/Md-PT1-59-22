def prepare():
    print("STARTING A NEW PIZZA-MAKING PROCESS")
    print("preparing a base")
    print("choosing a sauce")

def add_ingridient(ingridient):
    print(f"adding {ingridient}")

def grind_cheese():
    print("grinding some cheese")

def bake(temp, duration):
    print(f"baking for {duration} at {temp}")

def box():
    print("boxing")
    print("slicing")
    print("DONE!")

# def make_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake(250, 3)
#     box()

# def make_gawaii():
#     prepare()
#     add_ingridient("shrimp")
#     add_ingridient("pineaple")
#     grind_cheese()
#     bake(200, 4)
#     box()

# def make_chili():
#     prepare()
#     add_ingridient("chili")
#     add_ingridient("green mess")
#     grind_cheese()
#     bake(180, 5)
#     box()


def pizza_factory(ingridients, temp, duration):
    def action():
        prepare()
        for i in ingridients:
            add_ingridient(i)
        grind_cheese()
        bake(temp, duration)
        box()
    return action

make_pepperoni = pizza_factory(["pepperoni"], 250, 3)
make_gawaii = pizza_factory(["shrimp", "pineaple"], 200, 4)
make_chili = pizza_factory(["chili", "brokolly"], 180, 5)

make_gawaii()
make_pepperoni()
make_chili()