# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from decimal import Decimal

from model_utils.models import TimeStampedModel

from apps.users.models import Profile, InterestTag


class MemberIt(TimeStampedModel):
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    score = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=Decimal('0.00')
    )

    description = models.CharField(max_length=50, blank=True, null=True)
    annotations = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=50, blank=True, null=True)
    tags = models.ManyToManyField(InterestTag, related_name="memberit_tag", blank=True)
