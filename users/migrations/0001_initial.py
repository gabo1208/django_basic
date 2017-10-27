# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 03:09
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('tags', models.ManyToManyField(related_name='interest_tag', to='users.InterestTag')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileMessageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TimeStampedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.TimeStampedModel')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to=b'')),
            ],
            bases=('users.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.TimeStampedModel')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to=b'')),
            ],
            bases=('users.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.TimeStampedModel')),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('mail', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to=b'')),
                ('reputation', models.DecimalField(decimal_places=1, default=Decimal('0.00'), max_digits=3)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('NU', 'Normal User'), ('VU', 'VIP'), ('EU', 'Entreprise'), ('OU', 'Organization'), ('SU', 'Staff'), ('AU', 'Admin')], default='NU', max_length=2)),
                ('events', models.ManyToManyField(blank=True, related_name='profile_events', to='users.Event')),
                ('followers', models.ManyToManyField(blank=True, related_name='_profile_followers_+', to='users.Profile')),
                ('following', models.ManyToManyField(blank=True, related_name='_profile_following_+', to='users.Profile')),
                ('friends', models.ManyToManyField(blank=True, related_name='_profile_friends_+', to='users.Profile')),
                ('groups', models.ManyToManyField(blank=True, related_name='profile_groups', to='users.Group')),
                ('interests', models.ManyToManyField(blank=True, related_name='profile_interests', to='users.ProfileInterest')),
            ],
            bases=('users.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='ProfileMessage',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.TimeStampedModel')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
            bases=('users.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='ProfilePreferences',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.TimeStampedModel')),
                ('option1', models.BooleanField(default=True)),
            ],
            bases=('users.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='ProfileRequest',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.TimeStampedModel')),
                ('reason', models.CharField(choices=[('FL', 'Invitation so you could see users Activity.'), ('FR', 'Invitation to become Friends.'), ('EV', 'Invitation to an Event.'), ('GR', 'Invitation to become part of a Group.'), ('OR', 'Invitation to become part of an Organization.'), ('EN', 'Invitation to become part of an Enterprise.')], default='FL', max_length=2)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
                ('sugested_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_event_sugested', to='users.Event')),
                ('sugested_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_group_sugested', to='users.Group')),
                ('sugested_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_user_sugested', to='users.Profile')),
            ],
            bases=('users.timestampedmodel',),
        ),
        migrations.AddField(
            model_name='profilemessagehistory',
            name='message_history',
            field=models.ManyToManyField(related_name='profile_messages_history_messages', to='users.ProfileMessage'),
        ),
        migrations.AddField(
            model_name='profilemessagehistory',
            name='profile1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile1', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='profilemessagehistory',
            name='profile2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile2', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='message_history',
            field=models.ManyToManyField(blank=True, related_name='profile_message_history', to='users.ProfileMessageHistory'),
        ),
        migrations.AddField(
            model_name='profile',
            name='preferences',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ProfilePreferences'),
        ),
        migrations.AddField(
            model_name='profile',
            name='requests',
            field=models.ManyToManyField(blank=True, related_name='profile_requests', to='users.ProfileRequest'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='group_admins', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='group_members', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='invited',
            field=models.ManyToManyField(blank=True, related_name='event_invited', to='users.ProfileRequest'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizers',
            field=models.ManyToManyField(blank=True, related_name='event_organizers', to='users.Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='profilerequest',
            unique_together=set([('from_user', 'sugested_user', 'reason')]),
        ),
        migrations.AlterUniqueTogether(
            name='profilemessagehistory',
            unique_together=set([('profile1', 'profile2')]),
        ),
    ]
