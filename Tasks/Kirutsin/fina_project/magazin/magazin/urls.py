"""magazin URL Configuration

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
from main_site import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('title/', main_views.view_all_content, name="title"),
    path('title/<str:id>', main_views.view_content_by_id, name="product_info"),
    path('bascet/', main_views.bascet, name="basket_view"),
    path('bascet/add/<str:id>', main_views.add, name="add_product_basket"),
    path('bascet/del/<str:id>', main_views.del_product, name="del_product_basket"),
    path('back_office/', main_views.back_office, name='user_bo'),
    path('accounts/', include('django.contrib.auth.urls'))
]
