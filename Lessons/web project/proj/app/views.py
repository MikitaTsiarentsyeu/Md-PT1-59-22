from django.shortcuts import render, HttpResponse, redirect
import datetime
from .models import Author, Post
from .forms import AddPost, AddPostModelForm
from django.contrib.auth.decorators import permission_required


# Create your views here.
def home(request):
    current_time = datetime.datetime.now()
    return render(request, 'home.html', {'time':str(current_time)})

def posts(request):
    posts = Post.objects.all()
    viewed_posts = request.session.get('viewed_posts', [])
    return render(request, 'posts.html', {'posts':posts, 'viewed_posts': viewed_posts})

def post(request, id):
    try:
        p = Post.objects.get(id=id)
        viewed_posts = request.session.get('viewed_posts', [])
        if id not in viewed_posts:
            viewed_posts.append(id)
            request.session['viewed_posts'] = viewed_posts
    except:
        p = False
    return render(request, 'post.html', {'post':p, 'id':id})

def add(request):
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data["title"]
            post.subtitle = form.cleaned_data["subtitle"]
            post.content = form.cleaned_data["content"]
            post.post_type = form.cleaned_data["post_type"]
            post.image = form.cleaned_data["image"]
            post.issued = datetime.datetime.now()
            post.author = Author.objects.get(email=request.user.email)

            post.save()
            return redirect('posts')
    else:
        form = AddPost()
    return render(request, 'add.html', {'form':form})

@permission_required('app.add_post')
def add_model(request):
    if request.method == "POST":
        form = AddPostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.issued = datetime.datetime.now()
            post.author = Author.objects.get(email=request.user.email)

            post.save()
            return redirect('posts')
    else:
        form = AddPostModelForm(initial={'title':"test initial title"})
    return render(request, 'add.html', {'form':form})