# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from .models import Profile, ProfilePreferences
from .forms import ProfileForm


# Home profile view for requested user
def user_index(request):
    profile_form = ProfileForm(request.POST or None, instance=request.user.profile)
    
    if request.method == 'POST':
        if profile_form.is_valid():
            profile_form.save()

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
            # Create profile with its options and asociate it with the created user
            preferences = ProfilePreferences()
            preferences.save()
            profile = Profile(user=user, preferences=preferences)
            profile.save()
            # Authenticate the user and redirect it to home view
            login(request, user)
            return redirect('users:user_index')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', context={"form": form})


# Any user profile view
def user_profile(request, username):
    user = get_object_or_404(User, username=username)

    return render(
        request,
        'user_profile.html',
        context={
            "userprofile": user,
            "friends": request.user.profile.check_if_friends(user.profile),
            "friends_request": user.profile.check_if_request_from_user(request.user.profile, 'FR'),
            "following": request.user.profile.check_if_following(user.profile),
            "follow_request": user.profile.get_if_request_from_user(request.user.profile, 'FL'),
            "follower": request.user.profile.check_if_follower(user.profile),
        }
    )
