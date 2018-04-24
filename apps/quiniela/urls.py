# -*- coding: utf-8 -*-
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'quiniela'
urlpatterns = [
    # Quiniela related views
    re_path('^$', views.quiniela_index, name='users_quinielas'),
    path('<int:quiniela_id>', views.quiniela_details, name='quiniela_details'),
]
