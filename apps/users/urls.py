# -*- coding: utf-8 -*-
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    # User registration and authentication views
    re_path('^login/$', views.user_login, name='login'),
    re_path('^logout/$',auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    re_path('^sign_up/$', views.sign_up, name='user_sign_up'),

    # User related views
    #re_path('^$', views.user_index, name='user_index'),

    # Social related views
    #path('profiles/@<str:username>', views.user_profile, name='user_profile'),

    # Include user member-its urls
    #re_path('^', include('apps.memberits.urls', namespace='member-it')),
]
