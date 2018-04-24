# Generated by Django 2.0.2 on 2018-04-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180423_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='event_tag', to='users.InterestTag'),
        ),
        migrations.AlterField(
            model_name='profileinterest',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='interest_tag', to='users.InterestTag'),
        ),
    ]
