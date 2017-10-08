# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile, ProfilePreferences

admin.site.register(Profile)
admin.site.register(ProfilePreferences)
