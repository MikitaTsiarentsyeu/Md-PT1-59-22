"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views as app_views
from django.conf.urls.static import static
from django.conf import settings
from app.views import ContactCreate, success 


urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', app_views.home, name="home"),
    path('about/', app_views.about, name="about"),
    path('oils/', app_views.oils, name="oils"),
    path('oils/<int:id>', app_views.oil, name="oil"),
    path ('posts/', app_views.posts, name="posts"),
    path ('posts/<int:id>', app_views.post, name="post"),
    path('', ContactCreate.as_view(), name='contact_page'),
    path('success/', success, name='success_page'),
    path('motor/', app_views.motor, name="motor"),
    path('hydraulic/', app_views.hydraulic, name="hydraulic"),
    path('transmission/', app_views.transmission, name="transmission"),
    path('grease/', app_views.grease, name="grease"),
    path('contacts/', app_views.contacts, name="contacts")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
