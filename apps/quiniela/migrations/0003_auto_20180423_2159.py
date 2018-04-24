# Generated by Django 2.0.2 on 2018-04-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0002_auto_20180423_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiniela',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='quiniela_tag', to='users.InterestTag'),
        ),
        migrations.AlterField(
            model_name='team',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='team_tag', to='users.InterestTag'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tournament_tag', to='users.InterestTag'),
        ),
    ]
