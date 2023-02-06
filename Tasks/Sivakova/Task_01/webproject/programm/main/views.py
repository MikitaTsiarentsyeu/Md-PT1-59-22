from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render (request, 'main/layout.html')
def main(request):
    return render (request, 'main/startpage.html')


def visitor(request):
    return render(request, 'main/bla.html')
