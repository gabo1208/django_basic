# Generated by Django 2.0.2 on 2018-04-26 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('quiniela', '0017_groupteam_games_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiniela',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
