# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 00:24
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171015_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='folowers', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='folowing', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='reputation',
            field=models.DecimalField(decimal_places=1, default=Decimal('0.00'), max_digits=3),
        ),
    ]
