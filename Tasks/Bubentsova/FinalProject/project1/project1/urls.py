"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasteandshare import views as tasteandshare_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', tasteandshare_views.home, name="home"),
    path('recipes/<int:id>', tasteandshare_views.recipe, name="recipe"),
    path('recipes/', tasteandshare_views.recipes, name="recipes"),
    path('recipes/add-recipe', tasteandshare_views.add_recipe, name="add-recipe"),
    path('search-recipes/', tasteandshare_views.search_recipes, name="search-recipes"),
    path('login/', tasteandshare_views.login, name="login"),
    path('edit-recipe/<int:id>', tasteandshare_views.edit_recipe, name="edit-recipe"),
    path('delete-recipe/<int:id>', tasteandshare_views.delete_recipe, name="delete-recipe"),
    path('rate-recipe/<int:id>', tasteandshare_views.add_rating_comment, name="rate-recipe"),
    path('add-edit-prohibited-foodstuffs/', tasteandshare_views.add_edit_prohibited_foodstuffs, name="add-edit-prohibited-foodstuffs"),
    path('add-edit-ingredients/<int:id>', tasteandshare_views.add_edit_ingredients, name="add-edit-ingredients"),
    path('salad', tasteandshare_views.get_salad, name="salad"),
    path('soup', tasteandshare_views.get_soup, name="soup"),
    path('hot-dish', tasteandshare_views.get_hot_dish, name="hot-dish"),
    path('dessert', tasteandshare_views.get_dessert, name="dessert"),
    path('pasta', tasteandshare_views.get_pasta, name="pasta"),
    path('pizza', tasteandshare_views.get_pizza, name="pizza"),
    path('rating/<int:id>', tasteandshare_views.rating_and_comments, name="rating"),
    path('account/', tasteandshare_views.account, name="account")

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)