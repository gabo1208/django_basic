# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    url('', views.home, name='home'),
]