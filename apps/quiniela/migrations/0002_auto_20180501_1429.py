# Generated by Django 2.0.2 on 2018-05-01 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('quiniela', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='memberfixture',
            unique_together={('user', 'tournament', 'quiniela')},
        ),
    ]
