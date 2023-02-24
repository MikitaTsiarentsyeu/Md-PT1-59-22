from django.shortcuts import render, HttpResponse
from .models import Oil, Post, Contact, Category
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    posts = Post.objects.all()
    oils = Oil.objects.all()
    cats = Category.objects.all()
    return render(request, 'app/home.html', {'posts':posts, 'oils':oils, 'cats':cats})

def about(request):
    return render(request, 'app/about.html')

def contacts(request):
    return render(request, 'app/contacts.html')

def motor (request):
    motor = Oil.objects.filter(category="1")
    return render (request, 'app/motor.html', {'motor':motor, 'category':1})

def hydraulic (request):
    hydraulic = Oil.objects.filter(category="2")
    return render (request, 'app/hydraulic.html', {'hydraulic':hydraulic})

def transmission (request):
    transmission = Oil.objects.filter(category="3")
    return render (request, 'app/transmission.html', {'transmission':transmission})

def grease (request):
    grease = Oil.objects.filter(category="4")
    return render (request, 'app/grease.html', {'grease':grease})

def oils (request): 
    oils = Oil.objects.all()
    return render(request, 'app/oils.html', {'oils':oils})

def oil (request, id):
    try:
        oil = Oil.objects.get(id=id)
    except:
        oil = False
    return render (request, 'app/oil.html', {'oil':oil, 'id':id})

def posts (request): 
    posts = Post.objects.all()
    return render(request, 'app/posts.html', {'posts':posts})

def post (request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        post = False
    return render (request, 'app/post.html', {'post':post, 'id':id}) 

class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        data = form.data
        subject = f'Form message from {data["name"]} Senders mail: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


def email(subject, data):
   send_mail(subject,
      data,
      'ciena777@mail.ru',
      ['ciena777@mail.ru']
   )

def success(request):
   return HttpResponse("<h>Letter sent!</h>")
