from django.shortcuts import render, redirect
from .models import Author, Recipe, Ingredient, ProhibitedFoodstuff
from .forms import RecipeForm, RatingForm
import datetime
from django.http import HttpResponseNotFound
from django.forms import inlineformset_factory
from .bl import *


def home(request):
    return render(request, 'home.html')


def recipe(request, id):
    try:
        recipe = Recipe.objects.get(id = id)
        ingredients = recipe.ingredient_set.all()
        ratings = recipe.rating_set.all()
        rating_count = recipe.rating_set.count()
        if ratings:
            rating_av = rating(ratings)
        else: rating_av = 0
        context = {'recipe':recipe, 'ingredients':ingredients, 'ratings':ratings, 'rating_count':rating_count, 'rating_av':rating_av}
    except:
        recipe = False
    return render(request, 'recipe.html', context) 


def recipes(request):
    recipes = Recipe.objects.all()
    res = recipes_wo_pfts(recipes)
    return render(request, 'recipes.html', {'recipes':res})


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.issued = datetime.datetime.now()
            recipe.author = Author.objects.get(email=request.user.email)

            recipe.save()
            return redirect('recipe', recipe.id)
    else: 
        form = RecipeForm()
    return render(request, 'add_edit_recipe.html', {'form':form})


def add_edit_ingredients(request, id):
    IngredientFormSet = inlineformset_factory(Recipe, Ingredient, fields=('name', 'amount'), extra=3)
    recipe = Recipe.objects.get(id=id)
    formset = IngredientFormSet(instance=recipe)
   
    if request.method == "POST":
        formset = IngredientFormSet(request.POST, instance=recipe)
        if formset.is_valid():
            formset.save()
            return redirect('recipe', recipe.id)

    context = {'formset':formset}
    return render(request, 'add_edit_ingredients.html', context)


def edit_recipe(request, id):
    try:
        recipe = Recipe.objects.get(id=id)
        form = RecipeForm(instance=recipe)

        if request.method == "POST":
            form = RecipeForm(request.POST, instance=recipe)
            if form.is_valid():
                
                form.save()
                return redirect('recipe', recipe.id)
        context = { 'form': form }
        return render(request, 'add_edit_recipe.html', context)
    except Recipe.DoesNotExist:
        return HttpResponseNotFound("<h2>Recipe not found</h2>")
    

def delete_recipe(request, id):
    try:
        recipe = Recipe.objects.get(id=id)
        if request.method == "POST":
            recipe.delete()
            return redirect('recipes')
        context = {'recipe': recipe}
        return render(request, 'delete_recipe.html', context)
    except:
        return HttpResponseNotFound("<h2>Recipe not found</h2>")


def add_edit_prohibited_foodstuffs(request):
    ProhibitedFoodstuffFormSet = inlineformset_factory(Author, ProhibitedFoodstuff, fields=('name', 'reason'), extra=2)
    author = Author.objects.get(email=request.user.email)
    formset = ProhibitedFoodstuffFormSet(instance=author)
   
    if request.method == "POST":
        formset = ProhibitedFoodstuffFormSet(request.POST, instance=author)
        if formset.is_valid():
            formset.save()
            return redirect('account')

    context = {'formset':formset}
    return render(request, 'add_edit_prohibited_foodstuffs.html', context)


def search_recipes(request):
    if request.method == "POST":
        searched = request.POST['searched']
        recipes = Recipe.objects.filter(recipe_name__contains=searched)
        return render(request, 'search_recipes.html', {'searched':searched, 'recipes':recipes})
    else:
        return render(request, 'search_recipes.html', {'searched':searched})
        

def add_rating_comment(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.issued = datetime.datetime.now()
            rating.recipe = Recipe.objects.get(id=id)
            rating.author = Author.objects.get(email=request.user.email)

            rating.save()
            return redirect('recipe', recipe.id)
    else: 
        form = RatingForm()
    return render(request, 'add_rating_and_comments.html', {'form':form, 'recipe':recipe})


def rating_and_comments(request, id):
    try:
        recipe = Recipe.objects.get(id = id)
        ratings = recipe.rating_set.all()
        context = {'recipe':recipe, 'ratings':ratings}
    except:
        recipe = False
    return render(request, 'rating_and_comments.html', context) 


def get_salad(request):
    recipes = Recipe.objects.filter(recipe_type ='sl')
    res = recipes_wo_pfts(recipes)
    return render(request, 'recipes.html', {'recipes':res})


def get_soup(request):
    recipes = Recipe.objects.filter(recipe_type ='sp')
    res = recipes_wo_pfts(recipes)
    return render(request, 'recipes.html', {'recipes':res})


def get_hot_dish(request):
    recipes = Recipe.objects.filter(recipe_type ='hd')
    res = recipes_wo_pfts(recipes)
    return render(request, 'recipes.html', {'recipes':res})


def get_dessert(request):
    recipes = Recipe.objects.filter(recipe_type ='ds')
    res = recipes_wo_pfts(recipes)
    return render(request, 'recipes.html', {'recipes':res})


def get_pasta(request):
    recipes = Recipe.objects.filter(recipe_type ='ps')
    res = recipes_wo_pfts(recipes)
    return render(request, 'recipes.html', {'recipes':res})


def get_pizza(request):
    recipes = Recipe.objects.filter(recipe_type ='pz')
    res = recipes_wo_pfts(recipes)
    return render(request, 'recipes.html', {'recipes':res})


def account(request):
    author = Author.objects.get(email=request.user.email)
    prohibitedFoodstuffs = author.prohibitedfoodstuff_set.all()
    context = {'author':author, 'prohibitedFoodstuffs':prohibitedFoodstuffs}     
    return render(request, 'account.html', context)


def login(request):
    return render(request, 'login.html')