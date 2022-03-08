import imp
from typing import ValuesView
from django.urls import path
from django.views import View
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
