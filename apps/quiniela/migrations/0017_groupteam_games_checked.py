# Generated by Django 2.0.2 on 2018-04-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0016_quiniela_score_type_cache'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupteam',
            name='games_checked',
            field=models.IntegerField(default=0),
        ),
    ]
