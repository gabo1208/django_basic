# Generated by Django 2.0.2 on 2018-04-27 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('quiniela', '0019_auto_20180426_1831'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='quiniela',
            unique_together={('admin', 'name', 'tournament')},
        ),
    ]