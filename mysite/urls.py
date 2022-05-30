"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
import views

urlpatterns = [
    path('admin/', admin.site.urls),
      
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.index),
    path('aboutUs.html', views.aboutUs),
    path('gallery.html', views.gallery),
    path('index.html', views.index),
    path('login.html', views.login),
    path('likes/', include('likes.urls', namespace='likes')),
    path('likes/aboutUs.html', views.aboutUs),
    path('likes/gallery.html', views.gallery),
    path('likes/index.html', views.index),
    path('likes/login.html', views.login) 
)