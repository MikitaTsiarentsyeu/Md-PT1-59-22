from django.shortcuts import render, HttpResponse, redirect
import datetime
from .models import Author, Post
from .forms import AddPost, AddPostModelForm
from django.contrib.auth.decorators import permission_required
from django.views import View

# Create your views here.
# def home(request):
#     current_time = datetime.datetime.now()
#     return render(request, 'home.html', {'time':str(current_time)})

class PostModelViewBase:

    model = Post
    
    def get_all_posts(self):
        return self.model.objects.all()

    def get_post(self, id):
        try:
            return self.model.objects.get(id=id) 
        except:
            return False

    def add_post(self, form, author):
        try:
            post = self.model()
            post.title = form.cleaned_data["title"]
            post.subtitle = form.cleaned_data["subtitle"]
            post.content = form.cleaned_data["content"]
            post.post_type = form.cleaned_data["post_type"]
            post.image = form.cleaned_data["image"]
            post.issued = datetime.datetime.now()
            post.author = author

            post.save()
            return True
        except:
            return False

class PostSessionViewBase:

    session_key = 'viewed_posts'

    def get_post_id_from_session(self, request):
        return request.session.get(self.session_key, [])

    def set_post_post_id_for_session(self, request, id):
        viewed_posts = request.session.get(self.session_key, [])
        if id not in viewed_posts:
            viewed_posts.append(id)
            request.session[self.session_key] = viewed_posts

class PostsView(PostModelViewBase, PostSessionViewBase, View):

    template = 'posts.html'

    def get(self, request):
        posts = self.get_all_posts()
        viewed_posts = self.get_post_id_from_session(request)
        return render(request, self.template, {'posts':posts, 'viewed_posts': viewed_posts})

# def posts(request):
#     posts = Post.objects.all()
#     viewed_posts = request.session.get('viewed_posts', [])
#     return render(request, 'posts.html', {'posts':posts, 'viewed_posts': viewed_posts})

class PostView(PostModelViewBase, PostSessionViewBase, View):

    template = 'post.html'

    def get(self, request, id):
        p = self.get_post(id)
        if p:
            self.set_post_post_id_for_session(request, id)

        return render(request, self.template, {'post':p, 'id':id})


# def post(request, id):
#     try:
#         p = Post.objects.get(id=id)
#         viewed_posts = request.session.get('viewed_posts', [])
#         if id not in viewed_posts:
#             viewed_posts.append(id)
#             request.session['viewed_posts'] = viewed_posts
#     except:
#         p = False
#     return render(request, 'post.html', {'post':p, 'id':id})

class AddPostView(PostModelViewBase, View):

    form = AddPost
    template = 'add.html'

    def get(self, request):
        form = self.form()
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            author = Author.objects.get(email=request.user.email)
            if self.add_post(form, author):
                return redirect('posts')

        return render(request, self.template, {'form':form})

# def add(request):
#     if request.method == "POST":
#         form = AddPost(request.POST, request.FILES)
#         if form.is_valid():
#             post = Post()
#             post.title = form.cleaned_data["title"]
#             post.subtitle = form.cleaned_data["subtitle"]
#             post.content = form.cleaned_data["content"]
#             post.post_type = form.cleaned_data["post_type"]
#             post.image = form.cleaned_data["image"]
#             post.issued = datetime.datetime.now()
#             post.author = Author.objects.get(email=request.user.email)

#             post.save()
#             return redirect('posts')
#     else:
#         form = AddPost()
#     return render(request, 'add.html', {'form':form})

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