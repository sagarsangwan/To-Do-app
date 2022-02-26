from . import views
from django.urls import URLPattern, path

URLPattern = [
    path('', views.home, name='home')
]
