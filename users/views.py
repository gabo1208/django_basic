# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile, ProfilePreferences


def index(request):
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
