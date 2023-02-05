import bl

menu = """
1. Add recipe
2. Add prohibited foodstuff (recipes which contain it will not be displayed in the returned recipes list)
3. Get all recipes
4. Get recipe by name
5. Update recipe name
6. Update amount of some recipe ingredient
7. Delete recipe
8. Rate the recipe
9. Add ingredient
"""

def add_recipe():
    while True:
        recipe_name = input("Enter recipe name:\n")
        prepr = input("Enter preparation steps:\n")
        ingrs_number = int(input("Enter number of ingredients:\n"))
        ingrs = []
        ingrs_amount = []
        i = 0
        while i < ingrs_number:
            ingr = input("Enter name of ingredient:\n")
            amount = input("Enter amount:\n")
            ingrs.append(ingr)
            ingrs_amount.append(amount)
            i += 1
        recipes = bl.add_recipe(recipe_name, ingrs, ingrs_amount, prepr)
        if input("Add one more recipe:\n") == "+":
            continue
        else:
            break
    return print(recipes)  


def add_prohibited_foodstuff():
    while True:
        name = input("Enter the foodstuff which should not be used in the recipe:\n")
        reason = input("Enter the reason:\n")
        pr_fst = bl.add_prohibited_foodstuff(name, reason)
        if input("Add one more:\n") == "+":
            continue
        else:
            break
    return print(pr_fst)


def get_all_recipes():
    return print(f"The list of recipes:\n{bl.get_all_recipes()}")


def get_recipe_by_name():
    name = input("Enter name of the recipe to be find:\n")
    print(bl.get_recipe_by_name(name))


def update_recipe_name():
    name = input("Enter the recipe name to be updated:\n")
    name_new = input("Enter new recipe name:\n")
    return print(bl.update_recipe_name(name, name_new))


# Note: if entered ingredient does not exist in data it will be added
def update_recipe():
    name = input("Enter the recipe name which ingredient amount you would like to update:\n")
    ingr_name = input("Eter ingredient name:\n")
    ingr_amount_new = input("Enter new amount:\n")
    return print(bl.update_recipe(name, ingr_name, ingr_amount_new))


def delete_recipe():
    name = input("Enter the name of the recipe to be deleted:\n")
    return print(bl.delete_recipe(name))


def rate_recipe():
    name = input("Enter recipe name to rate it:\n")
    rate = input("Enter recipe rate from 1 to 5:\n")
    return print(bl.rate_recipe(name, rate))


def add_ingredient():
    name = input("Enter name of the recipe to add ingredient to it:\n")
    new_ingr = input("Enter name of the new ingredient:\n")
    ingr_amount = input("Enter amount:\n")
    return print(bl.add_ingredient(name, new_ingr, ingr_amount))


def main_cycle():
    while True:
        print("Please choose a point from the below menu:")
        print(menu)
        choice = input()
        if choice == '1':
            add_recipe()
        elif choice == '2':
            add_prohibited_foodstuff()
        elif choice == '3':
            get_all_recipes()
        elif choice == '4':
            get_recipe_by_name()
        elif choice == '5':
            update_recipe_name()
        elif choice == '6':
            update_recipe()
        elif choice == '7':
            delete_recipe()
        elif choice == '8':
            rate_recipe()
        elif choice == '9':
            add_ingredient()
        else:
            print("Such menu point does not exist. Please select another one")

main_cycle()