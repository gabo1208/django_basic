# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib.auth.views import logout, login

from . import views

urlpatterns = [
    # User registration and authentication views
    url(r'^login/$', login, kwargs={'redirect_authenticated_user': True}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^sign_up/$', views.sign_up, name='user_sign_up'),

    # User related views
    url(r'^$', views.user_index, name='user_index'),

    # Social related views
    url(r'^profiles/@(?P<username>\w+)$', views.user_profile, name='user_profile'),

    # Include user member-its urls
    url(r'^', include('memberits.urls', namespace='member-it')),
]
