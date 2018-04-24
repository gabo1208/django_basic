# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, UserCreationForm, UserLoginForm
from .models import User


# Login for user mail or username
def user_login(request):
    if request.user.is_authenticated:
        return redirect('users:user_index')
    else:
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('users:user_index')
        else:
            form = UserLoginForm()

        return render(request, 'registration/login.html', context={"form": form})


# Home profile view for requested user
@login_required
def user_index(request):
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)

    if request.method == 'POST':
        if profile_form.is_valid():
            profile = profile_form.save()

    return render(
        request,
        'user_index.html',
        context={
            "form": profile_form,
        }
    )
    return render(request, 'index.html', context={'msg': "Hello, world. You're at index."})


# View to sign up a new user // TODO: organization and enterprises cases
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # Check if user form is Valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            # Authenticate the user and redirect it to home view
            login(request, user)
            return redirect('users:user_index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', context={"form": form})


# Any user profile view
def user_profile(request, username):
    if request.user.is_authenticated:
        user = request.user
        current_profile = request.user.profile

        return render(
            request,
            'user_profile.html',
            context={
                "userprofile": user,
                "friends": current_profile.check_if_friends(user.profile),
                "friends_request": user.profile.get_if_request_from_user(current_profile, 'FR'),
                "following": current_profile.check_if_following(user.profile),
                "follow_request": user.profile.get_if_request_from_user(current_profile, 'FL'),
                "follower": current_profile.check_if_follower(user.profile),
            }
        )
    else:

        return render(
            request,
            'user_profile.html',
            context={
                "userprofile": user
            }
        )
