# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib.auth.views import logout, login

from . import views

urlpatterns = [
    url(r'^$', views.index, name='user_index'),
    url(r'^login/$', login, kwargs={'redirect_authenticated_user': True}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^sign_up/$', views.sign_up, name='user_sign_up'),
    # Include user member-its urls
    url(r'^', include('memberits.urls', namespace='member-it')),
]
