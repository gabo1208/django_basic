# Generated by Django 2.0.2 on 2018-04-24 16:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('quiniela', '0004_auto_20180424_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('score_home', models.IntegerField(default=0)),
                ('score_away', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='memberfixture',
            name='games',
        ),
        migrations.AlterField(
            model_name='game',
            name='score_away',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='score_home',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gameresult',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiniela.Game'),
        ),
        migrations.AddField(
            model_name='gameresult',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='memberfixture',
            name='results',
            field=models.ManyToManyField(related_name='member_fixture_game_results', to='quiniela.GameResult'),
        ),
    ]
