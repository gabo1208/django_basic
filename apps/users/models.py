# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    created_by = models.ForeignKey(
        'Profile',
        on_delete=models.DO_NOTHING
    )
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

    #date
    #asisted
    #tickets until
    #event_photos
    #recurrent
    #restrictions
    #score
    #colaborators
    #aliances
    #tags


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

    CANCELED = '2'
    PENDING = '1'
    ANSWERED = '0'

    STATUS_CHOICES = (
        (PENDING, 'Pending Request'),
        (ANSWERED, 'Request Responded'),
        (CANCELED, 'Request Canceled')
    )

    from_user = models.ForeignKey('Profile', on_delete=models.DO_NOTHING)
    sugested_user = models.ForeignKey(
        'Profile',
        related_name="request_user_sugested",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )
    sugested_event = models.ForeignKey(
        Event,
        related_name="request_event_sugested",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )
    sugested_group = models.ForeignKey(
        Group,
        related_name="request_group_sugested",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )
    reason = models.CharField(
        max_length=2,
        choices=USER_REQUEST_CHOICES,
        default=FOLLOW
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=PENDING
    )

    class Meta:
        unique_together = ('from_user', 'sugested_user', 'reason')


class ProfileMessage(TimeStampedModel):
    created_by = models.ForeignKey('Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)


class ProfileMessageHistory(models.Model):
    profile1 = models.ForeignKey(
        'Profile',
        related_name="profile1",
        on_delete=models.DO_NOTHING
    )
    profile2 = models.ForeignKey('Profile',
        related_name="profile2",
        on_delete=models.DO_NOTHING
    )
    message_history = models.ManyToManyField(
        ProfileMessage,
        related_name="profile_messages_history_messages"
    )

    class Meta:
        unique_together = ('profile1', 'profile2')


# Profile Model, the base of the Users Interface
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

    #member_its = blah

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(null=True)
    reputation = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=Decimal('0.00')
    )

    description = models.CharField(max_length=50, blank=True, null=True)
    verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    preferences = models.ForeignKey(ProfilePreferences, on_delete=models.DO_NOTHING)
    role = models.CharField(
        max_length=2,
        choices=USER_ROLE_CHOICES,
        default=NORMAL,
    )
    # Social Related Relations---------
    # Profiles followed by self profile
    following = models.ManyToManyField(
        'self',
        blank=True,
        related_name="profile_folowing"
    )
    # Profiles following by self profile
    followers = models.ManyToManyField(
        'self',
        blank=True,
        related_name="profile_folowers"
    )
    # Profiles friends of self profile
    friends = models.ManyToManyField(
        'self',
        blank=True,
        related_name="profile_friends"
    )
    # Profile interests
    interests = models.ManyToManyField(
        ProfileInterest,
        blank=True,
        related_name="profile_interests"
    )
    # Request sent to profile
    requests = models.ManyToManyField(
        ProfileRequest,
        blank=True,
        related_name="profile_requests"
    )
    # Events accepted by profile
    events = models.ManyToManyField(
        Event,
        blank=True,
        related_name="profile_events"
    )
    # Profile accepted Groups
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name="profile_groups"
    )
    # TODO: groups message history
    message_history = models.ManyToManyField(
        ProfileMessageHistory,
        blank=True,
        related_name="profile_message_history"
    )

    def check_if_friends(self, user):
        return user in self.friends.all()

    def check_if_follower(self, user):
        return user in self.followers.all()

    def check_if_following(self, user):
        return user in self.following.all()

    def check_if_repeated_interest(self, interest):
        return interest in self.insterests.all()

    def get_if_request_from_user(self, user, reason):
        return self.requests.filter(
            reason=reason,
            from_user=user
        )

    def check_if_repeated_event(self, event):
        return event in self.events.all()

    def check_if_already_in_group(self, group):
        return group in self.groups.all()

    def get_pending_requests(self):
        return self.requests.filter(status='1')

    # TODO: This -------------------------------
    def get_if_have_messages_with(self, user):
        return (
            self.messages.filter(profile1=user) |
            self.messages.filter(profile2=user)
        )
