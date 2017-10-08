# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProfilePreferences(TimeStampedModel):
    option1 = models.BooleanField(default=True)


class Profile(TimeStampedModel):
    NORMAL = 'NU'
    VIP = 'VU'
    ENTERPRISE = 'EU'
    STAFF = 'SU'
    ADMIN = 'AU'

    USER_ROLE_CHOICES = (
        (NORMAL, 'Normal User'),
        (VIP, 'VIP'),
        (ENTERPRISE, 'Entreprise'),
        (STAFF, 'Staff'),
        (ADMIN, 'Admin'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    preferences = models.ForeignKey('ProfilePreferences')
    role = models.CharField(
        max_length=2,
        choices=USER_ROLE_CHOICES,
        default=NORMAL,
    )
