from .models import  ProhibitedFoodstuff


def rating(ratings):
    value_list = []
    for r in ratings:
        value = getattr(r, 'value')
        value_list.append(value)
    rating_len = len(value_list)
    rating_av = round(sum(value_list)/rating_len)
    return rating_av


def recipes_wo_pfts(recipes):
    pr_fsts = ProhibitedFoodstuff.objects.all()
    pr_fsts_list = []
    recipes_list = []

    for r in recipes:
        recipes_list.append(r)

    for p in pr_fsts:
        pr_fsts_list.append(p)

    r_pr_fsts = [r for r in recipes_list if r.ingredient_set.filter(name__in = pr_fsts_list)]
    for r in r_pr_fsts:
        recipes_list.remove(r)
    return recipes_list