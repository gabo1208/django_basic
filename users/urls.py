# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    url(r'^$', views.index, name='user_index'),
    url(r'^logout/admin/$', logout, {'next_page': '/'}),
    url(r'^decorator_index/$', views.index_decorator, name='user_logged_decorator'),
    url(r'^aspect_index/$', views.index_aspect, name='user_logged_aspect'),
]
