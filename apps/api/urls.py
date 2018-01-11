# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'api'
urlpatterns = [
    # TODO authentication via token for the api #
    url('hello', views.ApiHello.as_view(), name='api_hello'),
    url('login/', views.ApiLogin.as_view(), name='api_login'),
    # Get all users #
    url('users/<str:like>', views.users_like, name='users_like'),
    url('user_to_user/', views.User2UserRequest.as_view(), name='user_2_user_request'),

    url('request/confirm', views.ConfirmRequest.as_view(), name='user_request_confirm'),
]
