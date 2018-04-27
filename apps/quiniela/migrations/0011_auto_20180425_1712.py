# Generated by Django 2.0.2 on 2018-04-25 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0010_auto_20180425_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('name', 'tournament')},
        ),
        migrations.AlterUniqueTogether(
            name='groupteam',
            unique_together={('team', 'group')},
        ),
    ]
