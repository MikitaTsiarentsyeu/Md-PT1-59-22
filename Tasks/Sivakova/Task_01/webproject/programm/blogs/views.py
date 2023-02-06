from django.shortcuts import HttpResponse, render, redirect
from .models import Articles, Visitors, Comments, Doctors
from .forms import ArticlesForm, VisitorsForm, VisitorsForm01, VisitorsForm02, VisitorsForm03, VisitorsForm04, CommentsForm

# Create your views here.
def blogs_home(request):
    blogs = Articles.objects.all()
    return render(request, 'blogs/blogs_home.html', {'blogs':blogs})

def doctors(request):
    doctors = Doctors.objects.all()
    return render(request, 'blogs/doctors.html', {'doctors':doctors})

def visitors_home(request):
    visit = Visitors.objects.all()
    return render(request, 'blogs/visitor_home.html', {'visit':visit})

def visitorstartpage (request):
    return render(request, 'main/startpage.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form =  ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs_home')
        else:
            error = 'Что-то пошло не так...'
        
    form = ArticlesForm()
    data = {
        'form':form,
        'error': error
        }
    return render(request, 'blogs/create.html', data)

def about(request):
    visit = Comments.objects.all()
    return render(request, 'blogs/about.html', {'visit':visit})

def comments(request):
    error = ''
    if request.method == 'POST':
        c_form =  CommentsForm(request.POST)
        if c_form.is_valid():

       
            c_form.save()
            
            return redirect('added')
        else:
            error = 'Что-то пошло не так...'
            
        
    c_form = CommentsForm()
    data3 = {'c_form':c_form, 
             'error': error}
    return render(request, 'blogs/comments.html', data3)




def createvisitor(request):
    error = ''
    if request.method == 'POST':
        v_form =  VisitorsForm(request.POST)
        
        if v_form.is_valid():

       
            v_form.save()
            
            return redirect('visitor')
        else:
            error = 'Что-то пошло не так...'
            
        
    v_form = VisitorsForm()
    data2 = {'v_form':v_form, 
             'error': error}
    return render(request, 'blogs/create_visitor.html', data2)




def createvisitor01(request):
    error = ''
    if request.method == 'POST':
        v_form =  VisitorsForm01(request.POST)
        if v_form.is_valid():

       
            v_form.save()
            
            return redirect('visitor')
        else:
            error = 'Что-то пошло не так...'
            
        
    v_form = VisitorsForm01()
    data2 = {'v_form':v_form, 
             'error': error}
    return render(request, 'blogs/create_visitor.html', data2)



def createvisitor02(request):
    error = ''
    if request.method == 'POST':
        v_form =  VisitorsForm02(request.POST)
        if v_form.is_valid():

       
            v_form.save()
            
            return redirect('visitor')
        else:
            error = 'Что-то пошло не так...'
            
        
    v_form = VisitorsForm02()
    data2 = {'v_form':v_form, 
             'error': error}
    return render(request, 'blogs/create_visitor.html', data2)





def createvisitor03(request):
    error = ''
    if request.method == 'POST':
        v_form =  VisitorsForm03(request.POST)
        if v_form.is_valid():

       
            v_form.save()
            
            return redirect('visitor')
        else:
            error = 'Что-то пошло не так...'
            
        
    v_form = VisitorsForm03()
    data2 = {'v_form':v_form, 
             'error': error}
    return render(request, 'blogs/create_visitor.html', data2)




def createvisitor04(request):
    error = ''
    if request.method == 'POST':
        v_form =  VisitorsForm04(request.POST)
        if v_form.is_valid():

       
            v_form.save()
            
            return redirect('visitor')
        else:
            error = 'Что-то пошло не так...'
            
        
    v_form = VisitorsForm04()
    data2 = {'v_form':v_form, 
             'error': error}
    return render(request, 'blogs/create_visitor.html', data2)

