from django.shortcuts import render, redirect
import datetime
from .models import Author, Post
from .forms import AddPost
# from .forms import AddPost, AddPostModelForm
from django.contrib.auth.decorators import permission_required
# Create your views here.
def home(request):
    current_time= datetime.datetime.now()
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
@permission_required('first.add_post')
def add(request):
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.issued = datetime.datetime.now()
            post.author = Author.objects.get(email=request.user.email)

            post.save()
            return redirect('posts')
    else:
        form = AddPost()
    return render(request, 'add.html', {'form':form})