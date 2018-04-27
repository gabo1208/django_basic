# Generated by Django 2.0.2 on 2018-04-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0015_quiniela_score_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiniela',
            name='score_type_cache',
            field=models.CharField(choices=[('TO', 'Game Result Points.'), ('EA', 'Game Result and Teams Score Points.')], default='TO', editable=False, max_length=2),
        ),
    ]