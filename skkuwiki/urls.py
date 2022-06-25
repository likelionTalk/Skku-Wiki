# skkuwiki URL Configuration

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('posts/', include('posts.urls')),
    path('account/', include('account.urls')),
]
