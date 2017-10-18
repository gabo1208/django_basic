# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('NU', 'Normal User'), ('VU', 'VIP'), ('EU', 'Entreprise'), ('OU', 'Organization'), ('SU', 'Staff'), ('AU', 'Admin')], default='NU', max_length=2),
        ),
    ]