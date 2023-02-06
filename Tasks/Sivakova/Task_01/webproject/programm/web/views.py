from django.shortcuts import render, HttpResponse, redirect
import datetime
from .models import Author, Post
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .forms import  AddPostModelForm
# Create your views here.
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class DTForm(forms.Form):
    name =  forms.CharField(max_length=100)
    content = forms.Textarea()
    date =forms.DateField(widget=AdminDateWidget)
    time =forms.TimeField(widget=AdminTimeWidget)

def home(request):
    current_time = datetime.datetime.now()
    return render(request, 'web/menu.html', {'time':str(current_time)})

def home(request):
    current_time = datetime.datetime.now()
    return render(request, 'web/home.html', {'time':str(current_time)})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'web/posts.html', {'posts':posts})


def post(request, id):
    try:
        p = Post.objects.get(id=id)
    except:
        p = False
    return render(request, 'web/post.html', {'post':p, 'id':id})


def add_model(request):
    if request.method == "POST":
        form = AddPostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.issued = datetime.datetime.now()
            post.author = Author.objects.all()[0]

            post.save()
            return redirect('posts')
    else:
        form = AddPostModelForm()
    return render(request, 'web/index.html', {'form':form})
