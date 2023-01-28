from django.shortcuts import render, HttpResponse
import datetime
from .models import Author, Post

# Create your views here.
def home(request):
    current_time = datetime.datetime.now()
    return render(request, 'home.html', {'time':str(current_time)})

def posts(request):
    count = Post.objects.all().count()
    return HttpResponse(f"<h1>Total posts count is {count}</h1>")

def post(request, id):
    try:
        p = Post.objects.get(id=id)
        res = f"<h1>{p.title}</h1><h3>{p.subtitle}</h3><p>{p.content}</p>"
    except:
        res = f"<h1>Nothing was found</h1>"
    return HttpResponse(res)