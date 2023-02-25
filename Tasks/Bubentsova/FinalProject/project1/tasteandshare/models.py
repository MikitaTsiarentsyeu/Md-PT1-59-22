from django.db import models


class Author(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads', blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    RECIPE_TYPES = [('sl', "Salad"), ('sp', "Soup"), ('hd', "Hot dish"), ('ds', "Dessert"), ('ps', "Pasta"), ('pz', "Pizza")]

    recipe_name = models.CharField(max_length=100, unique=True, verbose_name="Recipe name")
    recipe_type = models.CharField(choices=RECIPE_TYPES, max_length=10, verbose_name="Recipe type")
    calories = models.CharField(max_length=30, verbose_name="Calories")
    time = models.CharField(max_length=4, verbose_name="Time")
    preparation = models.TextField()
    image = models.ImageField(upload_to='uploads', blank=True)
    issued = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name


class Ingredient(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Name")
    amount = models.CharField(max_length=50, verbose_name="Amount")
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProhibitedFoodstuff(models.Model):

    name = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Rating(models.Model):

    value = models.IntegerField()
    comment = models.TextField()
    issued = models.DateField()
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)