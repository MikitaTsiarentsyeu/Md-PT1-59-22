from django.urls import path
from . import views


urlpatterns = [
    path('add/<product_id>)', views.cart_add),
]