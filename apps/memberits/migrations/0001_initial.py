# Generated by Django 2.0.2 on 2018-02-26 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_auto_20180110_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='memberIt',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.TimeStampedModel')),
            ],
            bases=('users.timestampedmodel',),
        ),
    ]
