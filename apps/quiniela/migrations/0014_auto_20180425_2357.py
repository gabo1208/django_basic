# Generated by Django 2.0.2 on 2018-04-26 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0013_game_score_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='fixture',
            field=models.ManyToManyField(blank=True, related_name='fixture_games', to='quiniela.Game'),
        ),
    ]
