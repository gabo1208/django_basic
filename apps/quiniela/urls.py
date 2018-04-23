# -*- coding: utf-8 -*-
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'quiniela'
urlpatterns = [
    # Quiniela related views
    path('', views.quiniela_index, name='quiniela_index'),
]
