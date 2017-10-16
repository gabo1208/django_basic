# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProfilePreferences(TimeStampedModel):
    option1 = models.BooleanField(default=True)


class Profile(TimeStampedModel):
    NORMAL = 'NU'
    VIP = 'VU'
    ENTERPRISE = 'EU'
    ORGANIZATION = 'OU'
    STAFF = 'SU'
    ADMIN = 'AU'

    USER_ROLE_CHOICES = (
        (NORMAL, 'Normal User'),
        (VIP, 'VIP'),
        (ENTERPRISE, 'Entreprise'),
        (ORGANIZATION, 'Organization'),
        (STAFF, 'Staff'),
        (ADMIN, 'Admin'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    reputation = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=Decimal('0.00')
    )
    description = models.CharField(max_length=50, blank=True, null=True)
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    preferences = models.ForeignKey('ProfilePreferences')
    role = models.CharField(
        max_length=2,
        choices=USER_ROLE_CHOICES,
        default=NORMAL,
    )
    following = models.ManyToManyField("Profile", blank=True, related_name="folowing")
    followers = models.ManyToManyField("Profile", blank=True, related_name="folowers")
