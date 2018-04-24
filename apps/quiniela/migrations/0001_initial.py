# Generated by Django 2.0.2 on 2018-04-23 16:46

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_home', models.CharField(default='0', max_length=3)),
                ('score_away', models.CharField(default='0', max_length=3)),
                ('limit_date', models.DateField(blank=True, null=True)),
                ('match_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiniela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('description', models.CharField(default='', max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('history', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('description', models.CharField(max_length=150, unique=True)),
                ('start_in', models.DateField(blank=True, null=True)),
                ('ends_in', models.DateField(blank=True, null=True)),
                ('fixture', models.ManyToManyField(related_name='fixture_games', to='quiniela.Game')),
            ],
        ),
    ]
