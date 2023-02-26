from django.shortcuts import render, redirect
from .models import Catalog, Products, Bascet


# Create your views here.
def view_all_content(request):
    catalog_list = Catalog.objects.all()
    content = Products.objects.all()
    return render(request, 'base_templates/base_title.html', {'catalog': catalog_list, 'content': content})


def view_content_by_id(request, id):
    catalog_list = Catalog.objects.all()
    content = catalog_list.filter(catalog_name=f'{id}')[0].id
    result = Products.objects.all().filter(product_type=content)
    return render(request, 'base_templates/base_title.html', {'catalog': catalog_list, 'content': result})


def add(request, id):
    if request.user.is_authenticated:
        product_info = Products.objects.filter(name=id)[0]
        Bascet.objects.create(name=product_info, description=product_info.description, currency=product_info.currency,
                              price=product_info.price, user=request.user)
        return redirect('title')
    else:
        return render(request, 'registration/login.html')


def del_product(request, id):
    if request.user.is_authenticated:
        Bascet.objects.filter(id=id).delete()
        return redirect('basket_view')
    else:
        return render(request, 'registration/login.html')


def bascet(request):
    if request.user.is_authenticated:
        bascet_select = Bascet.objects.filter(user=request.user)
        return render(request, 'base_templates/base_bascet.html', {"Bascet": bascet_select})
    else:
        return render(request, 'registration/login.html')


def back_office(request):
    if request.user.is_authenticated:
        username = request.user
        return render(request, 'base_templates/base_back_office.html', {'username': username})
    else:
        return render(request, 'registration/login.html')
