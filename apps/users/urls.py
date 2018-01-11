# -*- coding: utf-8 -*-
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    # User registration and authentication views
    path('login/',
        auth_views.LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='registration/login.html'
        ), 
        name='login'
    ),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('sign_up/', views.sign_up, name='user_sign_up'),

    # User related views
    path('', views.user_index, name='user_index'),

    # Social related views
    path('profiles/@<str:username>', views.user_profile, name='user_profile'),

    # Include user member-its urls
    path('', include('apps.memberits.urls', namespace='member-it')),
]
