# Generated by Django 2.0.2 on 2018-05-13 00:07

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiniela', '0002_auto_20180501_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='OscarCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('value', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
