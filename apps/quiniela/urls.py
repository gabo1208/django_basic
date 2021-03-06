# -*- coding: utf-8 -*-
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'quiniela'
urlpatterns = [
    # Quiniela related views
    re_path('^$', views.quiniela_index, name='user_quinielas'),
    path('<int:quiniela_id>', views.quiniela_details, name='quiniela_details'),
    path('<int:quiniela_id>/join', views.quiniela_join, name='quiniela_join'),
    path('<int:quiniela_id>/delete', views.quiniela_delete, name='quiniela_delete'),
    path('<int:quiniela_id>/@<str:username>', views.quiniela_from_user, name='quiniela_from_user'),
    # Oscarcoin
    path('oscarcoin/', views.oscarcoin_update, name='oscarcoin_uptade'),
]
