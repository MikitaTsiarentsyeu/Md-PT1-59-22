from django.urls import path
from . import views



from django.conf import settings


   
urlpatterns = [
   
    path('', views.blogs_home, name='blogs_home'),
    path('doctors', views.doctors, name='doctors'),
    path('visitor', views.visitors_home, name='visitor'),
    path('visitorstartpage', views.visitorstartpage, name='visitorstartpage'),
    path('create', views.create, name='blogs_create'),
    path('createvisitor', views.createvisitor, name='create_visitor'),
     path('createvisitor01', views.createvisitor01, name='create_visitor01'),
     path('createvisitor02', views.createvisitor02, name='create_visitor02'),
      path('createvisitor03', views.createvisitor03, name='create_visitor03'),
       path('createvisitor04', views.createvisitor04, name='create_visitor04'),
       path('comments', views.comments, name='comments'),
       path('added', views.about, name='added')
       
   
    
    
       
]