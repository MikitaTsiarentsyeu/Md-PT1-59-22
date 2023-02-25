from django.contrib import admin

from .models import Author, Recipe, Ingredient, ProhibitedFoodstuff, Rating

admin.site.register(Author)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(ProhibitedFoodstuff)
admin.site.register(Rating)