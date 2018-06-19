# Generated by Django 2.0.2 on 2018-06-19 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='penalties',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='penalties_away',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='penalties_home',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='groupteam',
            name='extra',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='groupteam',
            name='goals_difference',
            field=models.IntegerField(default=0),
        ),
    ]