# Generated by Django 2.0.2 on 2018-04-28 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0022_auto_20180427_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='quiniela.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='quiniela.Team'),
        ),
    ]