# Generated by Django 2.0.2 on 2018-04-23 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixture',
            name='games',
        ),
        migrations.RemoveField(
            model_name='fixture',
            name='tournament',
        ),
        migrations.AddField(
            model_name='tournament',
            name='fixture',
            field=models.ManyToManyField(related_name='fixture_games', to='quiniela.Game'),
        ),
        migrations.DeleteModel(
            name='Fixture',
        ),
    ]
