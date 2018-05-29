# -*- coding: utf-8 -*-

from django.contrib.auth import views as auth_views
from django.urls import re_path, include, reverse_lazy

from . import views

app_name = 'users'
urlpatterns = [
    # User registration and authentication views
    re_path('^login/$', views.user_login, name='login'),
    re_path(
        '^logout/$',
        auth_views.LogoutView.as_view(next_page='/'),
        name='logout'
    ),
    re_path('^sign_up/$', views.sign_up, name='user_sign_up'),

    # Password reset related views
    re_path(
        r'^password_reset/$',
        auth_views.password_reset,
        {
            'post_reset_redirect': reverse_lazy('users:password_reset_done'),
        },
        name='password_reset'),
    re_path(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {
            'post_reset_redirect': reverse_lazy('users:password_reset_complete'),
        },
        name='password_reset_confirm'),
    re_path('', include('django.contrib.auth.urls')),


    # User related views
    # re_path('^$', views.user_index, name='user_index'),

    # Social related views
    # path('profiles/@<str:username>', views.user_profile, name='user_profile'),

    # Include user member-its urls
    # re_path('^', include('apps.memberits.urls', namespace='member-it')),
]
