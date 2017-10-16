# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    url(r'^$', views.index, name='user_index'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^sign_up/$', views.sign_up, name='user_sign_up'),
]
