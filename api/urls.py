# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # TODO authentication via token for the api #
    # Get all users #
    url(r'^users/(?P<like>\w*)', views.users_like),
]
