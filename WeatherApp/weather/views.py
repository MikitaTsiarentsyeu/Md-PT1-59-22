from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1a28208731e07aec35dc3883f8cfe5e7'
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'humidity': res["main"]["humidity"],
            'pressure': res["main"]["pressure"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
