from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    current_time = datetime.datetime.now()
    return render(request, 'home.html', {'time':str(current_time)})