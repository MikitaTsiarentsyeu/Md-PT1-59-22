import data

def add_recipe(recipe_name, ingrs, ingrs_amount, prepr):
    data.add_recipe(recipe_name, ingrs, ingrs_amount, prepr)
    return f"The recipe(s) added successfully"


def add_prohibited_foodstuff(name, reason):
    data.add_prohibited_foodstuff(name, reason)
    return f"The prohibited foodstuff(s) added"

# Note: result returned from the data should be displayed as a string, some converting is required here,
# that is why it is done on the bl side
def recipes_wo_pr_fsts():
    recipes = data.data()
    prohibited_foodstuffs = data.prohibited_foodstuff_data()
    pr_fsts = []
    recipes_list = []
    for name in recipes:
        recipe_dict = recipes[name]
        recipe_descr = ', '.join(key + ": " + value for key, value in recipe_dict.items())
        recipe = f"{name}:\n {recipe_descr}"
        recipes_list.append(recipe)
    for pf in prohibited_foodstuffs:
        pr_fsts.append(pf)
    recipes_with_pr_fsts = [x for y in pr_fsts for x in recipes_list if y in x]
    for r in recipes_with_pr_fsts:
        recipes_list.remove(r)
    return recipes_list


def get_all_recipes():
    recipes = recipes_wo_pr_fsts()
    res = ""
    if len(recipes) > 0:
        for i, r in enumerate(recipes, 1):
            res = f"{res}\n{i}. {r}\n"
    return res if res else "Recipes have not been added yet"

# Note: there is no validation regarding prohibited foodstuffs
def get_recipe_by_name(name):
    recipe = data.get_recipe_by_name(name)
    recipe_descr = ', '.join(key + ": " + value for key, value in recipe.items()) if recipe else "Recipe was not found"
    return f"{name}:\n {recipe_descr}"


def answer(name):
    answer = f"Recipe with {name} name does not exist. Please enter another name"
    return answer


def update_recipe_name(name, name_new):
    res = data.update_recipe_name(name, name_new)
    return f"The {name} recipe was changed to the {name_new}" if res else answer(name)
     

def update_recipe(name, ingr_name, ingr_amount_new):
    res = data.update_recipe(name, ingr_name, ingr_amount_new)
    return f"The {name} recipe was updated successfully" if res else answer(name)

 
def delete_recipe(name):
    res = data.delete_recipe(name)
    return f"The {name} recipe was deleted" if res else answer(name)


def rate_recipe(name, rate):
    res = data.rate_recipe(name, rate)
    return f"The {name} recipe was rated with {rate} star(s)" if res else answer(name)


def add_ingredient(name, new_ingr, ingr_amount):
    res = data.add_ingredient(name, new_ingr, ingr_amount)
    return f"{new_ingr} ingredient was added to the {name} recipe" if res else answer(name)


# if __name__ == "__main__":
#     print(add_recipe("Salad", ["Cucumber", "Tomato", "Avocado"], ["3", "2", "1"], "Some preparation steps"))
#     print(add_recipe("Ice cream", ["Milk"], ["1 liter"], "Steps to prepare ice cream"))
#     print(add_prohibited_foodstuff("Peanut", "Allergy"))
#     print(recipes_wo_pr_fsts())
#     print(get_all_recipes())
#     print(get_recipe_by_name("Biscuit"))
#     print(get_recipe_by_name("Borsch"))
#     print(get_recipe_by_name("Ice cream"))
#     print(update_recipe_name("Salad", "Avocado salad"))
#     print(update_recipe_name("Hash browns", "Pancakes"))
#     print(update_recipe("Avocado salad", "Avocado", "2"))
#     print(update_recipe("Pancakes", "Milk", "2 l."))
#     print(delete_recipe("Avocado salad"))
#     print(delete_recipe("Pancakes"))
#     print(rate_recipe("Ice cream", "4"))
#     print(rate_recipe("Pancakes", "5"))
#     print(add_ingredient("Ice cream", "Sugar", "2 teaspoons"))
#     print(add_ingredient("Сake", "Sugar", "4 teaspoons"))