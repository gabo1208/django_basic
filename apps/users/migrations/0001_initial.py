# Generated by Django 2.0.2 on 2018-04-13 00:13

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterestTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('mail', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('reputation', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=3)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('NU', 'Normal User'), ('VU', 'VIP'), ('EU', 'Entreprise'), ('OU', 'Organization'), ('SU', 'Staff'), ('AU', 'Admin')], default='NU', max_length=2)),
                ('events', models.ManyToManyField(blank=True, related_name='profile_events', to='users.Event')),
                ('followers', models.ManyToManyField(blank=True, related_name='_profile_followers_+', to='users.Profile')),
                ('following', models.ManyToManyField(blank=True, related_name='_profile_following_+', to='users.Profile')),
                ('friends', models.ManyToManyField(blank=True, related_name='_profile_friends_+', to='users.Profile')),
                ('groups', models.ManyToManyField(blank=True, related_name='profile_groups', to='users.Group')),
            ],
            options={
                'abstract': False,
            },
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
            name='ProfileMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileMessageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_history', models.ManyToManyField(related_name='profile_messages_history_messages', to='users.ProfileMessage')),
                ('profile1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile1', to='users.Profile')),
                ('profile2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile2', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('reason', models.CharField(choices=[('FL', 'Invitation so you could see users Activity.'), ('FR', 'Invitation to become Friends.'), ('EV', 'Invitation to an Event.'), ('GR', 'Invitation to become part of a Group.'), ('OR', 'Invitation to become part of an Organization.'), ('EN', 'Invitation to become part of an Enterprise.')], default='FL', max_length=2)),
                ('status', models.CharField(choices=[('1', 'Pending Request'), ('0', 'Request Responded'), ('2', 'Request Canceled')], default='1', max_length=1)),
                ('seen', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Profile')),
                ('sugested_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='request_event_sugested', to='users.Event')),
                ('sugested_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='request_group_sugested', to='users.Group')),
                ('sugested_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='request_user_sugested', to='users.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='profile_interests', to='users.ProfileInterest'),
        ),
        migrations.AddField(
            model_name='profile',
            name='message_history',
            field=models.ManyToManyField(blank=True, related_name='profile_message_history', to='users.ProfileMessageHistory'),
        ),
        migrations.AddField(
            model_name='profile',
            name='preferences',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.ProfilePreferences'),
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
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='group_members', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Profile'),
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
            unique_together={('from_user', 'sugested_user', 'reason')},
        ),
        migrations.AlterUniqueTogether(
            name='profilemessagehistory',
            unique_together={('profile1', 'profile2')},
        ),
    ]
