import os
import json

def data():
    with open('data.json') as f:
        recipes = json.load(f)
        return recipes


def write_data(recipes):
     with open('data.json', 'w') as f:
        return json.dump(recipes, f)


def prohibited_foodstuff_data():
    with open('prohibited_foodstuff.json') as f:
        pr_fsts = json.load(f)
        return pr_fsts


def add_recipe(recipe_name, ingrs, ingrs_amount, prepr):
    recipes = {}
    descr = {}
    descr = dict(zip(ingrs, ingrs_amount))
    descr["Preparation"] = prepr
    recipes[recipe_name] = descr
    if os.path.exists('data.json'):
        recipes_existing = data()
        recipes_existing.update(recipes)
        recipes = recipes_existing
    write_data(recipes)
    return recipes


def add_prohibited_foodstuff(name, reason):
    pr_fsts = {}
    pr_fsts[name] = (reason)
    if os.path.exists('prohibited_foodstuff.json'):
        pr_fsts_existing = prohibited_foodstuff_data()
        pr_fsts_existing.update(pr_fsts)
        pr_fsts = pr_fsts_existing
    with open('prohibited_foodstuff.json', 'w') as f:
        json.dump(pr_fsts, f)
    return pr_fsts


def get_recipe_by_name(name):
    recipes = data()
    recipe = ""
    for i in recipes:
        if name in i:
            recipe = recipes[name]
    return recipe


def update_recipe_name(name, name_new):
    recipes = data()
    if name in recipes:
        recipe_updated = {}
        descr = recipes[name]
        del recipes[name]
        recipe_updated[name_new] = descr
        recipes.update(recipe_updated)
        write_data(recipes)
    else:
        recipes = ""
    return recipes


def update_recipe(name, ingr_name, ingr_amount_new):
    recipes = data()
    if name in recipes:
        recipe_dict = recipes[name]
        recipe_dict[ingr_name] = ingr_amount_new
        write_data(recipes)
    else:
        recipes = ""
    return recipes


def delete_recipe(name):
    recipes = data()
    if name in recipes:
        del recipes[name]
        write_data(recipes)
    else:
        recipes = ""
    return recipes


def rate_recipe(name, rate):
    recipes = data()
    if name in recipes:
        recipe_dict = recipes[name]
        recipe_dict["Rating"] = rate
        write_data(recipes)
    else:
        recipes = ""
    return recipes


def add_ingredient(name, new_ingr, ingr_amount):
    recipes = data()
    if name in recipes:
        recipe_dict = recipes[name]
        recipe_list = list(recipe_dict.items())
        recipe_list.insert(0, (new_ingr, ingr_amount))
        recipe_dict = dict(recipe_list)
        recipes[name] = recipe_dict
        write_data(recipes)
    else:
        recipes = ""
    return recipes


# if __name__ == "__main__":
    # print(add_recipe("Salad", ["Cucumber", "Tomato", "Avocado"], ["3", "2", "1"], "Some preparation steps"))
    # print(add_recipe("Ice cream", ["Milk"], ["1 liter"], "Steps to prepare ice cream"))
    # print(data())
    # print(add_prohibited_foodstuff("Peanut", "Allergy"))
    # print(prohibited_foodstuff_data())
    # print(get_recipe_by_name("Salad"))
    # print(update_recipe_name("Salad", "Avocado salad"))
    # print(update_recipe("Avocado salad", "Avocado", "2"))
    # print(delete_recipe("Avocado salad"))
    # print(rate_recipe("Ice cream", "5"))
    # print(add_ingredient("Ice cream", "Sugar", "2 teaspoons"))