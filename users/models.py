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


class InterestTag(models.Model):
    name = models.CharField(max_length=50, unique=True)


class ProfileInterest(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tags = models.ManyToManyField(InterestTag, related_name="interest_tag")


class Group(TimeStampedModel):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    image = models.ImageField(null=True)
    created_by = models.ForeignKey('Profile', on_delete=models.CASCADE)
    admins = models.ManyToManyField('Profile', blank=True, related_name="group_admins")
    members = models.ManyToManyField('Profile', blank=True, related_name="group_members")


class Event(TimeStampedModel):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField(null=True)
    created_by = models.ForeignKey('Profile')
    organizers = models.ManyToManyField(
        'Profile',
        blank=True,
        related_name="event_organizers"
    )
    invited = models.ManyToManyField(
        'ProfileRequest',
        blank=True,
        related_name="event_invited"
    )


class ProfileRequest(TimeStampedModel):
    FOLLOW = 'FL'
    FRIENDS = 'FR'
    EVENT = 'EV'
    GROUP = 'GR'
    ORGANIZATION = 'OR'
    ENTERPRISE = 'EN'

    USER_REQUEST_CHOICES = (
        (FOLLOW, 'Invitation so you could see users Activity.'),
        (FRIENDS, 'Invitation to become Friends.'),
        (EVENT, 'Invitation to an Event.'),
        (GROUP, 'Invitation to become part of a Group.'),
        (ORGANIZATION, 'Invitation to become part of an Organization.'),
        (ENTERPRISE, 'Invitation to become part of an Enterprise.'),
    )
    from_user = models.ForeignKey('Profile')
    sugested_user = models.ForeignKey(
        'Profile',
        related_name="request_user_sugested",
        blank=True,
        null=True
    )
    sugested_event = models.ForeignKey(
        Event,
        related_name="request_event_sugested",
        blank=True,
        null=True
    )
    sugested_group = models.ForeignKey(
        Group,
        related_name="request_group_sugested",
        blank=True,
        null=True
    )
    message = models.CharField(max_length=50)
    reason = models.CharField(max_length=2, choices=USER_REQUEST_CHOICES)


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
    # Social Related Relations
    following = models.ManyToManyField("Profile", blank=True, related_name="profile_folowing")
    followers = models.ManyToManyField("Profile", blank=True, related_name="profile_folowers")
    interests = models.ManyToManyField(ProfileInterest, blank=True, related_name="profile_interests")
    requests = models.ManyToManyField(ProfileRequest, blank=True, related_name="profile_requests")
    events = models.ManyToManyField(Event, blank=True, related_name="profile_envents")
    groups = models.ManyToManyField(Group, blank=True, related_name="profile_groups")
