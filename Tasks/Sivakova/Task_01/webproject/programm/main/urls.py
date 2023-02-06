from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('startpage', views.main, name = 'start'),
   
    

    ]
