# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # TODO authentication via token for the api #
    url(r'^hello', views.ApiHello.as_view(), name='api_hello'),
    url(r'^login/$', views.ApiLogin.as_view(), name='api_login'),
    # Get all users #
    url(r'^users/(?P<like>\w*)', views.users_like, name='users_like'),
    url(r'^user_to_user/$', views.User2UserRequest.as_view(), name='user_2_user_request'),

    url(r'^request/confirm$', views.ConfirmRequest.as_view(), name='user_request_confirm'),
]
